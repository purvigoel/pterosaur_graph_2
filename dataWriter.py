#!usr/bin/python
import csv
f = open("data.csv", "w")
writer = csv.writer(f)
writer.writerow(["x","y","z","t"])
steps = 25;
axisMax = 314;
tMax = 31;
axisStep = axisMax / steps;

def inRange(x, mmin, mmax):
	if(x <= mmax and x >= mmin):
		return True
	return False

for t in range(0, 3):
	for x in range(0, axisMax, axisStep):
		for y in range(0, axisMax, axisStep):
			xDat = x
			yDat= y
			value = 15
			tDat = t
			write = str(xDat)+","+str(yDat)+","+str(value)+","+str(t) +"\n"
			writer.writerow([xDat,yDat,value,t])
for t in range(3,8):
	for x in range(0, axisMax, axisStep):
		for y in range(0, axisMax, axisStep):
			if inRange(x, 25, 50) and inRange(y, 25, 50):
				xDat = x
				yDat = y
				value = 15-t
				tDat = t
				write = str(xDat)+","+str(yDat)+","+str(value)+","+str(t)+"\n"
				writer.writerow([xDat,yDat,value,t])
			else:	
				xDat = x
				yDat= y
				value = 15
				tDat = t
				write = str(xDat)+","+str(yDat)+","+str(value)+","+str(t)+"\n"
				writer.writerow([xDat,yDat,value,t])
