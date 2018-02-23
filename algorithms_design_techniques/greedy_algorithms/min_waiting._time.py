def MinTotalWaitingTime(t, n):
    waitingTime = 0
    treated = []
    for i in range(0, n):
        tMin = 10**5
        minIndex = 0
        for j in range(0, n):
            if treated[j] == 0 and t[j] < tMin:
                tMin = t[j]
                minIndex = j
        waitingTime = waitingTime + (n - i) * tMin
        treated[minIndex] = 1

    return waitingTime

def MinTotalWaitingTime(t, n):
    waitingTime = 0
    for i in len(n):
        waitingTime = waitingTime + (n - i) * t[i]
    return waitingTime