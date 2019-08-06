from pydent import AqSession
from tqdm import tqdm
import json 

prettyprint = lambda x: json.dumps(x, indent=4, sort_keys=True)


def serialize_aq_obj(aq_obj):
    return aq_obj.dump(all_relations=True)


if __name__ == '__main__':
    session = AqSession('danyfu', 'whiteCatsSlouchFar', 'http://0.0.0.0/')

    with open('all_allowable_field_types.json', 'w+') as f:
        f.write('[')
        for aq_obj in tqdm(session.AllowableFieldType.all()):
            f.write(prettyprint(serialize_aq_obj(aq_obj)))
            f.write(',')
        f.write(']')

    with open('all_collections.json', 'w+') as f:
        f.write('[')
        for aq_obj in tqdm(session.Collection.all()):
            f.write(prettyprint(serialize_aq_obj(aq_obj)))
            f.write(',')
        f.write(']')

    with open('all_data_associations.json', 'w+') as f:
        f.write('[')
        for aq_obj in tqdm(session.DataAssociation.all()):
            f.write(prettyprint(serialize_aq_obj(aq_obj)))
            f.write(',')
        f.write(']')

    with open('all_field_types.json', 'w+') as f:
        f.write('[')
        for aq_obj in tqdm(session.FieldType.all()):
            f.write(prettyprint(serialize_aq_obj(aq_obj)))
            f.write(',')
        f.write(']')

    with open('all_field_value.json', 'w+') as f:
        f.write('[')
        for aq_obj in tqdm(session.FieldValue.all()):
            f.write(prettyprint(serialize_aq_obj(aq_obj)))
            f.write(',')
        f.write(']')

    with open('all_items.json', 'w+') as f:
        f.write('[')
        for aq_obj in tqdm(session.Item.all()):
            f.write(prettyprint(serialize_aq_obj(aq_obj)))
            f.write(',')
        f.write(']')

    with open('all_object_types.json', 'w+') as f:
        f.write('[')
        for aq_obj in tqdm(session.ObjectType.all()):
            f.write(prettyprint(serialize_aq_obj(aq_obj)))
            f.write(',')
        f.write(']')

    with open('all_operations.json', 'w+') as f:
        f.write('[')
        for aq_obj in tqdm(session.Operation.all()):
            f.write(prettyprint(serialize_aq_obj(aq_obj)))
            f.write(',')
        f.write(']')

    with open('all_operation_types.json', 'w+') as f:
        f.write('[')
        for aq_obj in tqdm(session.OperationType.all()):
            f.write(prettyprint(serialize_aq_obj(aq_obj)))
            f.write(',')
        f.write(']')
    
    with open('all_parts_association.json', 'w+') as f:
        f.write('[')
        for aq_obj in tqdm(session.PartAssociation.all()):
            f.write(prettyprint(serialize_aq_obj(aq_obj)))
            f.write(',')
        f.write(']')

    with open('all_plans.json', 'w+') as f:
        f.write('[')
        for aq_obj in tqdm(session.Plan.all()):
            f.write(prettyprint(serialize_aq_obj(aq_obj)))
            f.write(',')
        f.write(']')

    with open('all_plan_associations.json', 'w+') as f:
        f.write('[')
        for aq_obj in tqdm(session.PlanAssociation.all()):
            f.write(prettyprint(serialize_aq_obj(aq_obj)))
            f.write(',')
        f.write(']')

    with open('all_samples.json', 'w+') as f:
        f.write('[')
        for aq_obj in tqdm(session.Sample.all()):
            f.write(prettyprint(serialize_aq_obj(aq_obj)))
            f.write(',')
        f.write(']')

    with open('all_sample_types.json', 'w+') as f:
        f.write('[')
        for aq_obj in tqdm(session.SampleType.all()):
            f.write(prettyprint(serialize_aq_obj(aq_obj)))
            f.write(',')
        f.write(']')

    with open('all_users.json', 'w+') as f:
        f.write('[')
        for aq_obj in tqdm(session.User.all()):
            f.write(prettyprint(serialize_aq_obj(aq_obj)))
            f.write(',')
        f.write(']')

    with open('all_wires.json', 'w+') as f:
        f.write('[')
        for aq_obj in tqdm(session.Wire.all()):
            f.write(prettyprint(serialize_aq_obj(aq_obj)))
            f.write(',')
        f.write(']')







