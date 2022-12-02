"""Rock defeats/BAT Scissors, Scissors defeats Paper, and Paper defeats Rock.

Opponent=
A for Rock, B for Paper, and C for Scissors.

Me = 
X for Rock, Y for Paper, and Z for Scissors.

Scores 
1 for Rock, 2 for Paper, and 3 for Scissors + (0 if you lost, 3 if the round was a draw, and 6 if you won).

 X means lose, Y means draw, and Z means  win !"
"""

"""
#First exercice
file1 = open('input2.txt', 'r')
Lines = file1.readlines()
count = 0
sum = 0
sum_list =[]
total_scores= 0
0# Strips the newline character
for line in Lines:
	scores = 0
	P1 = line.split(" ")[0]
	P2 = line.split(" ")[1].rstrip()
	if P1 == "A":
		P1 = "R"
	elif P1 == "B":
		P1 = "P"
	elif P1 == "C":
		P1 = "S"
	else:
		print("pb")
		exit(0)
	if P2 == "X":
		scores = 1
		P2 = "R"
	elif P2 == "Y":
		scores = 2
		P2 = "P"
	elif P2 == "Z":
		scores = 3
		P2 = "S"
	else:
		print("pb")
		exit(0)


	if P1 == P2:
		print("Draw")
		scores = scores + 3
	elif (P2 == "R" and P1 == "S") or (P2 == "S" and P1 == "P") or (P2 == "P" and P1 == "R"):
		scores = scores + 6

	print(P1+" "+P2)
	print(scores)
	total_scores = scores +total_scores

print(total_scores)"""

#Second exercice
"""Scores 
1 for Rock, 2 for Paper, and 3 for Scissors + (0 if you lost, 3 if the round was a draw, and 6 if you won).
 X means lose, Y means draw, and Z means  win !"""
#Rock defeats/BAT Scissors, Scissors defeats Paper, and Paper defeats Rock
file1 = open('input2.txt', 'r')
Lines = file1.readlines()
count = 0
sum = 0
sum_list =[]
total_scores= 0
0# Strips the newline character
for line in Lines:
	scores = 0
	P1 = line.split(" ")[0]
	P2 = line.split(" ")[1].rstrip()
	if P1 == "A":
		P1 = "R"
	elif P1 == "B":
		P1 = "P"
	elif P1 == "C":
		P1 = "S"
	else:
		print("pb")
		exit(0)
	if P2 == "X":
		if P1 == "R":
			P2 = "S"
		elif P1 == "S":
			P2 = "P"
		elif P1 == "P":
			P2 = "R"
		scores = 0
	elif P2 == "Y":
		scores = 3
		P2 = P1
	elif P2 == "Z":
		scores = 6
		if P1 == "R":
			P2 = "P"
		elif P1 == "S":
			P2 = "R"
		elif P1 == "P":
			P2 = "S"
	else:
		print("pb")
		exit(0)

	if P2 == "R":
		scores = 1 +scores 
	elif P2 == "S":
		scores = 3+scores 
	elif P2 == "P":
		scores = 2+scores 

	print(P1+" "+P2)
	print(scores)
	total_scores = scores +total_scores

print(total_scores)

