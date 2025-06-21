import math
import random
from utils import loss, makeRandomSolution, showResults
import sys

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

def tppFitness(randomSolution, numbers):
    return loss(randomSolution, numbers)

def generate_binary_random_solution(labelsLength, basePower):
    ransol = makeRandomSolution(labelsLength)
    encoded_chromosome = encode_chromosome(ransol, basePower)
    return encoded_chromosome

def genetic_algorithm(init_pop, term_condition,
                      fitness, selection,
                      crossover,
                      mutation,
                      validateSets):
    population = init_pop()
    while term_condition(population):
        population_fit = [ fitness(e) for e in population ]
        selected_indexes = selection(population_fit)
        offspring = crossover(selected_indexes, population, validateSets)
        offspring = mutation(offspring, validateSets)
        population = offspring

    return population

def roulette_selection(population):
    ret_population = []
    sum_fitness = sum(population)

    for i in range(len(population)):
        random_selection = random.random()*sum_fitness
        part_sum = 0
        for idx,e in enumerate (population):
            part_sum += e
            if part_sum >= random_selection:
                ret_population.append(idx)
                break
    return ret_population


def two_point_crossover(selected_indexes, population, validateSets, p_crossover = 0.25):

    ret_population = []

    for i in range(0, len(selected_indexes), 2):
        parent1 = population[selected_indexes[i]].copy()
        parent2 = population[selected_indexes[i+1]].copy()
        if random.random() < p_crossover:
            cp1, cp2 = createCrosoverPoints(population, parent1, parent2, validateSets)
            if cp1 is not None:
                ret_population.append(parent1[0:cp1] + parent2[cp1:cp2] + parent1[cp2:])
                ret_population.append(parent2[0:cp1] + parent1[cp1:cp2] + parent2[cp2:])
            else:
                ret_population.append(parent1)
                ret_population.append(parent2)
        else:
            ret_population.append(parent1)
            ret_population.append(parent2)
    return ret_population


def createCrosoverPoints(population, parent1, parent2, validateSets):
    for _ in range(100):
        cp1 = random.randint(0, len(population[0]) - 1)
        cp2 = random.randint(0, len(population[0]) - 1)
        if cp1 > cp2:
            cp1, cp2 = cp2, cp1
        descendant1 = parent1[0:cp1] + parent2[cp1:cp2] + parent1[cp2:]
        descendant2 = parent2[0:cp1] + parent1[cp1:cp2] + parent2[cp2:]
        if validateSets(descendant1) and validateSets(descendant2):
            return cp1, cp2
    return None, None


def mutation_uniform(offspring, validateSets, p_mutation = 0.01):
    ret = offspring.copy()
    for _ in range(100):
        for e in ret:
            for i in range(len(e)):
                if random.random() < p_mutation:
                    e[i] = 1 - e[i]
        if all([validateSets(e) for e in ret]):
            return ret
    return offspring

def fitness_factory(fun, basePower, numbers):
    def fitness(chromosome):
        return fun(decode_chromosome(chromosome, basePower), numbers)
    return fitness

def checkSetsValidity(groupNumber, basePower, chromosome):
    decodedChromosome = decode_chromosome(chromosome, basePower)
    if sorted(decodedChromosome) != sorted([i for i in range(groupNumber)] * 3):
        return False
    return True

def checkSetsFactory(fun, groupNumber, basePower):
    def checkSets(chromosome):
        return fun(groupNumber, basePower, chromosome)
    return checkSets

def best_element(population, fitness):
    best = population[0]
    for e in population:
        if fitness(e) >= fitness(best):
            best = e
    return best

iteration_num = 0
def main(numbers, maxIteration):
    goal = tppFitness
    groupNumber = len(numbers) // 3
    basePower = count_base_power(groupNumber)
    fitness = fitness_factory(goal, basePower, numbers)
    checkSets = checkSetsFactory(checkSetsValidity, groupNumber, basePower)

    def term_condition_iterations(population):
        global iteration_num
        iteration_num = iteration_num + 1

        print(iteration_num,
              decode_chromosome(best_element(population, fitness), basePower),
              [goal(decode_chromosome(e, basePower), numbers) for e in population])
        return iteration_num < maxIteration


    results = genetic_algorithm(lambda : [generate_binary_random_solution(len(numbers), basePower) for i in range(26)],
                      term_condition_iterations,
                      fitness,
                      roulette_selection,
                      two_point_crossover,
                      mutation_uniform,
                      checkSets)

    decoded_result = [decode_chromosome(result, basePower) for result in results]
    print(decoded_result)
    # bestElement = best_element(decoded_result, fitness)
    # print(bestElement)
    # print(sumSubset(bestElement[1], numbers))


if __name__ == "__main__":
    numbers = [int(arg) for arg in sys.argv[2:]]
    main(numbers, int(sys.argv[1]))

