Hangar Management Scripts
=================

:License: BSD

Provides temperature reporting and power relay control from the Raspberry Pi
in our hangar.

See hangar repository for the other end of the project. These scripts just do 
the data collection.



Deployment
----------

1. Install python packages required. This will probably just install the
requests package.

`pip install -r requirements.txt`


2. Run `python setup.py` and enter your API endpoint (ex: http://localhost:8000/api),
username and password. This will save the endpoint and authentication token
to `config.py`.


3. Activate crontab. `cp hangar.crontab /etc/crontab.d/hangar.crontab`

