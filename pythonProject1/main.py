import Functions
import StopFun
import Bisection
import Falsi

import numpy as np
import matplotlib.pyplot as plt


def stop_fun_menu():
    print("Wybór kryterium zatrzymania programu")
    print("1. Ilosc iteracji")
    print("2. Dokladnosc wyniku ze wzoru |x - prev_x|")
    print("3. Dokladnosc wyniku ze wzoru |f(x)|")
    menu = int(input("Twoj wybor: "))
    if menu == 1:
        max_interation = int(input("Podaj maksumalna ilosc iteracj: "))
        return None, None, max_interation
    elif menu in (2, 3):
        eps = float(input("Podaj wartosc warunku dokładnosci(epsilon): "))
        return (StopFun.stop_fun_varA, eps, None) if menu == 2 else \
            (StopFun.stop_fun_varB, eps, None)
    else:
        print("Wybrano nieprawidłowa wartosc")
        exit()


def interval():
    print("Podaj przedzial dla jakiego chcesz wyliczyc pierwiastek(a-lewy kraniec przedziału, b-prawy")
    a = float(input("a="))
    b = float(input("b="))
    return a, b


def calculations_and_outcome(a, b, fun, stop_fun, eps, max_iter):
    def calculate_function_values(fun, a, b, num=50):
        x_values = np.linspace(a, b, num)
        y_values = fun(x_values)
        return x_values, y_values

    x_values, y_values = calculate_function_values(fun, a, b)

    plt.plot(x_values, y_values, label='Function' )
    plt.xlabel('x')
    plt.ylabel('f(x)')
    plt.title('Plot of Function')
    plt.grid(True)
    plt.legend()
    plt.show()
    try:

        x_result_falsi, iterations_falsi, accuracy_falsi = Falsi.falsi(a, b, fun, stop_fun, eps,
                                                                       max_iter)
        x_result_bisection, iterations_bisection, accuracy_bisection = Bisection.bisection(a, b, fun, stop_fun, eps,max_iter)

        print("falsi:")
        print(f"x={x_result_falsi}")
        print(f"iteracje={iterations_falsi}")
        print(f"dokladnosc ={accuracy_falsi}")
        print("bisekcja:")
        print(f"x={x_result_bisection}")
        print(f"iteracje={iterations_bisection}")
        print(f"dokladnosc ={accuracy_bisection}")

    except ValueError as e:
        print(e)
        print("Exiting program.")
        exit()


def polynomialMenu():
    degree = int(input("Podaj stopień wielomianu: "))
    coefficients = []
    for i in range(degree + 1):
        coefficient = float(
            input(f"Podaj współczynnik a{i} (w kolejnosci od wspolczynnika przy najwiekszej potedze): "))
        coefficients.append(coefficient)
    return degree, coefficients


def trygonometryMenu():
    print("1. sinus")
    print("2. cosinus")
    print("3. tangens")
    print("4. cotangens")
    tryg = int(input("Wybiesz funkcje trygonometryczna: "))
    fun = Functions.sin
    if (tryg == 1):
        fun = Functions.sin
    elif (tryg == 2):
        fun = Functions.cos
    elif (tryg == 3):
        fun = Functions.tan
    elif (tryg == 4):
        fun = Functions.ctan
    else:
        print("Nieprawidlowy wybor")
        exit()
    return fun


def exponentioalMenu():
    base = int(input("Podaj wartosc podstawy w funkcji wykladniczej"))
    return base


print("Program do rozwiazywania rownan nieliniowych")
print("Wybierz rodzej równania do rozwiazania:")
print("1. Wielomian")
print("2. Funkcja trygonometryczna")
print("3. Funkcja wykladnicza")
print("4. Funkcja zlozona")
menu = int(input("Twoj wybor:"))

a, b = interval()
stop_fun, eps, max_iter = stop_fun_menu()

if (menu == 1):
    degree, coefficients = polynomialMenu()
    calculations_and_outcome(a, b, lambda x: Functions.polynomial(x, coefficients, degree), stop_fun, eps,
                             max_iter)

elif (menu == 2):
    fun = trygonometryMenu()
    calculations_and_outcome(a, b, fun, stop_fun, eps, max_iter)
elif (menu == 3):
    base = int(input("Podaj wartosc podstawy w funkcji wykladniczej"))
    calculations_and_outcome(a, b, lambda x: Functions.exponential(x, base), stop_fun, eps, max_iter)

elif (menu == 4):
    print("Wybierz funkcje wewnetrzna zlozenia:")
    print("1. Wielomian")
    print("2. Funkcja Trygonometryczna")
    print("3. Funkcja Wykładnicza")
    complex1 = int(input("Twoj wybor: "))
    print("Wybierz funkcje zewnetrzna zlozenia:")
    print("1. Wielomian")
    print("2. Funkcja Trygonometryczna")
    print("3. Funkcja Wykładnicza")
    complex2 = int(input("Twoj wybor: "))
    if complex1 == 1 and complex2 == 1:
        print("Pierwszy wielomian:")
        degree1, coefficients1 = polynomialMenu()
        fun1 = lambda x: Functions.polynomial(x, coefficients1, degree1)
        print("Drugi wielomian:")
        degree2, coefficients2 = polynomialMenu()
        fun2 = lambda x: Functions.polynomial(x, coefficients2, degree2)

    elif complex1 == 1 and complex2 == 2:
        degree1, coefficients1 = polynomialMenu()
        fun1 = lambda x: Functions.polynomial(x, coefficients1, degree1)
        fun2 = trygonometryMenu()

    elif complex1 == 1 and complex2 == 3:
        degree1, coefficients1 = polynomialMenu()
        fun1 = lambda x: Functions.polynomial(x, coefficients1, degree1)
        base = exponentioalMenu()
        fun2 = lambda x: Functions.exponential(x, base)

    elif complex1 == 2 and complex2 == 1:
        fun1 = trygonometryMenu()
        degree1, coefficients1 = polynomialMenu()
        fun2 = lambda x: Functions.polynomial(x, coefficients1, degree1)

    elif complex1 == 2 and complex2 == 2:
        print("Pierwsza funkcja tryg")
        fun1 = trygonometryMenu()
        print("Druga funkcja tryg")
        fun2 = trygonometryMenu()

    elif complex1 == 2 and complex2 == 3:
        fun1 = trygonometryMenu()
        base = exponentioalMenu()
        fun2 = lambda x: Functions.exponential(x, base)

    elif complex1 == 3 and complex2 == 1:
        base1 = exponentioalMenu()
        fun1 = lambda x: Functions.exponential(x, base1)
        degree2, coefficients2 = polynomialMenu()
        fun2 = lambda x: Functions.polynomial(x, coefficients2, degree2)

    elif complex1 == 3 and complex2 == 2:
        base1 = exponentioalMenu()
        fun1 = lambda x: Functions.exponential(x, base1)
        fun2 = trygonometryMenu()

    elif complex1 == 3 and complex2 == 3:
        print("Pierwsza funkcja wykladnicza ")
        base1 = exponentioalMenu()
        fun1 = lambda x: Functions.exponential(x, base1)
        print("Druga funkcja wykladnicza ")
        base2 = exponentioalMenu()
        fun2 = lambda x: Functions.exponential(x, base2)

    else:
        print("Bledny wybor")
        exit()

    calculations_and_outcome(a, b, lambda x: Functions.complex(fun1, fun2, x), stop_fun, eps, max_iter)

else:
    print("Nieprawidlowy wybor")
