#we have a list of superheroes representing teh justice league justice_league=["superman","batman","wonder women","flash","aquaman","green lantern"]
#ques 1- calculate teh number of meamber in list
justice_league=["Superman","Batman","Wonder Woman","Flash","Aquaman","Green Lantern"]
print(len(justice_league))

#2. batman recruited batgirl and nightwing as new member add them to your list
justice_league=["Superman","Batman","Wonder Woman","Flash","Aquaman","Green Lantern"]
justice_league.append("Batgirl")
justice_league.append("Nightwing")
print(justice_league)

#3. wonder women is now the leader of justivce league move her to the begining of the list
justice_league=["Superman","Batman","Wonder Woman","Flash","Aquaman","Green Lantern"]
justice_league.remove("Wonder Woman")
justice_league.insert(0 ,"Wonder Woman")
print(justice_league)

#4. aquaman and flash are having conflict and wee need to separate them .choose either "green lantren or "superman and move them in between aquaman and flash
justice_league=["Superman","Batman","Wonder Woman","Flash","Aquaman","Green Lantern"]
justice_league.remove("Superman")

index = justice_league.index("Flash")
justice_league.insert(index, "Superman")

print(justice_league)
#5. the justice league faced a crisis and superman decideed to assemble   a new team .replace existing list with the following new meambers:"Cyborg","Shazam","Hawkgirl","Matrian","Manhunter","Green Arrow"
justice_league=["Superman","Batman","Wonder Woman","Flash","Aquaman","Green Lantern"]
justice_league=["Cyborg","Shazam","Hawkgirl","Matrian Manhunter","Green Arrow"]
print(justice_league)

#6. sort the justice league alphabetically . the hero at oth index will become new leader
justice_league.sort()
print(justice_league)

leader=justice_league[0]
print("leader is: ",leader)