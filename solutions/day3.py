from pathlib import Path
from typing import List
from collections import Counter

def _binary_to_decimal(binary_number: List[int]):

    decimal = 0
    multilpier = 1
    for bit in binary_number[::-1]:
        decimal += bit*multilpier
        multilpier *= 2
    
    return decimal

def _get_binary_numbers() -> List[List[int]]:

    data_path = Path('data/day3.txt')
    binary_numbers = []
    for binary_number in data_path.read_text().split('\n'):
        binary_numbers.append(list(map(int, binary_number)))

    return binary_numbers

def puzzle1():
    
    binary_numbers = _get_binary_numbers()
    

    n_numbers = len(binary_numbers)
    sums = [0] * len(binary_numbers[0])
    
    for binary_number in binary_numbers:
        for i, digit in enumerate(binary_number):
            sums[i] += digit


    gamma_binary = [1 if s > n_numbers/2 else 0 for s in sums]
    epsilon_binary = [0 if s > n_numbers/2 else 1 for s in sums]


    return _binary_to_decimal(gamma_binary) * _binary_to_decimal(epsilon_binary)

def puzzle2():
    
    oxygen_candidates = _get_binary_numbers()
    co2_candidates = _get_binary_numbers()

    n_bits = len(oxygen_candidates[0])
    for i in range(n_bits):

        sum_of_bits = sum(candidate[i] for candidate in co2_candidates)
        most_common = int(sum_of_bits >= len(co2_candidates)/2)
        least_common = int(not most_common)

        sum_of_bits = sum(candidate[i] for candidate in oxygen_candidates)
        most_common = int(sum_of_bits >= len(oxygen_candidates)/2)
    

        if len(oxygen_candidates) > 1:
            oxygen_candidates = list(filter(lambda x: x[i] == most_common, oxygen_candidates))
        if len(co2_candidates) > 1:
            co2_candidates =  list(filter(lambda x: x[i] == least_common, co2_candidates))

    return _binary_to_decimal(oxygen_candidates[0]) * _binary_to_decimal(co2_candidates[0])


if __name__ == '__main__':
    print('puzzle1: ',puzzle1())
    print('puzzle2: ',puzzle2())