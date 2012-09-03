from math import *

pitch = 5 # htd5
PLD = 0.5715 # pitch diameter - outer diameter
drillD = 1.56*2
teethH = 2.06

N = 14 # zub'ev
deep = -9 # tolsina

feed = 200
Q = 2
PD = N*pitch/pi
OD = PD - PLD*2
DD = OD - teethH*2 + drillD

cx = 0 # coord of center
cy = 0
cycle = 'G83 x%.3f y%.3f q%.2f r1 z%.3f'
toolD = 6
zPerTurn = 7

#print("PD:%f OD:%f sin(90):%f" % (PD, OD, sin(pi))

print("G21 F%.2f" % feed)
print("G64 P0.01")
print("m6t1")
print("o<auto-tool-change> call")

print("G21 F%.2f" % (feed))

for i in range(N):
	x = cx + sin(2*pi/N*i)*PD/2
	y = cy + cos(2*pi/N*i)*PD/2
	print(cycle % (x, y, Q, deep))

print("m6t2")
print("o<auto-tool-change> call")
print("G21 F%.2f" % feed)

tD = toolD + .2
print("G0 X%.3f Y%.3f Z1" % (0, (OD + tD)/2))
z = 1
while z > deep:
	z -= zPerTurn
	if z < deep :
		z = deep;
	print("G2 X%.3f Y%.3f Z%.2f I0 J%.3f P1" % (0, (OD + tD)/2, z, -(OD + tD)/2))

#final cut
tD = toolD
print("G1 X%.3f Y%.3f" % (0, (OD + tD)/2))
print("G2 X%.3f Y%.3f Z%.2f I0 J%.3f P1" % (0, (OD + tD)/2, z, -(OD + tD)/2))
print("g53 G0 z0")
print("M2")
