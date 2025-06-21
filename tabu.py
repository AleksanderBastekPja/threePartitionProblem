import time
from utils import loss, makeRandomSolution, generateNeighbours, showResults
import sys

def tabu(nums, maxIteration, tabu_size = 100):
    current = makeRandomSolution(len(nums))
    global_best = [current.copy()]
    tabu_list = [current.copy()]

    for i in range(maxIteration):
        neighbours = [ n for n in generateNeighbours(current) if n not in tabu_list ]
        if len(neighbours) == 0: break
        bestSolution = neighbours[0]

        for neighbour in neighbours[1:]:
            if loss(neighbour, nums) < loss(bestSolution, nums):
                bestSolution = neighbour

        current = bestSolution
        tabu_list.append(bestSolution)
        if len(tabu_list) > tabu_size:
            tabu_list = tabu_list[-tabu_size:]
        if loss(current, nums) < loss(global_best[-1], nums):
            global_best.append(current)
        if loss(current, nums) == 0:
            return current, i
    return current, maxIteration


def main(numbers, iterationNumber):
    timeBefore = time.time()
    result = tabu(numbers, iterationNumber)
    timeAfter = time.time() - timeBefore
    showResults(numbers, result, timeAfter)

if __name__ == "__main__":
    numbers = [int(arg) for arg in sys.argv[2:]]
    main(numbers, int(sys.argv[1]))
