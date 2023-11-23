"""
Problem:
    In a university, your attendance determines whether you will be
    allowed to attend your graduation ceremony.
    You are not allowed to miss classes for four or more consecutive days.
    Your graduation ceremony is on the last day of the academic year,
    which is the Nth day.

    Your task is to determine the following:

    1. The number of ways to attend classes over N days.
    2. The probability that you will miss your graduation ceremony.

    Represent the solution in the string format as "Answer of (2) / Answer
    of (1)", don't actually divide or reduce the fraction to decimal

    Test cases:
        for 5 days: 14/29
        for 10 days: 372/773
"""

def calculate_graduation_ceremony_solution(number_of_days:int)->str:
    """
    Used approach:
        Dynamic programming tabulation
    NOTE: solution for 4 or more consecutive days
    """
    table = [[0] * 5 for _ in range(number_of_days + 1)]

    for i in range(4):
        table[0][i] = 1

    
    # Nested loop to iterate over each academic day and the number of consecutive missed classes
    for x in range(1, number_of_days + 1):
        # Inner loop used to calculate the number of ways to attend classes or 
        # miss the current day based on the previous day's values
        for y in range(3, -1, -1):
            table[x][y] = table[x - 1][0] + table[x - 1][y + 1]

    # The number of ways to attend classes over given number of days
    solution1 = table[number_of_days][0] 
    
    # The probability that you will miss your graduation ceremony
    solution2 = table[number_of_days - 1][1]  

    return f"{solution2}/{solution1}"



input_days = input("Enter number of days: ")

try:
    result = calculate_graduation_ceremony_solution(number_of_days=int(input_days))
except ValueError as error:
    result = "Invalid input. Please enter a valid integer."

print(result)
