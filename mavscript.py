#based in part off https://github.com/dronekit/dronekit-python/blob/master/examples/simple_goto/simple_goto.py

from droneapi.lib import VehicleMode, Location
import time


print("hello world")
api=local_connect()
v=api.get_vehicles()[0]
#print(v.mode.name)

def init(alt):
	print("checking stuff")
	if vehicle.mode.name=="INITIALISING":
		print("waiting for init")
		time.sleep(2)
	while vehicle.gps_0.fix_type<2:
		print("getting gps: "+str(vehicle.gps_0.fix_type))
		time.sleep(1)

	print("located at: "+str(vehicle.location))
	print("arming motors")
	vehicle.mode=VehicleMode("GUIDED")
	vehicle.armed=True
	vehicle.flush()

	while not vehicle.armed and not api.exit:
		print("waiting for arm")
		time.sleep(1)

	print("taking off")
	vehicle.commands.takeoff(alt)
	vehicle.flush()
	
	while not api.exit:
		print("altitude: "+str(vehicle.location.alt))
		if vehicle.location.alt>=alt*.95:
			print("reached alt")
			break
		time.sleep(1)

def goplace(lat,long,alt):
	point=Location(lat,long,alt,is_relative=True)
	vehicle.commands.goto(point)
	vehicle.flush()
