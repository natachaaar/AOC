import numpy as np 

# Using readlines()
file1 = open('input.txt', 'r')
Lines = file1.readlines()
count = 0
sum = 0
sum_list =[]
# Strips the newline character
for line in Lines:
	count += 1
	if line.strip() != "":
		sum = sum + int(line.strip())
	else:
		sum_list.append(sum)
		#print(sum)
		sum = 0
	#print("Line{}: {}".format(count, line.strip()))
#Handle if last line is not empty
sum_list.append(sum)
#print(np.sort(sum_list)[::-1])
print(max(sum_list))

print(np.sort(sum_list)[::-1][0]+np.sort(sum_list)[::-1][1]+np.sort(sum_list)[::-1][2])

