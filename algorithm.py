import random

def generate_individual(board_size=8):
    # تولید یک حالت تصادفی: در هر ستون یک وزیر با ردیف تصادفی
    return [random.randint(0, board_size - 1) for _ in range(board_size)]

def fitness(queens):
    # محاسبه‌ی تعداد جفت وزیرهایی که همدیگه رو تهدید نمی‌کنن
    non_attacking = 0
    size = len(queens)
    for i in range(size):
        for j in range(i + 1, size):
            if queens[i] != queens[j] and abs(queens[i] - queens[j]) != abs(i - j):
                non_attacking += 1
    return non_attacking

def generate_population(pop_size=10, board_size=8):
    return [generate_individual(board_size) for _ in range(pop_size)]

def selection(population):
    sorted_population = sorted(population, key=lambda q: fitness(q), reverse=True)
    return sorted_population[0], sorted_population[1]

def crossover(parent1, parent2):
    size = len(parent1)
    crossover_point = random.randint(1, size - 2)
    child = parent1[:crossover_point] + parent2[crossover_point:]
    return child

def mutate(individual, mutation_rate=0.1):
    size = len(individual)
    for i in range(size):
        if random.random() < mutation_rate:
            individual[i] = random.randint(0, size - 1)

def genetic_algorithm(pop_size=10, board_size=8, max_generations=1000, mutation_rate=0.1):
    population = generate_population(pop_size, board_size)
    max_fitness = (board_size * (board_size - 1)) // 2

    for generation in range(max_generations):
        best = max(population, key=lambda q: fitness(q))
        if fitness(best) == max_fitness:
            print(f"\n✅ Solution found in generation {generation}:")
            return best

        parent1, parent2 = selection(population)
        child = crossover(parent1, parent2)
        mutate(child, mutation_rate)

        population.sort(key=lambda q: fitness(q))
        population[0] = child

    print("\n❌ No perfect solution found.")
    return max(population, key=lambda q: fitness(q))

# اجرای الگوریتم
if name == "__main__":
    solution = genetic_algorithm()
    print("Solution:", solution)