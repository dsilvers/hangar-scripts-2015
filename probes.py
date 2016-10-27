from api import api

import random
import sys
from w1thermsensor import W1ThermSensor

class FakeSensor:
    id = "fake"
    value = 0
    def get_temperature(self):
        return random.randint(1000, 3000) / 100.0

if len(sys.argv) > 1:
    all_api_sensors = api("probes")
    sensors = []
    for api_sensor in all_api_sensors:
        print api_sensor
        sensor = FakeSensor()
        sensor.id = api_sensor['serial']
        sensors.append(sensor)
else:
    sensors = W1ThermSensor.get_available_sensors()

for sensor in sensors:
    api_sensor = api("probes", method="get", data={'serial': sensor.id})
    if len(api_sensor) == 1:
        id = api_sensor[0]["id"]
        value = round(sensor.get_temperature(), 2)

        print "===== #{} - {}: {}'C".format(id, sensor.id, value)
        r = api("probedata", method="post", data={
            'probe': id,
            'value': value,
        })
        print r
        print ""
    else:
        print "### API has no probe setup for serial '{}'".format(sensor.id)