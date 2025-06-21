import time
from utils import loss, makeRandomSolution, generateNeighbours, showResults
import sys
from random import randint

def hillClimbingStochastic(nums, maxIteration):
    current = makeRandomSolution(len(nums))
    for i in range(maxIteration):
        neighbours = generateNeighbours(current)
        neighbour = neighbours[randint(0,len(neighbours)-1)]

        if loss(neighbour, nums) <= loss(current, nums):
            current = neighbour
        if loss(current, nums) == 0:
            return current,i
    return current, maxIteration


def main(numbers, iterationAmount):
    numsLen = len(numbers)
    if (numsLen % 3 != 0):
        raise ValueError("Ilość podanych liczb nie jest podzielna przez trzy!")
    if (sum(numbers) % (numsLen // 3) != 0):
        raise ValueError("Suma liczb nie podzielna przez liczbę grup!")

    timeBefore = time.time()
    result = hillClimbingStochastic(numbers, iterationAmount)
    timeAfter = time.time() - timeBefore

    showResults(numbers, result, timeAfter)

if __name__ == "__main__":
    numbers = [int(arg) for arg in sys.argv[2:]]
    main(numbers, int(sys.argv[1]))
