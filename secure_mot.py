from sense_hat import SenseHat
import time
sense = SenseHat()
import sys
import gps
import os




def get_position():
        # Listen on port 2947 (gpsd) of localhost
        session = gps.gps("localhost", "2947")
        session.stream(gps.WATCH_ENABLE | gps.WATCH_NEWSTYLE)

        while True:
                try:
                        report = session.next()
                                # Wait for a 'TPV' report and display the current time
                                # To see all report data, uncomment the line below
                                # print report
                        
                        if report['class'] == 'TPV':
                                if hasattr(report, 'lat') and hasattr(report, 'lon'):
                                        print_str = 'lat = ' + str(report.lat) + ' lon = ' + str(report.lon)
                                        #os.system("sudo echo" + 'lat = ' + report.lat + 'lon =' + report.lon | mail -s 'coordinates' naccuardi@gmail.com")
                                        os.system("sudo echo %s | mail -s 'Motorcycle has been knocked over.' EMAILTOSENDMSGTO" %print_str)
                                        print('Cords Sent.')
                                        return
                except KeyError:
                        pass
                except KeyboardInterrupt:
                        quit()
                except StopIteration:
                        session = None
                        print "GPSD has terminated"

def print_accelerations():
	
	while True:
                try:
                        acceleration = sense.get_accelerometer_raw()
                        x = acceleration['x']
                        y = acceleration['y']
                        z = acceleration['z']
                        x = round(x, 2)
                        y = round(y, 2)
                        z = round(z, 2)
                        time.sleep(1)	
                        if y > .8 or y < -.8:
                                print "finding lat/lon"
                                get_position()
                                quit()
                except KeyboardInterrupt:
                        sense.show_letter(" ")
                        quit()
                        
                        
                        
print_accelerations()
