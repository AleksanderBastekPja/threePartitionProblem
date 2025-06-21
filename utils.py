import random

def sumSubset(randomSolutions, nums):
    acc = [0] * (len(nums) // 3)
    for index, subsetId in enumerate(randomSolutions):
        acc[subsetId] += nums[index]
    return acc

def loss(randomSolution, nums):
    subsets = sumSubset(randomSolution, nums)
    return sum([abs(subsets[i] - subsets[i+1]) for i in range(len(subsets) - 1)])

def makeRandomSolution(numbersLength):
    randomSolution = [rs for rs in range(numbersLength // 3)] * 3
    random.shuffle(randomSolution)
    return randomSolution

def generateNeighbours(randomSolution):
    n = len(randomSolution)
    neighbors = []
    for i in range(n):
        for j in range(i+1, n):
            if randomSolution[i] != randomSolution[j]:
                nb = randomSolution.copy()
                nb[i], nb[j] = nb[j], nb[i]
                neighbors.append(nb)
    return neighbors

def generateNeighbours(randomSolution):
    n = len(randomSolution)
    neighbors = []
    for i in range(n):
        for j in range(i+1, n):
            if randomSolution[i] != randomSolution[j]:
                nb = randomSolution.copy()
                nb[i], nb[j] = nb[j], nb[i]
                neighbors.append(nb)
    return neighbors

def showResults(numbers, result, timeAfter):
    print("Rezultaty")
    print("liczba iteracji: ", result[1])
    belongingNumber = result[0]
    zbiory = {}
    for zbior, liczba in zip(belongingNumber, numbers):
        if zbior not in zbiory:
            zbiory[zbior] = []
        zbiory[zbior].append(liczba)
    for zbior in sorted(zbiory.keys()):
        print(f"Zbiór {zbior}: {zbiory[zbior]}")
    print("Sumy zbiorów: ", sumSubset(result[0], numbers))
    print("Czas wykonania", timeAfter, "s")
