# python3
def max_pairwise_product(numbers):
    max_product = 0
    first_max = numbers[0]
    second_max = float('-inf')

    for num in numbers[1:]:
        if num > first_max:
            second_max = first_max
            first_max = num
        elif num > second_max:
            second_max = num

    max_product = first_max * second_max
    return max_product


if __name__ == '__main__':
    input_n = int(input())
    input_numbers = [int(x) for x in input().split()]
    print(max_pairwise_product(input_numbers))
