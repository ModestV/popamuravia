import random

def random_math_task():
    a = random.randint(1, 10)
    b = random.randint(1, 10)
    op = random.choice(["+", "-", "*"])
    
    if op == "+":
        result = a + b
    elif op == "-":
        result = a - b
    else:
        result = a * b

    return f"{a} {op} {b} = {result}"

if __name__ == "__main__":
    print("Случайный пример:")
    print(random_math_task())
