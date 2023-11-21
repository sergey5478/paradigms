array1 = [2, 4, 6, 8]
array2 = [2, 4, 10, 12]

# Найдем среднее значение массива
mean = lambda arr: sum(arr) / len(arr)


# Вычислим корреляцию Пирсона
def pearson_corr(x, y):
    mean_x, mean_y = mean(x), mean(y)
    n = len(x)
    numerator = sum((xi - mean_x) * (yi - mean_y) for xi, yi in zip(x, y))
    denominator = (sum((xi - mean_x) ** 2 for xi in x) *
                   sum((yi - mean_y) ** 2 for yi in y)) ** 0.5
    return numerator / denominator


result = pearson_corr(array1, array2)
print("Коэффициент корреляции Пирсона между двумя массивами:", result)
