#!/usr/bin/env python
from subprocess import Popen
import time

#next line is atrocious. get rid of it
Popen('mavproxy.py --master 10.0.1.3:14550 --quadcopter --load-module=droneapi.module.api --cmd="api start /home/pi/swarm/mavtest.py"',shell=True)

print("successfully called thingy")

time.sleep(1000)
