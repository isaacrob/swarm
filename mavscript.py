from droneapi.lib import VehicleMode, Location

print("hello world")
api=local_connect()
v=api.get_vehicles()[0]
print(v.mode.name)

#print("doing second one")
#print(api.get_vehicles())
#v=api.get_vehicles()[1]
