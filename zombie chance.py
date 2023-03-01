import random

master_list_of_first_names = []
with open(r"C:\Users\Joel\programming class\first names.csv", 'r') as opened_file:
	for line in opened_file:
		split_line = line.split(',')
		master_list_of_first_names.append(split_line[1])
		master_list_of_first_names.append(split_line[4])
master_list_of_last_names = []
with open(r"C:\Users\Joel\programming class\last names.csv", 'r') as opened_file:
	for line in opened_file:
		split_line = line.split(',')
		master_list_of_last_names.append(split_line[1])
		
def randomName():
	return random.choice(master_list_of_first_names) + " " + random.choice(master_list_of_last_names)
	
def findZombie():
	found = set()
	while True:
		next = randomName()
		if next in found:
			return len(found)
		found.add(next)

def inDataRange(data, min, max):
	total = 0
	for i in range(min, max):
		if i in data:
			total += data[i]
	return total

def getDist(data, steps):
	out = []
	s = len(data)
	for i in range(steps):
		out.append( ( i*(s//steps), (i+1)*(s//steps), inDataRange( data, i*(s//steps), (i+1)*(s//steps) ) ) )
	return out

def printChart(dist, height):
	peak = 0
	for i in dist:
		if i[2] > peak:
			peak = i[2]
	size_per_chunk = peak/height
	chunks_array = []
	for i in dist:
		chunks_array.append(i[2]/size_per_chunk)
	for drop in range(height):
		needed_chunks = height - drop
		for i in chunks_array:
			if i >=needed_chunks:
				print("#", end="")
			else:
				print(" ", end="")
		print()

results = {}
for i in range(10000):
	if i%1000==0:
		print(i)
	n = findZombie()
	if n not in results:
		results[n] = 1
	else:
		results[n] += 1
		
printChart(getDist(results, 100), 23)
print(min(results), max(results), sep="-")