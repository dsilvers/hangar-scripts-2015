from api import api

import random
import sys
from w1thermsensor import W1ThermSensor

"""
Script has two modes:

Testing mode. Add anything as an argument when running this script to use
random data and existing sensors in the API.
    python probes.py test 

Production mode. Reads any temperature sensors hooked up.
    python probes.py
"""


class FakeSensor:
    """ Fake sensor for testing purposes. Returns a random temperature """
    id = "fake"
    value = 0
    def get_temperature(self):
        return random.randint(1000, 3000) / 100.0

if len(sys.argv) > 1:
    """ Testing mode. Grab all sensors from the API and use those """
    all_api_sensors = api("probes")
    sensors = []
    for api_sensor in all_api_sensors:
        print api_sensor
        sensor = FakeSensor()
        sensor.id = api_sensor['serial']
        sensors.append(sensor)
else:
    """ Production mode. Use all sensors detected by W1ThermSensor. """
    sensors = W1ThermSensor.get_available_sensors()


for sensor in sensors:
    """ Actually send the data to the API. """
    api_sensor = api("probes", method="get", data={'serial': sensor.id})
    if len(api_sensor) == 1:
        id = api_sensor[0]["id"]
        value = round(sensor.get_temperature(), 2)

        print "===== #{} - {}: {}'C".format(id, sensor.id, value)
        print api("probedata", method="post", data={
            'probe': id,
            'value': value,
        })
        print ""
    else:
        print "### API has no probe setup for serial '{}'".format(sensor.id)
        print ""