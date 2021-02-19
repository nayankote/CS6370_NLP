## Implementation of edit distance (Dynamic Programming) (Levenshtein distance)

string1 = input("Enter first word : ")
string2 = input("Enter second word : ")

l1, l2 = len(string1), len(string2)
string1, string2 = " "+string1, " "+string2

costMatrix = [[0]*(l2+1) for j in range(l1+1)]

for i in range(1,l1+1):
	costMatrix[i][0] = i
for j in range(1,l2+1):
	costMatrix[0][j] = j

for i in range(1,l1+1) :
	for j in range(1,l2+1):
		substitutionCost = costMatrix[i-1][j-1] + 1 * (string1[i] != string2[j])
		insertionCost = costMatrix[i][j-1] + 1
		deletionCost = costMatrix[i-1][j] + 1
		costMatrix[i][j] = min(substitutionCost, insertionCost, deletionCost)

print("Levenshtein distance is : ", costMatrix[-1][-1])
