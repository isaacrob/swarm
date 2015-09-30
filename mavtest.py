from droneapi.lib import VehicleMode, Location
import time

print("hello world")
api=local_connect()
v=api.get_vehicles()[0]
print(v.mode)
print("THIS MESSAGE MEANS THE SCRIPT GOT PAST CONNECTING PHASE")
