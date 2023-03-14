def main():
    ##################################################
    # Comlete your code here
    ##################################################
    import random
    number1 = random.randint(1,100)
    number2 = random.randint(1,100)
    number3 = random.randint(1,100)
    print(f'Three random numbers: {number1},{number2},{number3}')

    if(number1 < number2 and number1 < number3):
        lowest = number1
        print(f'The lowest number is: {lowest} ')
    elif(number2 < number1 and number1 < number3):
        lowest = number2
        print(f'The lowest number is: {lowest} ')
    else:
        lowest = number3
        print(f'The lowest numbr is : {lowest} ')

if __name__ == '__main__':
    main()
