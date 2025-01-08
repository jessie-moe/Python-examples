import sys

kilometers = int(sys.argv[1])
time  = int(sys.argv[2])

miles = kilometers /1.6
Kilo2Meters = kilometers * 1000
seconds = time * 3600

KPM = kilometers / time
MPH = miles / time
MPS = Kilo2Meters / seconds

print("The speed in kilometers per hour is: {KPM:.2f}".format(KPM=KPM))
print("The speed in miles per hours is: {MPH:.2f}".format(MPH=MPH))
print("The speed in meters per second is: {MPS:.2f}".format(MPS=MPS))
