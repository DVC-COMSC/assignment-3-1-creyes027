def main():
    import random
    number1 = random.randint(1,100)
    number2 = random.randint(1,100)
    number3 = random.randint(1,100)
    print(f'Three random numbers: {number1},{number2},{number3}')

    if(number1 < number2 and number1 < number3):
        lowest = number1
    elif(number2 < number1 and number2 < number3):
        lowest = number2
    else:
        lowest = number3
        
    print(f'The lowest number is {lowest} ')
    pass
if __name__ == '__main__':
    main()
