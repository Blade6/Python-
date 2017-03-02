f = open('score.txt','r')

score = []
credit = []

while True:
	line = f.readline()
	if not line:
		break
	Line = line.split()
	score.append(float(Line[0]))
	credit.append(float(Line[1]))

credits = sum(credit)

def s2c(number):
	if number >= 90:
		return 4.0
	elif number >= 85:
		return 3.7
	elif number >= 82:
		return 3.3
	elif number >= 78:
		return 3.0
	elif number >= 75:
		return 2.7
	elif number >= 71:
		return 2.3
	elif number >= 66:
		return 2.0
	elif number >= 62:
		return 1.7
	elif number > 60:
		return 1.3
	elif number == 60:
		return 1.0
	else:
		return 0

total = 0
for i,item in enumerate(score):
	total += s2c(item) * credit[i]

result = total/credits
print result