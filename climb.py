from random import randint
import time

def sumSubset(randomSolutions, nums):
    acc = [0, 0, 0]
    for index, subsetId in enumerate(randomSolutions):
        acc[subsetId] += nums[index]
    return acc


def loss(randomSolution, nums):
    sub1, sub2, sub3 = sumSubset(randomSolution, nums)
    return abs(sub1 - sub2) + abs(sub2 - sub3)


def makeRandomSolution(n):
    return [randint(0, 2) for _ in range(n)]


def generateNeighbours(randomSolution):
    neighbours = []
    for i in range(len(randomSolution)):
        randomSolutionCopy = randomSolution.copy()
        randomSolutionCopy[i] = (randomSolutionCopy[i] + 1) % 3
        neighbours.append(randomSolutionCopy)

    for i in range(len(randomSolution)):
        randomSolutionCopy = randomSolution.copy()
        randomSolutionCopy[i] = (randomSolutionCopy[i] - 1) % 3
        neighbours.append(randomSolutionCopy)

    return neighbours


def hillClimbing(nums, maxIteration):
    current = makeRandomSolution(len(nums))

    for i in range(maxIteration):
        neighbours = generateNeighbours(current)
        bestSolution = neighbours[0]

        for neighbour in neighbours[1:]:
            if loss(neighbour, nums) < loss(bestSolution, nums):
                bestSolution = neighbour

        if (loss(bestSolution, nums) < loss(current, nums)):
            current = bestSolution

        if loss(current, nums) == 0:
            return current, i
    return current, maxIteration


def main(numbers):
    timeBefore = time.time()
    result = hillClimbing(numbers, 10)
    sumSubsetValue = sumSubset(result[0], numbers)
    itertion = 0

    while(not (sumSubsetValue[0] == sumSubsetValue[1] == sumSubsetValue[2])):
        result = hillClimbing(numbers, 10000)
        sumSubsetValue = sumSubset(result[0], numbers)
        itertion += 1

    print(result)
    print(itertion)
    print(sumSubset(result[0], numbers))
    print(time.time() - timeBefore)

if __name__ == "__main__":
    main([1, 9, 5, 5, 3, 7,4,3,5,7,2,1,3,6,9,4,4])
