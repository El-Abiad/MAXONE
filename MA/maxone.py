import GA.maxone as ga
import random

def local_search(chromosome):
    answer = chromosome.copy()

    for ind in range(3):
        new_chromosome = answer.copy()
        flip = random.randint(0, len(chromosome) - 1)
        new_chromosome[flip] = 1 - new_chromosome[flip]

        if ga.fitness(new_chromosome) > ga.fitness(answer):
            answer = new_chromosome

    return answer


def memetic_algorithm(pop_size, n, generations, mutation_rate):
    population = ga.initialize_population(pop_size, n)

    while(generations):
        parents = ga.selection(population)
        parent1 = parents[0]
        parent2 = parents[1]

        offspring = ga.crossover(parent1, parent2)
        offspring = ga.mutation(offspring, mutation_rate)
        offspring = local_search(offspring)
        population.append(offspring)
        population = ga.remove_bad(population)
        generations -= 1

    return ga.get_best(population)

