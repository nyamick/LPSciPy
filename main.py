from scipy.optimize import linprog
def linProgMain(): #лп 0
    obj = [-45000, -76000] #кф целевой функции

    lhs_ineq = [[22, 28], #матрица ограничений
                [10, 14],
                [1, 2],
                [2, 0.8],
                [1, 1.1]]

    rhs_ineq = [ 325, #ограничения
                155,
                 20,
                 20,
                 15]

    lb1 = [(0, float("inf")), (0, float("inf"))]  # одз переменных
    opt = linprog(c=obj, A_ub=lhs_ineq, b_ub=rhs_ineq, bounds=lb1,
                  method="highs")
    # вывод результатов
    print(opt)
    print(
        "\n-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------\n")
def linProgOne(): #lp1
    obj = [-45000, -76000] #кф целевой функции

    lhs_ineq = [[22, 28], #матрица ограничений
                [10, 14],
                [1, 2],
                [2, 0.8],
                [1, 1.1]]

    rhs_ineq = [ 325, #ограничения
                155,
                 20,
                 20,
                 15]

    lb1 = [(0, float("inf")), (0, 7)]  # одз переменных
    opt = linprog(c=obj, A_ub=lhs_ineq, b_ub=rhs_ineq, bounds=lb1,
                  method="highs")
    # вывод результатов
    print(opt)
    print(
        "\n-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------\n")
def linProgTwo(): #lp2
    obj = [-45000, -76000] #кф целевой функции

    lhs_ineq = [[22, 28], #матрица ограничений
                [10, 14],
                [1, 2],
                [2, 0.8],
                [1, 1.1],
                [0, 1]]

    rhs_ineq = [ 325, #ограничения
                155,
                 20,
                 20,
                 15,
                 8]
    lb1 = [(0, float("inf")), (8, float("inf"))]  #одз переменных
    opt = linprog(c=obj, A_ub=lhs_ineq, b_ub=rhs_ineq,bounds=lb1,
                  method="highs")
    #вывод результатов
    print(opt)
    print(
        "\n-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------\n")
#вызов функций
linProgMain()
linProgOne()
linProgTwo()