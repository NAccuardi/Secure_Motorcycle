from sense_hat import SenseHat
import time
sense = SenseHat()
import sys
import gpsd
gpsd.connect()



def get_position():
	packet = gpsd.get_current()

	return packet.position()
def print_accelerations():
	
	while True:
		acceleration = sense.get_accelerometer_raw()
		x = acceleration['x']
		y = acceleration['y']
		z = acceleration['z']
		if x > y and x > z:
			sense.show_letter("X")

		if z > y and z > y:
			sense.show_letter("Z")

		else:
			sense.show_letter("Y")	
		x = round(x, 2)
		y = round(y, 2)
		z = round(z, 2)
		time.sleep(.75)	
		print("x={0}, y={1}, z = {2}".format(x, y, z))
print(get_position())	
