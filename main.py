import random


def main():
    total = 0
    numbers = [random.randint(0,100) for _ in range(5)]
    total = sum(numbers[:-1])
    print(total)

    #i = 0
    
   

    



    print(f'The random values are {numbers}')
    print(f'The total is {total}')

    ########################################
    # Do not delete the return statement
    ########################################
    return numbers, total


if __name__ == '__main__':
    main()
