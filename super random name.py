import random

def randomConCombination():
	return random.choice(("th", "ch", "sh", "ph", "st", "ts", "gl", "br", "tr"))
def randomConLetter():
	return random.choice("bcdfghjklmnpqrstvwxyz")
def randomCons():
	return random.choice(("", randomConLetter(), randomConCombination()))
def randomVol():
	return random.choice(("a", "e", "i", "o", "u", "ae", "ai", "ao", "au", "ea", "ee", "ei", "eo", "eu", "ia", "ie", "io", "iu", "oa", "oe", "oi", "oo", "ou", "ua", "ue", "ui", "uo", "y"))
def randomSyllable():
	return randomCons() + randomVol() + randomCons()
def randomName():
	name = ""
	for i in range(int(random.triangular(1, 4, 1))):
		name += randomSyllable()
	return name[0].upper() + name[1:]

while True:
	input(randomName() + " " + randomName())