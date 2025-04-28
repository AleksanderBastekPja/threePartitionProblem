import random
import time
import math

def sumSubset(randomSolutions, nums):
    acc = [0, 0, 0]
    for index, subsetId in enumerate(randomSolutions):
        acc[subsetId] += nums[index]
    return acc

def loss(randomSolution, nums):
    sub1, sub2, sub3 = sumSubset(randomSolution, nums)
    return abs(sub1 - sub2) + abs(sub2 - sub3)

def makeRandomSolution(n):
    return [random.randint(0, 2) for _ in range(n)]

def generateNeighbour(randomSolution):
    difference = [random.randint(-1, 1) for _ in range(len(randomSolution))]
    randomSolutionCopy = randomSolution.copy()
    for i in range(len(randomSolution)):
        randomSolutionCopy[i] = (randomSolutionCopy[i] + difference[i]) % 3
    return randomSolutionCopy

def simulatedAnnealing(nums, K):
    s = makeRandomSolution(len(nums))
    V = [s]
    for k in range(1,K):
        t = generateNeighbour(s)
        if loss(t, nums) <= loss(s, nums):
            s = t
        else:
            if random.random() < math.exp(-abs(loss(s, nums)-loss(t, nums))/T(k)):
                s = t
        V.append(s)

    minelement = V[0]
    for e in V:
        if loss(e, nums) < loss(minelement, nums):
            minelement = e

    return minelement, V, [loss(e, nums) for e in V]

def T(i):
    return 100.0/i

def main(numbers):
    timeBefore = time.time()
    result = simulatedAnnealing(numbers, 10000)

    print(sumSubset(result[0], numbers))
    print(time.time() - timeBefore)

if __name__ == "__main__":
    main([1, 9, 5, 5, 3, 7,4,3,5,7,2,1,3,6,9,4,4])
