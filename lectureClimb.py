import math
import random
from matplotlib import pyplot as plt


def ackley(x):
    ret = (-20*math.exp(-0.2*math.sqrt(0.5*(x[0]**2 + x[1]**2))) -
           math.exp(0.5*(
                   math.cos(x[0]*2*math.pi) + math.cos(2*math.pi*x[1]))
                    ) + math.e + 20)
    return ret

def himmelblau(v):
    x = v[0]
    y = v[1]
    ret = (x**2+y-11)**2+(x+y**2-7)**2
    return ret

def generate_start_point():
    return [random.random()*10-5, random.random()*10-5]

def genetic_algorithm(init_pop, term_condition,
                      fitness, selection,
                      crossover,
                      mutation):
    population = init_pop()
    while term_condition(population):
        population_fit = [ fitness(e) for e in population ]
        selected_indexes = selection(population_fit)
        offspring = crossover(selected_indexes, population)
        offspring = mutation(offspring)
        population = offspring

    return population
def decode_chromosome(chromosome):
    x = 0
    y = 0
    for v in chromosome[0:len(chromosome)/2]:
        x = x * 2 + v
    for v in chromosome[len(chromosome)/2:]:
        y = y * 2 + v
    x = 10.0 * x / (2**(len(chromosome)/2)) - 5.0
    y = 10.0 * y / (2**(len(chromosome)/2)) - 5.0
    return [x,y]

def fitness_factory(fun):
    def fitness(chromosome):
        return 1.0/(fun(decode_chromosome(chromosome))+0.01)
    return fitness

def main():
    sp = generate_start_point()
#     best, points, goals = sim_annealing(sp, 200, N, T, himmelblau)
    x = [ x[0] for x in points ]
    y = [ x[1] for x in points ]
    ax = plt.axes(projection='3d')
    ax.plot3D(x,y, goals)
    plt.show()
    print(sp,best)

if __name__ == '__main__':
    main()
