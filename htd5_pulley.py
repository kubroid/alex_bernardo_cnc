from math import *

feed = 300
Q = 2
pitch = 5 # htd5
N = 44 # zub'ev
deep = -15 # tolsina
PD = N*pitch/pi
OD = PD - 1.14
cx = 0 # coord of center
cy = 0
cycle = 'G83 x%.3f y%.3f q%.2f r1 z%.3f'
toolD = 6
zPerTurn = 1

#print "PD:%f OD:%f sin(90):%f" % (PD, OD, sin(pi))

print "G21 F%.2f" % feed
print "G64 P0.01"
#print "G0 X0 Y0 Z0"

for i in range(N):
	x = cx + sin(2*pi/N*i)*PD/2
	y = cy + cos(2*pi/N*i)*PD/2
	print cycle % (x, y, Q, deep)

tD = toolD + .2
print "G0 X%.3f Y%.3f Z1" % (0, (OD + tD)/2)
z = 1
while z > deep:
	z -= zPerTurn
	if z < deep :
		z = deep;
	print "G2 X%.3f Y%.3f Z%.2f I0 J%.3f P1" % (0, (OD + tD)/2, z, -(OD + tD)/2)

#final cut
tD = toolD
print "G1 X%.3f Y%.3f" % (0, (OD + tD)/2)
print "G2 X%.3f Y%.3f Z%.2f I0 J%.3f P1" % (0, (OD + tD)/2, z, -(OD + tD)/2)
print "G0 z20"
print "M2"
