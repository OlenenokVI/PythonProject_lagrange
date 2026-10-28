from typing import List

def lagrange_function(x_list: List[float],
                      y_list: List[float],
                      x_to_find: float):
    if len(x_list) != len(y_list):
        raise ValueError('Длины списков должны быть одинаковыми')
    if len(x_list) != len(set(x_list)):
        raise ValueError('Все Х должны быть уникальными')
    if len(x_list) < 2:
        raise ValueError('Слишком мало точек')

    result = 0.0
    for x, y in zip(x_list, y_list):
        basis = 1.0
        for x_i in x_list:
            if x != x_i:
                basis *= (x_to_find - x_i) / (x - x_i)
        result += basis * y

    return result

x = [1,2,4,5]
y = [1,4,16,25]
interpolation = lagrange_function(x, y,3)
print(interpolation)



