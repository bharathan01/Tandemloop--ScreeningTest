def generate_series(x):
    series = []

    for number in range(2*x):
        if(number % 2 == 0):
            continue;
        else:
            series.append(number)
    series_str = ', '.join(map(str, series))

    return series_str

x = int(input("Enter a positive integer : "))

result = generate_series(x)
print("input a" ,x ,"then output" ,result)
