import json
d = json.load(open('aquarium-operations.json'))

map_container_to_cty = {
    '0.6 mL tube of digested Fragment': ['tube','0.6 mL'],
    '0.6mL tube of Digested Plasmid': ['tube','0.6 mL'],
    '1 L Liquid': ['liquid','1 L'],
    '1 ng/µL Fragment Stock': ['stock','1 ng/µL'],
    '1 ng/µL Plasmid Stock': ['stock','1 ng/µL'],
    '1 ng/ÂµL Fragment Stock': ['stock','1 ng/µL'],
    '1 ng/ÂµL Plasmid Stock': ['stock','1 ng/µL'],
    '100 mL Bottle': ['bottle','100 mL'],
    '12% SDS Gel in Coomassie Staining': ['staining',''],
    '12% SDS Gel in Tank': ['tank',''],
    '12-Well TC Dish': ['dish',''],
    '1X LUDOX Aliquot': ['aliquot',''],
    '1mM Fluorescein Stock': ['stock','1 mM'],
    '2 mL Screw Cap Tube': ['tube','2 mL'],
    '200 mL Agar': ['agar','200 mL'],
    '200 mL Liquid': ['liquid','200 mL'],
    '200 mL Liquid (Reagents)': ['liquid','200 mL'],
    '24 Deep Well Plate': ['plate','200 mL'],
    '24-Slot Tube Rack': ['tube',''],
    '24-Well TC Dish': ['dish',''],
    '250 mL Bottle': ['bottle','250 mL'],
    '40 fmole/µL Fragment Stock': ['stock','40 fmole/µL'],
    '40 fmole/µL Plasmid Stock': ['stock','40 fmole/µL'],
    '400 mL Agar': ['agar','400 mL'],
    '400 mL Liquid': ['liquid','400 mL'],
    '50 mL 0.8 Percent Agarose Gel in Gel Box': ['box','50 mL'],
    '50 mL Agarose FULL Gel Box': ['box','50 mL'],
    '50 mL Agarose Gel in Gel Box': ['box','50 mL'],
    '500 mL Liquid': ['liquid','500 mL'],
    '500 mL TC Media Bottle': ['bottle','500 mL'],
    '500mL bottle': ['bottle','500 mL'],
    '50L Nalgene Tank': ['tank','50 L'],
    '50X PCR Template': ['template',''],
    '50mL Agarose Gel in Gel Box': ['box','50 mL'],
    '6-well TC Dish': ['dish',''],
    '800 mL Agar': ['agar','800 mL'],
    '800 mL Liquid': ['liquid','800 mL'],
    '96 File Matrix': ['matrix',''],
    '96 U-bottom Cell Culture Plate': ['plate',''],
    '96 U-bottom Well Plate': ['plate',''],
    '96 Well Flat Bottom (black)': ['flat',''],
    '96 Well PCR Plate': ['plate',''],
    '96 qPCR collection': ['collection',''],
    '96 shallow plate (M20) part': ['plate',''],
    '96-Well Primer Aliquot Plate': ['plate',''],
    '96-well TC Dish': ['dish',''],
    'Addgene Order': ['order',''],
    'Agar Plate Batch': ['batch',''],
    'Agar Stab': ['stab',''],
    'Agar Vial Batch': ['batch',''],
    'Agar plate': ['plate',''],
    'Agro competent cell batch': ['batch',''],
    'Agro glycerol stock': ['stock',''],
    'Agro large volume culture': ['culture',''],
    'Agro overnight culture': ['culture',''],
    'Alignment Marker Stock': ['stock',''],
    'Amplified Fragment Library': ['library',''],
    'Antibody Stock': ['stock',''],
    'Arabidopsis T1 seedlings on soil': ['soil',''],
    'Arabidopsis T1 seedstock': ['stock',''],
    'Arabidopsis T2 seedstock': ['stock',''],
    'Arabidopsis T3 seedlings on soil': ['soil',''],
    'Arabidopsis T3 seedstock': ['stock',''],
    'Arabidopsis T3 selection plate': ['plate',''],
    'Arabidopsis seedlings on soil': ['soil',''],
    'Arabidopsis seedstock': ['stock',''],
    'Bead droplet dispenser': ['dispenser',''],
    'Bottle': ['bottle',''],
    'Cas9::sgRNA Complex Tube': ['tube',''],
    'Cell Lysate of Protein Expression': ['expression',''],
    'Cell Pellet of protein': ['pellet',''],
    'Cell Suspension': ['suspension',''],
    'Checked E coli Plate of Plasmid': ['plate',''],
    'Checked Yeast Plate': ['plate',''],
    'Column': ['column',''],
    'Concentrated Lentivirus Aliquot': ['aliquot',''],
    'Concentrated Lentivirus Harvest': ['harvest',''],
    'Concentrated Protein': ['protein',''],
    'Cryostock (old)': ['cryostock',''],
    'Customer Container': ['container',''],
    'DNA Complex': ['complex',''],
    'DNA Mix': ['mix',''],
    'Divided Yeast Plate': ['plate',''],
    'Dried Fragment Mix': ['mix',''],
    'Dried tissue pool': ['pool',''],
    'E coli Glycerol Stock': ['stock',''],
    'E coli Plate of Plasmid': ['plate',''],
    'E. coli Comp Cell Batch': ['batch',''],
    'Enzyme Stock': ['stock',''],
    'Eppendorf 96 Deepwell Plate': ['plate',''],
    'Flat of Arabidopsis': ['flat',''],
    'Flat of Arabidopsis T1 plants': ['flat',''],
    'Flat of T0 plants': ['flat',''],
    'Fragment Library': ['library',''],
    'Fragment Stock': ['stock',''],
    'GUS stained Leaf discs': ['discs',''],
    'Gel Slice': ['slice',''],
    'Gibson Aliquot Batch': ['batch',''],
    'Gibson Reaction Result': ['result',''],
    'Golden Gate Stripwell': ['stripwell',''],
    'Harvested Arabidopsis tissue': ['tissue',''],
    'Hydra Dish': ['dish',''],
    'Hydra Tray': ['tray',''],
    'Illuminated Fragment Library': ['library',''],
    'Isolated RNA': ['isolated',''],
    'Labeled Yeast Library Suspension': ['suspension',''],
    'Labeled Yeast Strain Suspension': ['suspension',''],
    'Ladder Stock': ['stock',''],
    'Laemmli Sample Buffer': ['buffer',''],
    'Lentivirus Aliquot': ['aliquot',''],
    'Lentivirus DNA Complex': ['complex',''],
    'Lentivirus Harvest': ['harvest',''],
    'Lentivirus T75 Packaging Plate': ['plate',''],
    'Lentivirus T75 Transfected Plate': ['plate',''],
    'Library Gel Slice': ['slice',''],
    'Library Stock': ['stock',''],
    'Ligation product': ['product',''],
    'Lyophilized Fragment': ['fragment',''],
    'Lyophilized Primer': ['primer',''],
    'Lyopholized Library': ['library',''],
    'Maxiprep Stock': ['stock',''],
    'Midiprep Stock': ['stock',''],
    'Multiple Gel Slices': ['slices',''],
    'Normalized Illuminated Fragment Library': ['library',''],
    'OLA Detection Strips': ['strips',''],
    'OLA Ligation Stripwell': ['stripwell',''],
    'OLA PCR': ['PCR',''],
    'OLA Whole Blood': ['blood',''],
    'OLA lysed blood': ['blood',''],
    'OLASimple Synthetic DNA': ['DNA',''],
    'Ordered': ['?',''],
    'Overexpression of Plasmid': ['overexpression',''],
    'Overnight suspension': ['suspension',''],
    'PCR Result': ['result',''],
    'PEG Precipitated Lentivirus Harvest': ['harvest',''],
    'Phosphorylated fragment stock': ['stock',''],
    'Plasmid Glycerol Stock': ['stock',''],
    'Plasmid Library': ['library',''],
    'Plasmid Stock': ['stock',''],
    'Plasmid Stock in Ethanol': ['stock',''],
    'Plate Request': ['plate',''],
    'Plate of Agro': ['plate',''],
    'Plate of transformed Agro': ['plate',''],
    'Post-exonuclease': ['entity',''],
    'Pot of N. benthamiana seedlings': ['pot',''],
    'Primer Aliquot': ['aliquot',''],
    'Primer Mix Stock': ['stock',''],
    'Primer Stock': ['stock',''],
    'Protease Stock': ['stock',''],
    'Protein Elution': ['elution',''],
    'Purified Plasmid Stock': ['stock',''],
    'QC Certificate': ['certificate',''],
    'Resuspended Library': ['library',''],
    'Seed Bag': ['bag',''],
    'Seed Cryostock': ['stock',''],
    'Sequencing Result': ['result',''],
    'Sequencing Result (Fragment)': ['result',''],
    'Sequencing Stripwell': ['stripwell',''],
    'Serial Dilution': ['dilution',''],
    'Stripwell': ['stripwell',''],
    'Stripwell of Digested Plasmid': ['stripwell',''],
    'T175': ['T',''],
    'T25': ['T',''],
    'T75': ['T',''],
    'TB Overnight (400 mL) of Plasmid': ['TB',''],
    'TB Overnight of Plasmid': ['TB',''],
    'TB Overnight of Plasmid (large)': ['TB',''],
    'Transformed Agro Aliquot': ['aliquot',''],
    'Transformed E. coli Aliquot': ['aliquot',''],
    'Tray of Arabidopsis T1 plants': ['tray',''],
    'Tray of Arabidopsis plants': ['tray',''],
    'Tray of N. benthamiana plants': ['tray',''],
    'Tray of T1 Arabidopsis': ['tray',''],
    'Tray of T2 Arabidopsis': ['tray',''],
    'Tray of infiltrated plants': ['tray',''],
    'Tube of Agro mix': ['tube',''],
    'Unverified Hydra Well': ['well',''],
    'Unverified PCR Fragment': ['fragment',''],
    'Unverified Plasmid Stock': ['stock',''],
    'Verified Hydra Well': ['well',''],
    'Working Cryostock': ['stock',''],
    'Yeast 100ml culture': ['culture',''],
    'Yeast 250ml culture': ['culture',''],
    'Yeast 50ml culture': ['culture',''],
    'Yeast 5ml culture': ['culture',''],
    'Yeast Competent Aliquot': ['aliquot',''],
    'Yeast Competent Cell': ['cell',''],
    'Yeast Genome Prep': ['prep',''],
    'Yeast Glycerol Stock': ['stock',''],
    'Yeast Library Glycerol Stock': ['stock',''],
    'Yeast Library Liquid Culture': ['culture',''],
    'Yeast Library Plate': ['plate',''],
    'Yeast Library in Soln 1': ['library',''],
    'Yeast Overnight Suspension': ['suspension',''],
    'Yeast Overnight for Antibiotic Plate': ['plate',''],
    'Yeast Plate': ['plate',''],
    'Zymolyased Yeast Library': ['library',''],
    'gDNA prep': ['prep','']
}

