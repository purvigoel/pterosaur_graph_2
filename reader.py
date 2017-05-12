#!usr/bin/python
import csv
f = open("birds.csv", "r")
f2 = open("anage_data.txt", "r")
f3 = open("weight.csv", "w")
data = [row for row in f.read().splitlines()]
data2 = [row for row in f2.read().splitlines()]
bird = []
animalToType = {}
for dat in data:
	datS = dat.split(",")
	if(len(dat.split(",")) == 14):
		bird.append(datS[0].lower())
		animalToType[datS[0].lower()] = (datS[12], datS[3])


writer = csv.writer(f3)
writer.writerow(["Species","weight","type","MC"])
for line in data2:
	dat2 = line.split("\t")
	if len(dat2) > 18:
		weight = dat2[18]
	else:
		continue
	animal = dat2[6].lower() + " " + dat2[7].lower()
	if animal in bird:
		writer.writerow([animal,weight, animalToType[animal][0],animalToType[animal][1]])
writer.writerow(["peteinosaurs zambelli",100,"dino",185])
writer.writerow(["Dimorphodon macronyx",907,"dino",400])
writer.writerow(["Rhamphorhynchus gemmingi",1500,"dino",443])
writer.writerow(["Rhamphorhynchus longiceps",1500,"dino",429])
writer.writerow(["Rhamphorhynchus intermedius",2267,"dino",178])
writer.writerow(["Gallodactylus suevicus", 1250, "dino", 527])
writer.writerow(["Pterodactylus elegans",60,"dino",81])
writer.writerow(["Pterodactylus kochi",450,"dino",164])
writer.writerow(["Scaphognathus purdoni",1500,"dino",458])
writer.writerow(["Pteranodon species",20000,"dino",1638])


print(len(bird))
f.close()
f2.close()
f3.close()