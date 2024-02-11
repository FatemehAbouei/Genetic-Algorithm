import random

# Constants
POPULATION_SIZE = 6
NUMBER_OF_GENERATIONS = 20
CROSSOVER_RATE = 0.8
MUTATION_RATE = 0.1

# Generate initial population
def initialize_population():
    # Create a population with random chromosomes
    return [[random.randint(0, 100) for _ in range(4)] for _ in range(POPULATION_SIZE)]

# Evaluate fitness for each chromosome
def evaluate_population(population):
    # Calculate the fitness value for each chromosome
    fitness_values = [abs(chromosome[0] + 2 * chromosome[1] + 3 * chromosome[2] + 4 * chromosome[3] - 30) for chromosome in population]
    return fitness_values

# Select parents based on roulette wheel selection
def select_parents(population, fitness_values):
    # Calculate probabilities for each chromosome based on their fitness
    total_fitness = sum(fitness_values)
    probabilities = [fitness / total_fitness for fitness in fitness_values]
    cumulative_probabilities = [sum(probabilities[:i+1]) for i in range(len(probabilities))]
    
    parents = []
    # Select two parents using roulette wheel selection
    for _ in range(2):
        random_number = random.random()
        for i, probability in enumerate(cumulative_probabilities):
            if random_number <= probability:
                parents.append(population[i])
                break
    return parents

# Crossover (Point Cut-One)
def crossover(parents):
    # Perform crossover with a certain probability
    if random.random() < CROSSOVER_RATE:
        crossover_point = random.randint(1, len(parents[0]) - 1)
        # Swap genetic information between parents at the crossover point
        return [parents[0][:crossover_point] + parents[1][crossover_point:],
                parents[1][:crossover_point] + parents[0][crossover_point:]]
    else:
        return parents

# Mutation
def mutate(chromosome):
    # Perform mutation with a certain probability
    if random.random() < MUTATION_RATE:
        mutation_point = random.randint(0, len(chromosome) - 1)
        # Mutate a gene in the chromosome
        chromosome[mutation_point] = random.randint(0, 100)

# Genetic Algorithm
def genetic_algorithm():
    population = initialize_population()

    for generation in range(NUMBER_OF_GENERATIONS):
        print(f"Generation {generation + 1}:")
        
        fitness_values = evaluate_population(population)
        best_chromosome_index = fitness_values.index(min(fitness_values))
        best_chromosome = population[best_chromosome_index]
        best_fitness = min(fitness_values)
        print(f"  Best Chromosome: {best_chromosome}, Fitness: {best_fitness}")

        new_population = []

        # Create a new population through selection, crossover, and mutation
        for _ in range(int(POPULATION_SIZE / 2)):
            parents = select_parents(population, fitness_values)
            offspring = crossover(parents)
            for child in offspring:
                mutate(child)
                new_population.append(child)

        population = new_population

    # Find the best chromosome in the final population
    fitness_values = evaluate_population(population)
    best_chromosome_index = fitness_values.index(min(fitness_values))
    best_chromosome = population[best_chromosome_index]
    best_fitness = min(fitness_values)
    
    # Display the final result
    print("\nFinal Result:")
    print(f"Best solution: {best_chromosome}")
    print(f"Result: f(a, b, c, d) = {best_chromosome[0]} + 2 * {best_chromosome[1]} + 3 * {best_chromosome[2]} + 4 * {best_chromosome[3]} - 30 = {best_fitness}")

# Main driver
genetic_algorithm()
