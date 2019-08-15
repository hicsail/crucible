Requirements:
docker-compose
\>python 3.4

### Local Aquarium setup instructions

1) Clone Aquarium
https://github.com/klavinslab/aquarium

2) Remove docker/db folder

3) Place `dump.sql` in /docker/mysql_init/
* in Dropbox->bio-circuit->crucible

4) `docker-compose up --build`

### Terrarium setup instructions

1) Clone Terrarium demo scripts https://github.com/jvrana/TerrariumDemo

2) In the makefile, replace username and password with credentials in aq-login.txt (in Dropbox->bio-circuit->crucible)

3) Create a python virtual environment
`python3 -m venv terrarium-env`

4) Activate environment and install Terrarium (and compatible version of Trident)
```
source terrarium-env/bin/activate
pip install terrarium-capp==0.1.5 pydent==0.1.5a3
```

5) `make example1` or `make example2` (at least one should work)

6) `deactivate` to leave virtual env

### Scripts for pulling data from Aquarium database
1) Make sure you are not in terrarium-env, then pip install pydent (should be pydent-0.0.35)

2) `python get_aq_tables.py`
Creates a JSON file for every Aq model object (plans, wires, samples, etc) - this would be a full data dump similar to its SQL tables. Would take a little bit of work to link the data back together.

Alternatively use `get_plans_model_cache.py` (run in terrarium-env), and creates one JSON file for all plans and its nested objects needed for Terrarium. But I think we already have all this in Dropbox `all_plans_with_wires.json`.

3) remove trailing comma after the last element in array