def get_types(o):
    return [ft for ft in o['field_types']]

def get_id(o):
    sample = 'sample'
    container = ''
    if 'object_type' in o and o.get('object_type') is not None:
        (c_ty, c_amt) = map_container_to_cty[str(o.get('object_type').get('name'))]
        c_amt = '@'+c_amt if c_amt != '' else ''
        container = '<' + c_ty + '>'
    if 'sample_type_id' in o and o['sample_type_id'] is not None:
        sample = str(o['sample_type']['name']).replace(' ', '-')
    return sample

def ftids(ft):
    return frozenset(get_id(aft) for aft in ft['allowable_field_types'])

def get_types_in(o):
    return frozenset(ftids(ft) for ft in o['field_types'] if ft['role'] == 'input' and len(ft['allowable_field_types']) > 0)

def get_types_out(o):
    return frozenset(ftids(ft) for ft in o['field_types'] if ft['role'] == 'output' and len(ft['allowable_field_types']) > 0)

def sig(o):
    return (get_types_in(op), get_types_out(op))

def simplify1(xs):
    if type(xs) is list:
        if len(xs) == 0:
            return '( )'
        elif len(xs) == 1:
            return simplify2(xs[0])
        else:
            return ", ".join("("+simplify2(x)+")" for x in xs)
    else:
        return xs

def simplify2(xs):
    if type(xs) is list:
        if len(xs) == 0:
            return ' '
        elif len(xs) == 1:
            return xs[0]
        else:
            return "|".join(str(x) for x in xs)
    else:
        return xs

def show(t):
    (i, o) = t
    return simplify1(list(list(x) for x in i)) + " ==> " + simplify1(list([list(x) for x in o]))

#for op in d:
#    print(get_types(op))    

sig_count = {}

if __name__ == '__main__':
    
    '''
    cs = []
    for op in d:
        for ft in op.get('field_types'):
            for aft in ft.get('allowable_field_types'):
                if 'object_type' in aft and aft['object_type'] is not None and 'name' in aft['object_type']:
                    cs.append(aft.get('object_type').get('name'))
    cs = sorted(list(set(cs)))
    for c in cs:
        print(c)
    '''

    for op in d:
        s = sig(op)
        if s not in sig_count:
            sig_count[s] = 1
        else:
            sig_count[s] += 1

    l = [(c,s) for (s, c) in sig_count.items()]
    l = reversed(sorted(l))
    for (c,s) in l:
        print()
        print(str(c) + "\t" + show(s))
