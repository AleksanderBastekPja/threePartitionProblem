import random
import time
import sys
from utils import loss, makeRandomSolution, showResults

def create_population(n, size):
    return [makeRandomSolution(len(n)) for _ in range(size)]

def selection(population, losses, tournament_size=3):
    selected = []
    for _ in range(len(population)):
        tournament = random.sample(list(zip(population, losses)), tournament_size)
        winner = min(tournament, key=lambda x: x[1])[0]
        selected.append(winner)
    return selected

def crossover(parent1, parent2, solution_len):
    alpha = random.randint(0, solution_len-1)
    child1 = parent1[:alpha] + parent2[alpha+1:]
    child2 = parent2[:alpha] + parent1[alpha+1:]
    return child1, child2

def mutation(individual, mutation_rate):
    individual_copy = individual.copy()
    for i in range(len(individual_copy)):
        if random.random() < mutation_rate:
            mutation_difference = random.randint(-2, 2)
            individual_copy[i] = (individual_copy[i] + mutation_difference) % 3
    return individual_copy

def genetic(numbers, size, generations, mutation_rate):
    population = create_population(numbers, size)
    maxIteration = 0

    for generation in range(generations):
        losses = [loss(individual, numbers) for individual in population]
        best_individual = min(population, key=lambda x: loss(x, numbers))
        population = selection(population, losses)

        next_population = []
        for i in range(0, len(population), 2):
            parent1 = population[i]
            parent2 = population[i+1]

            child1, child2 = crossover(parent1, parent2, len(numbers))
            next_population.append(mutation(child1, mutation_rate))
            next_population.append(mutation(child2, mutation_rate))

        next_population[0] = best_individual
        population = next_population

        if loss(best_individual, numbers) == 0:
            break
        maxIteration += 1
    return population, maxIteration

def main(numbers, maxIteration):
    timeBefore = time.time()
    result = genetic(numbers, 100, maxIteration, 0.3)
    timeAfter = time.time() - timeBefore
    print(result)
    # print(result)
    # showResults(numbers, result, timeAfter)


if __name__ == "__main__":
    numbers = [int(arg) for arg in sys.argv[2:]]
    main(numbers, int(sys.argv[1]))
