import sys

def BestItem(values, weights):
    '''
    BestItem(values, weights): calculate what is the biggest number founded by divide each value by your respective weight
    Returns: The value founded
    '''
    maxValuePerWeight = 0
    bestItem = 0
    for i in range(0, len(values)):
        if weights[i] > 0:
            division = values[i] / weights[i]
            if division > maxValuePerWeight:
                maxValuePerWeight = values[i] / weights[i]
                bestItem = i
    return bestItem

def KnapsackNaive(W, values, weights):
    '''
    KnapsackNaive(maximum_weights, values of weight, weights)
    Returns: Total value acquired
    '''
    amounts = []
    totalValue = 0

    values = map(float, values) # Need be float
    weights = map(float, weights) # Need be float

    for i in range(0, len(values)):
        if W == 0:
            return (totalValue, amounts)
        bestItem = BestItem(values, weights)
        a = min(weights[bestItem], W)
        totalValue = totalValue + (a * (values[bestItem] / weights[bestItem]))
        weights[bestItem] = weights[bestItem] - a
        amounts.append(a)
        W = W - a
    return (totalValue, amounts)

def KnapsackFast(W, values, weights):
    amounts = []
    totalValue = 0
    for i in len(values):
        amounts[i] = amounts[i] if amounts[i] else 0
        if W == 0:
            return (totalValue, amounts)
        a = min(weights[i], W)
        totalValue = totalValue = a * (values[i] / weights[i])
        weights[i] = weights[i] - a
        amounts[i] = amounts[i] + a
        W = W - a
    return (round(totalValue, 4), amounts)

lines = sys.stdin.read().split('\n')

values = []
weights = []
[n, W] = lines[0].split(' ')
del lines[0]

for i in range(0, int(n)):
    line = map(int, lines[i].split(' '))
    values.append(line[0])
    weights.append(line[1])

print(KnapsackNaive(int(W), values, weights))