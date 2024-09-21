# Домашнее задание по теме "Декораторы"

import math

def is_prime(func):
    def wrapper(*args, **kwargs):
        sum = func(*args, **kwargs)
        if sum > 1:
            for i in range(2, int(math.sqrt(sum))):
                if sum % i == 0:
                    print("Составное")
                    return sum
            else:
                print("Простое")
                return sum
        if sum == 1:
            print("Не является ни простым, ни составным")
            return sum
        else:
            print("Число отрицательное")
        return sum
    return wrapper

@is_prime
def sum_three(*args):
    a, b, c = args
    return a + b + c

result = sum_three(13265214,543163,231542)
print(result)

