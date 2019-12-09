vET = ["docet", "ridet"]
endings = ["o", "s", "t"]
input = "docet"
if input in vET:
	for i in range(1, 4, 1):
		print(input[0:-2] + endings[i])