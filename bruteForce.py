import itertools
from functools import reduce
import time

def sumSubsetVariations(acc, indexAndSubsetId):
    index, subsetId = indexAndSubsetId
    return [acc[j] + (nums[index] if j == subsetId else 0) for j in range(3)]

def threePartition(nums):
    totalSum = sum(nums)
    if totalSum % 3 != 0:
        return None

    target = totalSum // 3
    n = len(nums)

    for productVariation in itertools.product(range(3), repeat=n):
        subsetSums = reduce(sumSubsetVariations, enumerate(productVariation), [0, 0, 0])

        if subsetSums[0] == target and subsetSums[1] == target and subsetSums[2] == target:

            partition = [[], [], []]
            for i, group in enumerate(productVariation):
                partition[group].append(nums[i])
            return partition

    return None

if __name__ == "__main__":
    timeBefore = time.time()
    nums = [1, 9, 5, 5, 3, 7,4,3,5,7,2,1,3,6,9,4,4]
    result = threePartition(nums)

    if result:
        print("A valid partition is:")
        for i, part in enumerate(result):
            print(f"Group {i+1}: {part}")
    else:
        print("No valid partition found.")

    print(time.time() - timeBefore)

"""
    [0,0,0,0]
    [1,0,0,0]
    [0,1,0,0]
    [0,0,1,0]
    [0,0,0,1]
    
    [2,0,0,0]
    [0,2,0,0]
    [0,0,2,0]
    [0,0,0,2]
"""
