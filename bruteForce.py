import time
from utils import loss, makeRandomSolution, showResults
import sys
def bruteForce(nums, maxIteration):
    currentSolution = []
    for i in range(maxIteration):
        currentSolution = makeRandomSolution(len(nums))
        if loss(currentSolution, nums) == 0:
            return currentSolution, i
    return currentSolution, maxIteration

def main(numbers, iterationAmount):
    numsLen = len(numbers)
    if (numsLen % 3 != 0):
        raise ValueError("Ilość podanych liczb nie jest podzielna przez trzy!")
    if (sum(numbers) % (numsLen // 3) != 0):
        raise ValueError("Suma liczb nie podzielna przez liczbę grup!")

    timeBefore = time.time()
    result = bruteForce(numbers, iterationAmount)
    timeAfter = time.time() - timeBefore

    showResults(numbers, result, timeAfter)

if __name__ == "__main__":
    numbers = [int(arg) for arg in sys.argv[2:]]
    main(numbers, int(sys.argv[1]))


