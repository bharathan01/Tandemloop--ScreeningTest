def generate_series(x):
    series = []

    for number in range(1, x + 1, 2):
        series.append(number)
    series_str = ', '.join(map(str, series))
    return series_str

x = int(input("Enter a positive integer: "))

result = generate_series(x)
print("input a" ,x ,"then output" ,result)
