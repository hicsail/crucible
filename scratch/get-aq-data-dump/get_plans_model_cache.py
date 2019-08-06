import pydent
import json
from tqdm import tqdm

prettyprint = lambda x: json.dumps(x, indent=4)

if __name__ == '__main__':

    session = pydent.login('danyfu', 'http://0.0.0.0')

    # make sure cache is turned off
    with session(using_cache=False, timeout=60) as no_cache_sess:
        last_plan = no_cache_sess.Plan.one()
        plans = []
        step_size = 500
        step_iter = list(range(0, last_plan.id, step_size))
        for i in tqdm(step_iter):
            #print(i)
            plans += no_cache_sess.Plan.last(step_size, opts={'offset': i})
        plans = list({p.id: p for p in plans}.values())

    cache_sess = session.with_cache(timeout=600)
    # how you would update a model cache for a different spawned session
    cache_sess.browser.update_cache(plans)

    # get all Plans from the cache, and request dependents "operations" and its "field_values" dependents
    sess.browser.get("Plan", {"operations": {"field_values"}})

    # and so on..
    sess.browser.get("Wire", {"source", "destination"})
    sess.browser.get("FieldValue", {"allowable_field_type": "field_type"})
    sess.browser.get("Operation", "operation_type")
        
    sess.browser.model_cache

    with open('all_plans_with_children.json', 'w+') as f:
        f.write('[')
        for plan_id, plan_obj in tqdm(sess.browser.model_cache['Plan'].items()):
            f.write(prettyprint(plan_obj._get_data()))
            f.write(',')
        f.write(']')

