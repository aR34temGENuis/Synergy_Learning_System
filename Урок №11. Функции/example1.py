def factorial(n):
    result = 1

    for i in range(1, n + 1):
        result *= i

    return result


number = int(input())

fact_number = factorial(number)

result_list = []

for i in range(fact_number, 0, -1):
    result_list.append(factorial(i))

print(result_list)