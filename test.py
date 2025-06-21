def encode_chromosome(labels, base_power):
    result = []
    for label in labels:
        current_label = label
        current_literal = []
        while(current_label > 0):
            current_literal.insert(0, current_label % 2)
            current_label //= 2
        current_literal = [0] * (base_power-len(current_literal)) + current_literal
        result += current_literal
    return result

def decode_chromosome(chromosome, base_power):
    labels = []
    for i in range(0, len(chromosome), base_power):
        binary_label = chromosome[i:i+base_power]
        binary_label.reverse()
        factors = [(binary_label[idx] * 2) ** idx if not (idx == 0 and binary_label[idx] == 0) else 0 for idx in range(len(binary_label))]
        labels.append(sum(factors))
    return labels

def count_base_power(groupNumber):
    power = 0
    while(groupNumber > 1):
        groupNumber = groupNumber // 2
        power += 1
    return power

# def count_base_power(labels):
#     maxNumber = max(labels)
#     power = 0
#     while(maxNumber > 1):
#         maxNumber = maxNumber // 2
#         power += 1
#     return power+1

# labels = [20, 23, 25, 30, 49, 45, 27, 30, 30, 40, 22, 1]
# base_power = count_base_power(labels)
# chromosomes = encode_chromosome(labels, base_power)
#
# if chromosomes == [0,1,0,1,0,0,0,1,0,1,1,1,0,1,1,0,0,1,0,1,1,1,1,0,1,1,0,0,0,1,1,0,1,1,0,1,0,1,1,0,1,1,0,1,1,1,1,0,0,1,1,1,1,0,1,0,1,0,0,0,0,1,0,1,1,0,0,0,0,0,0,1]:
#     print("encoding successful!")
# else:
#     print("encoding fail!")
#
# decoded_chromosomes = decode_chromosome(chromosomes, base_power)
# if (decoded_chromosomes == labels):
#     print("decoding successful!")
# else:
#     print("decoding fail!")

# failingLiteral = [0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 1, 0, 0, 1, 1, 1, 0, 0, 1, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1]

# nums = [2, 3, 2, 1, 1, 3, 0, 0, 1, 0, 3, 2]
# numbersLen = len(nums)
# base_power = count_base_power(numbersLen // 3)
# print(base_power)

# encoded_chromosome = encode_chromosome(nums, base_power)
# print(encoded_chromosome)
# decoded_chromosome = decode_chromosome(encoded_chromosome, base_power)
# print(decoded_chromosome)
# print(decoded_chromosome == nums)

base_power = count_base_power(len([2, 1, 0, 3, 1, 3, 0, 2, 1, 3, 0, 2])//3)
print(base_power)
encoded_chromosome = encode_chromosome([2, 1, 0, 3, 1, 3, 0, 2, 1, 3, 0, 2], base_power)
print(encoded_chromosome)
print(decode_chromosome(encoded_chromosome, base_power))

# [0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 1, 1, 1, 0, 1, 0, 0, 1, 0, 1, 1, 0, 0, 0, 0, 1, 1, 0, 1, 1, 0, 0, 0, 0, 1, 0]
# [2, 1, 0, 3, 5, 1, 3, 0, 3, 3, 0, 2]
# [2, 1, 0, 3, 1, 3, 0, 2, 1, 3, 0, 2]
