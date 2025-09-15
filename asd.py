def add(a, b):
    return a + b

def sub(a, b):
    return a - b

def mul(a, b):
    return a * b

def div(a, b):
    if b == 0:
        raise ValueError("Деление на ноль невозможно")
    return a / b


if __name__ == "__main__":
    print("Простой калькулятор")
    print("Доступные операции: +, -, *, /")

    a = float(input("Введите первое число: "))
    op = input("Операция (+ - * /): ")
    b = float(input("Введите второе число: "))

    if op == "+":
        print("Результат:", add(a, b))
    elif op == "-":
        print("Результат:", sub(a, b))
    elif op == "*":
        print("Результат:", mul(a, b))
    elif op == "/":
        print("Результат:", div(a, b))
    else:
        print("Неизвестная операция")

#Веселю день 1
