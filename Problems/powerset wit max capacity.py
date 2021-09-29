from itertools import combinations

def findMaxSum(weights,maxCapacity):
    powerset_list = []
    weights_sum = []
    weights_sum_less_or_equal_maxCapacity = []
    weights_count = len(weights)
    weights = set(weights)
    print("Set: ",weights)
    for i in range(weights_count+1):
        for element in combinations(weights,i):
            powerset_list.append(element)
            weightsSum = sum(element)
            weights_sum.append(weightsSum)
            if weightsSum<=maxCapacity:
                weights_sum_less_or_equal_maxCapacity.append(weightsSum)
    print(powerset_list)
    print(weights_sum)
    print(max(weights_sum_less_or_equal_maxCapacity))

weights = [1,3,5]
print("List: ",weights)
maxCapacity = 7
findMaxSum(weights,maxCapacity)