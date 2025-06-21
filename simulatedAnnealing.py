import random
import time
import math
from utils import loss, makeRandomSolution, showResults
import sys

def generateNeighbour(randomSolution):
    randomSolutionCopy = randomSolution.copy()
    random.shuffle(randomSolutionCopy)
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

    return minelement, len(V)

def T(i):
    return 100.0/i

def main(numbers, iterationNumber):
    timeBefore = time.time()
    result = simulatedAnnealing(numbers, iterationNumber)
    timeAfter = time.time() - timeBefore
    showResults(numbers, result, timeAfter)

if __name__ == "__main__":
    numbers = [int(arg) for arg in sys.argv[2:]]
    main(numbers, int(sys.argv[1]))
