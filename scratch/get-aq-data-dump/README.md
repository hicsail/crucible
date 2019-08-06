Requirements:
docker-compose
\>python 3.4


1) clone Aquarium
https://github.com/klavinslab/aquarium

2) Remove docker/db folder

3) place `dump.sql` in /docker/mysql_init/

4) `docker-compose up --build`

5) `pip3 install pydent`

6) `python get_aq_tables.py`
Creates a JSON file for every Aq model object (plans, wires, samples, etc) - this would be a full data dump similar to its SQL tables. Would take a little bit of work to link the data back together.

Alternatively use `get_plans_model_cache.py` - allegedly faster, need to use `pydent==0.1.5a3`, and creates one JSON file for all plans and its nested objects needed for Terrarium. But I think we already have all this in Dropbox `all_plans_with_wires.json`.

7) remove trailing comma after the last element in array
