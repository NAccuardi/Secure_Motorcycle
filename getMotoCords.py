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
                                        os.system("sudo echo %s | mail -s 'Coordinates of Motorcycle' EMAILTOSENDMSGTO" %print_str)
                                        print('Cords Sent.')
                                        return
                except KeyError:
                        pass
                except KeyboardInterrupt:
                        quit()
                except StopIteration:
                        session = None
                        print "GPSD has terminated"
get_position()
