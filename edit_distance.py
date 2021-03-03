## Implementation of edit distance (Dynamic Programming) (Levenshtein distance)

string1 = input("Enter first word : ")
string2 = input("Enter second word : ")
distance_type = input("Levenshtein (0) or Damerau-Levenshtein (1)? : ")

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
		transposition_cost = float('inf')
		if distance_type == 1 and (i > 1 and j > 1) and (string1[i]==string2[j-1] and string1[i-1]=string2[j]) : transposition_cost = costMatrix[i-2][j-2] + 1
		costMatrix[i][j] = min(substitutionCost, insertionCost, deletionCost, transpositionCost)

print("Levenshtein distance is : ", costMatrix[-1][-1])
