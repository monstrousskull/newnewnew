from utils import validate_number, get_operation_symbol
def add(a, b):
    """Сложение двух чисел"""
    return a + b
def subtract(a, b):
    """Вычитание двух чисел"""
    return a - b
def multiply(a, b):
    """Умножение двух чисел"""
    return a * b
def divide(a, b):
    """Деление двух чисел"""
    if b == 0:
        raise ValueError("Деление на ноль!")
    return a / b

def main():
    print("🎯 Добро пожаловать в калькулятор!")
 
    try:
        num1 = validate_number(input("Введите первое число: "))
        num2 = validate_number(input("Введите второе число: "))
        operation = input("Выберите операцию (+, -, *, /): ")
 
        if operation == '+':
            result = add(num1, num2)
            print(f"Результат: {num1} + {num2} = {result}")
        elif operation == '-':
            result = subtract(num1, num2)
            print(f"Результат: {num1} - {num2} = {result}")
        elif operation == '*':
            result = multiply(num1, num2)
        elif operation == '/':
            result = divide(num1, num2)
        else:
            print("❌ Неизвестная операция!")
 
    except ValueError:
        print("❌ Ошибка: введите числа корректно!")
if __name__ == "__main__":
 main()