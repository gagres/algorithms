BestItem(values, weights):
    maxValuePerWeight = 0
    bestItem = 0
    for i in range(0, n):
        if weights[i] > 0:
            if (values[i] / weights[i]) > maxValuePerWeight:
                maxValuePerWeight = (values[i] / weights[i])
                bestItem = i
    return bestItem

Knapsack(W, values, weights):
    amounts = []
    totalValue = 0
    for i in len(values):
        amounts[i] = amounts[i] if amounts[i] else 0
        if W = 0
            return (totalValue, amounts)
        bestItem = BestItem(values, weights)
        a = min(weights[i], W)
        totalValue = totalValue = a * (values[i] / weights[i])
        weights[i] = weights[i] - a
        amounts[i] = amounts[i] + a
        W = W - a
    return (totalValue, amounts)


Knapsack(W, values, weights):
    amounts = []
    totalValue = 0
    for i in len(values):
        amounts[i] = amounts[i] if amounts[i] else 0
        if W = 0
            return (totalValue, amounts)
        a = min(weights[i], W)
        totalValue = totalValue = a * (values[i] / weights[i])
        weights[i] = weights[i] - a
        amounts[i] = amounts[i] + a
        W = W - a
    return (totalValue, amounts)