import math


class MyClass:
    def __init__(self, name: str, side1: float, side2: float, side3: float, side4=0.0):
        self.name = name
        self.side1 = side1
        self.side2 = side2
        self.side3 = side3
        self.side4 = side4

    def print_name(self):
        print(self.name)

    def get_perimeter(self):
        perimeter_value = self.side1 + self.side2 + self.side3 + self.side4
        return perimeter_value

    def get_square_with_multiply(self, multiply=1.0):
        if self.side4 > 0:
            return (self.side1 * self.side2) * multiply
        else:
            side1 = self.side1
            side2 = self.side2
            side3 = self.side3
            p = (side1 + side2 + side3) / 2
            s = math.sqrt(p * (p - side1) * (p - side2) * (p - side3)) * multiply
            return s


figure1 = MyClass(name="квадрат", side4=10, side2=10, side3=15, side1=15)
figure1.print_name()

perimetr_perimeter_figure1 = figure1.get_perimeter()
print(perimetr_perimeter_figure1)

square_perimeter_figure1 = figure1.get_square_with_multiply(multiply=2.5)
print(square_perimeter_figure1)

figure2 = MyClass(name="прямоугольник", side4=20, side2=20, side3=7, side1=7)
figure2.print_name()

square_perimeter_figure2 = figure2.get_square_with_multiply(multiply=0.75)
print(square_perimeter_figure2)

perimetr_perimeter_figure2 = figure2.get_perimeter()
print(perimetr_perimeter_figure2)

figure3 = MyClass(name="треугольник", side2=20, side3=15, side1=7)
figure3.print_name()

square_perimeter_figure3 = figure3.get_square_with_multiply(multiply=0.75)
print(square_perimeter_figure3)

perimetr_perimeter_figure3 = figure3.get_perimeter()
print(perimetr_perimeter_figure3)


# side1 = float(input("Vvedite pervuy storonu: "))
# side2 = float(input("Vvedite vtoruyu storonu: "))
# side3 = float(input("Vvedite tretyu storonu: "))
# side4 = float(input("Vvedite chetvertuyu storonu: "))
users_string = input("Vvedite cherez zapatuyu storony obekta (12, 35, 65....): ")

sides = []
for x in users_string.split(sep=','):
    value = float(str(x).strip())
    sides.append(value)
if len(sides) == 3:
    sides.append(0.0)
elif len(sides) < 3:
    print(f"Vy vveli tolko {len(sides)} storony")


figure4 = MyClass(name="новый объект", side1=sides[0], side2=sides[1], side3=sides[2], side4=sides[3])
figure4.print_name()

square_perimeter_figure4 = figure4.get_square_with_multiply(multiply=0.5)
print(square_perimeter_figure4)

perimetr_perimeter_figure4 = figure4.get_perimeter()
print(perimetr_perimeter_figure4)




# def calk(number1, operation, number2 = 10,): #функция принимает параметры и аргументы
#     print(number1, number2, operation)
#     if operation == "+":
#         return number1 + number2
#     if operation == "-":
#         return number1 - number2
#     if operation == "*":
#         return number1 * number2
#     if operation == "/":
#         if number1 != 0:
#             return number1 / number2
#         else:
#             print("vy vveli 0")
#             return 0
#     if operation == "**":  # vozvedenie v stepen
#         return number1 ** number2
#     if operation == "//":  # Delenie bez ostatka
#         return number1 // number2
#     if operation == "%":
#         return number1 % number2
#     if operation == "///":
#         return math.sqrt(number1)
