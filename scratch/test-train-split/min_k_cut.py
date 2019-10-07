import networkx as nx
import random

import matplotlib.pyplot as plt
import randomcolor
from itertools import groupby
from functools import reduce

def make_contractable(graph):
	return nx.relabel_nodes(nx.Graph(graph), lambda node: frozenset({node}))

# combines two vertices into one and sums up the weights of the same neighbors
def contract(graph, edge):
    (v,w) = edge
    contracted = v.union(w)
    graph.add_node(contracted)

    def weighted_neighbors(v):
        return map(lambda n:
                    (contracted, n, graph[n][v]['weight'])
                  , graph.neighbors(v))

    all_neighbors = list(weighted_neighbors(v)) + list(weighted_neighbors(w))

    def same_edge(e1_e2_weight):
        (e1,e2,weight) = e1_e2_weight
        return (e1,e2)

    all_neighbors.sort(key=lambda e: str(same_edge(e)))

    joined_neighbors = []
    for k, g in groupby(all_neighbors, key=same_edge):
        s = sum(map(lambda l: l[2], g))
        (e1,e2) = k
        joined_neighbors.append((e1,e2,s))

    graph.add_weighted_edges_from(joined_neighbors)
    graph.remove_nodes_from([v,w])
    
    return contracted

""" This is the min k cut algorithm, it's a modified krager's algorithm
 that stops whenever the contracted node has more vertices than we want
"""
def k_krager(original_graph, n):
    graph = nx.Graph(original_graph)
    def get_contracted():    
        weights = map(lambda vw: graph[vw[0]][vw[1]]['weight'], graph.edges())
        chosen_edge = random.choices(list(graph.edges()) , list(weights))[0]
        return contract(graph, chosen_edge)

    contracted = get_contracted()
    while(len(contracted) < n):
        contracted = get_contracted()
    cut_size = sum(map(lambda n: graph[n][contracted]['weight'], graph[contracted]))

    kept = original_graph.subgraph(map(lambda v: frozenset({v}),contracted))
    
    rest = nx.Graph(original_graph)
    rest.remove_nodes_from(kept.nodes)
    
    return {'contracted_size': len(contracted), 'cut_size': cut_size, 'kept': kept, 'rest': rest}

def draw_graph(graph):
    fig = plt.figure()
    fig.set_figheight(15)
    fig.set_figwidth(15)

    pos = nx.spring_layout(graph, weight=None,k=0.15)
    nx.draw_networkx_nodes(graph, pos, graph.nodes(),
                                    node_color = randomcolor.RandomColor().generate()[0])
    nx.draw_networkx_edges(graph,pos)
    nx.draw_networkx_edge_labels(graph, pos,nx.get_edge_attributes(graph,'weight'));


# runs the k_kgrager algorithm n times and gets the best cuts when they overlap
def run_multiple(contractable, n, repetitions):
    cuts = {}
    for _ in range(repetitions):
        cut = k_krager(contractable, n)
        cut_size = cut['contracted_size']
        if cut_size in cuts:
            cuts[cut_size] = min(cuts[cut_size], cut, key=lambda c: c['contracted_size'])
        else:
            cuts[cut_size] = cut
    return cuts

def merge(A,B, merger):
    return {k: merger(A[k], B[k]) if k in A and k in B else A.get(k, B.get(k))
            for k in A.keys() | B.keys()}

# runs the run_multiple algorithm over a range and chooses the best cuts on each n
def run_many_over_range(contractable, repetitions, range):
	def min_by_cut_size(cut_A,cut_B):
	    return min(cut_A,cut_B,key=lambda x: x['cut_size'])

	multiple_runs = map(lambda i: run_multiple(contractable, i, repetitions), range)
	return reduce(lambda A,B: merge(A,B, min_by_cut_size), multiple_runs)


def random_graph(num_nodes, prob_of_edge, seed=100):
	G = nx.fast_gnp_random_graph(num_nodes, prob_of_edge, seed=seed)
	edges = list(G.edges)
	G.remove_edges_from(edges)
	
	def add_weight(edge):
	    (v,w) = edge
	    return (v,w,random.randrange(1,3))

	G.add_weighted_edges_from(map(add_weight,edges))
	return G