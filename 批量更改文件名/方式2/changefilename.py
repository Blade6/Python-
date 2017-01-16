from sys import argv

script, filename = argv

target = open(filename,'w')

for x in range(726):
	if x == 0:
		continue
	else:
		if x < 10:
			line = "ren 000%d.jpg img0000%d.jpg" % (x, x)
		elif x < 100:
			line = "ren 00%d.jpg img000%d.jpg" % (x, x)
		else:
			line = "ren 0%d.jpg img00%d.jpg" % (x, x)
		target.write(line)
		target.write("\n")

target.close()