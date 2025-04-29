import random

def fitness(board):
    """
    محاسبه تعداد برخوردهای بین وزیرها در یک آرایش خاص.
    هرچه برخورد کمتر، امتیاز بیشتر.
    """
    conflicts = 0
    for i in range(len(board)):
        for j in range(i + 1, len(board)):
            if board[i] == board[j]:  # هم‌ستونی
                conflicts += 1
            if abs(board[i] - board[j]) == abs(i - j):  # روی یک قطر
                conflicts += 1
    return 28 - conflicts  # امتیاز نهایی: حداکثر 28 بدون برخورد

def selection(population):
    """
    انتخاب دو فرد برتر بر اساس بیشترین fitness
    """
    sorted_population = sorted(population, key=lambda x: fitness(x), reverse=True)
    return sorted_population[0], sorted_population[1]

# مثال برای تست
if name == "__main__":
    sample_population = [
        [0, 1, 2, 3, 4, 5, 6, 7],
        [0, 4, 7, 5, 2, 6, 1, 3],
        [3, 1, 4, 2, 0, 6, 7, 5]
    ]
    fittest = selection(sample_population)
    print("Best two individuals:", fittest)