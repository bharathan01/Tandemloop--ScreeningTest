def count_multiples(numbers_list):
    multiples_count = {}

    multiples_of = [1, 2, 3, 4, 5, 6, 7, 8, 9]

    for num in multiples_of:
        multiples_count[num] = 0

    for num in numbers_list:
        for multiple in multiples_of:
            if num % multiple == 0:
                multiples_count[multiple] += 1

    return multiples_count


numbers_list = [1, 2, 8, 9, 12, 46, 76, 82, 15, 20, 30]

result = count_multiples(numbers_list)

print(result)


