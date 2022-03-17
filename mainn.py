import time

import numpy as np


class Matrix:
    def __init__(self, name, shape, matrix):
        self.name = name
        self.shape = shape
        self.matrix = matrix


class Vector:
    def __init__(self, name, shape, vector):
        self.name = name
        self.shape = shape
        self.vector = vector


def set_matrix():
    name = input("Podaj nazwę macierzy: ")
    for matrix in all_matrix:
        if matrix.name == name:
            print("Taka nazwa już istnieje, proszę wpisać inną!")
            set_matrix()
    i_len = int(input("Podaj pierwszy rozmiar macierzy: "))
    ii_len = int(input("Podaj drugi rozmiar macierzy: "))
    wymiar = (i_len, ii_len)
    value = input(menu2)
    match value:
        case '1':
            a = list(map(int, input("Podaj wartości do macierzy(po spacji): ").strip().split()))[:ii_len * i_len]
            mat = np.array(a).reshape(i_len, ii_len)
            print(mat)
            m = Matrix(name, wymiar, mat)
            all_matrix.append(m)
        case '2':
            mat = np.ones(wymiar)
            print(mat)
            m = Matrix(name, wymiar, mat)
            all_matrix.append(m)
        case '3':
            mat = np.ones(wymiar)
            print(mat)
            m = Matrix(name, wymiar, mat)
            all_matrix.append(m)
        case '4':
            if i_len == ii_len:
                mat = np.identity(i_len)
                print(mat)
                m = Matrix(name, wymiar, mat)
                all_matrix.append(m)
            else:
                print("Tej macierzy nie da się stworzyc, gdyż macierzy nie jest kwadratowa!")
                set_matrix()
        case '5':
            n = input("Podaj wartość liczby: ")
            mat = np.full(wymiar, n)
            print(mat)
            m = Matrix(name, wymiar, mat)
            all_matrix.append(m)
        case '6':
            x = input("Podaj wartości od jakiej liczby maja byc losowane: ")
            n = input("Podaj wartości do jakiej liczby maja byc losowane: ")
            mat = np.random.randint(x, n, size=wymiar)
            print(mat)
            m = Matrix(name, wymiar, mat)
            all_matrix.append(m)


def sub_multi_add_matrix(option):
    f_matrix = input("Podaj nazwę pierwszej macierzy: ")
    s_matrix = input("Podaj nazwę drugiej macierzy: ")
    tmp1, tmp2 = 0, 0
    for m in all_matrix:
        if m.name == f_matrix:
            tmp1 = m.matrix

    for m in all_matrix:
        if m.name == s_matrix:
            tmp2 = m.matrix

    match option:
        case "+":
            print(tmp1 + tmp2)
        case "-":
            print(tmp1 - tmp2)
        case "*":
            np.dot(tmp1, tmp2)


def transpose_matrix():
    name = input("Podaj nazwę macierzy do transponowania: ")
    for matrix in all_matrix:
        if matrix.name == name:
            t_matrix = matrix.matrix
            print(t_matrix.transpose())


def display_matrix():
    name = input("Podaj nazwę macierzy do wyświetlenia: ")
    for matrix in all_matrix:
        if matrix.name == name:
            print(matrix.matrix)


def inverse_matrix():
    name = input("Podaj nazwę macierzy do wyświetlenia: ")
    for matrix in all_matrix:
        if matrix.name == name:
            i_matrix = matrix.matrix
            if np.linalg.det(i_matrix) != 0:
                print(np.linalg.inv(i_matrix))


def det_matrix():
    name = input("Podaj nazwę macierzy do wyświetlenia: ")
    for matrix in all_matrix:
        if matrix.name == name:
            d_matrix = matrix.matrix
            print(np.linalg.det(d_matrix))


menu1 = """Menu:
          1. Tworzenie macierzy.
          2. Dodawanie
          3. Odejmowanie
          4. Mnożenie
          5. Transponowanie
          6. Odwracanie
          7. Wyznacznik macierzy
          8. Wyświetlanie macierzy
          9. Zakończenie programu
          """

menu2 = """Menu:
          1. Macierz własna
          2. Macierz wypełniona jedynkami
          3. Macierz wypełniona zerami
          4. Macierz jednostkowa z jedynkami na przekątnej 
          5. Macierz wypełniona jedna liczba
          6. Macierz z losowymi wartościami
          """
all_matrix = []
all_vector = []
while True:
    number = input(menu1)
    match number:
        case "1":
            set_matrix()
        case "2":
            option = "+"
            sub_multi_add_matrix(option)
        case "3":
            option = "-"
            sub_multi_add_matrix(option)
        case "4":
            option = "*"
            sub_multi_add_matrix(option)
        case "5":
            transpose_matrix()
        case "6":
            inverse_matrix()
        case "7":
            det_matrix()
        case "8":
            display_matrix()
        case "9":
            quit()
    time.sleep(3)
