import itertools
from functools import reduce

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

# Example usage:
if __name__ == "__main__":
    nums = [1,9,5,5,3,7]
    result = threePartition(nums)

    if result:
        print("A valid partition is:")
        for i, part in enumerate(result):
            print(f"Group {i+1}: {part}")
    else:
        print("No valid partition found.")
