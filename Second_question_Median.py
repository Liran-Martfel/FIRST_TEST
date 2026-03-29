def find_median(numbers: list) -> float:
    numbers.sort()
    if len(numbers) % 2 == 0:
        return (numbers[len(numbers) // 2 -1] + numbers[len(numbers) // 2])/2
    else:
        return numbers[len(numbers) // 2]

numbers = [3,1,4,1,5]
print(float(find_median(numbers)))

numbers = [7,2,10,9]
print(float(find_median(numbers)))

numbers = [42]
print(float(find_median(numbers)))
