import random

def crossover(parent1, parent2):
    """
    ترکیب دو والد برای تولید یک فرزند جدید.
    ژن‌های والد اول تا نقطه‌ای مشخص برداشته می‌شوند، بقیه از والد دوم.
    """
    point = random.randint(1, len(parent1) - 2)
    child = parent1[:point] + parent2[point:]
    return child

def mutation(board, mutation_rate=0.1):
    """
    تغییر تصادفی جای یک وزیر در صفحه.
    با احتمال مشخص mutation انجام می‌شود.
    """
    if random.random() < mutation_rate:
        row = random.randint(0, len(board) - 1)
        new_col = random.randint(0, len(board) - 1)
        board[row] = new_col
    return board

# مثال برای تست
if name == "__main__":
    p1 = [0, 4, 7, 5, 2, 6, 1, 3]
    p2 = [3, 1, 4, 2, 0, 6, 7, 5]
    child = crossover(p1, p2)
    mutated = mutation(child)
    print("Child:", child)
    print("After Mutation:", mutated)