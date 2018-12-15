# Nothing to do with Flash Cards, was already in the directory when I made the project.
# Early beginnings with Python, when I first started learning the language
""" 

import math

print('Combinatorics Calculator:\n'
      '1 - Permutation (No repeats: n!/(n-k)!\n'
      '2 - Permutation (Repeats: n^k)\n'
      '3 - Combinations (No repeats: n!/(k!(n-k)!\n'
      '4 - Combinations (Repeats: (n + k - 1)/k)')

in_data = int(input())

if in_data == 1:
    print('You have selected: 1 - Permutation (No repeats: n!/(n-k)!) \n')

    n = int(input("Enter n: "))
    k = int(input("Enter k: "))

    print (n/k)

    if (n / k) <= 0:
        print('Permutation not calculable. Try flipping the numbers around.')
    else:
        topK = math.factorial(n)
        bottom = math.factorial(n - k)

        permutationCalc = topK / bottom

        print('Permutation, no repeats:')
        print(permutationCalc)
elif in_data == 2:
    print('You have selected: 2 - Permutation (Repeats: n^k \n')
    n = int(input("Enter n: "))
    k = int(input("Enter k: "))
    print('Permutation with repeats: ', math.pow(n, k))
elif in_data == 3:
    print('You have selected: 3 - Combinations (No repeats: n!/(k!(n-k)! \n')

    n = int(input("Enter n: "))
    k = int(input("Enter k: "))

    nMinusK = n - k

    nFactorial = math.factorial(n)
    kFactorial = math.factorial(k)

    combinationCalculation = nFactorial / (kFactorial * (math.factorial(nMinusK)))

    print('Combination with no repeats:')
    print(combinationCalculation)
elif in_data == 4:
    print('You have selected: 4 - Combinations (Repeats: (n + k - 1)/k) ')
    # After initial formula is reduced, we get the same formula for a Combination, no repeats problem

    n = int(input("Enter n: "))
    k = int(input("Enter k: "))

    numeratorCalculation = n + k - 1
    numeratorFactorial = math.factorial(numeratorCalculation)
    kFactorial = math.factorial(k)
    nMinusK = n-k

    combinationRepeatsCalculation = numeratorFactorial / (kFactorial * (math.factorial(nMinusK)))

    print('Combination with repeats: ')
    print(combinationRepeatsCalculation)
else:
    print('No combinatoric operator has been selected. Exiting now.')
"""""