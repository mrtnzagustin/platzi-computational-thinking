def run():
    number = int(input("Give me a number: "))
    exponential = int(input("Give me a exponential: "))
    result = 0
    
    # Tries all base from 1 to number
    for actual_base in range(1, number):
        if actual_base ** exponential == number:
            result = actual_base
            break

    if result != 0:
        print(f'The result for {str(number)}^1/{str(exponential)} is {str(result)}')
    else:
        print(f"There is no exact result for {number}^1/{exponential}")


if __name__ == '__main__':
    run()
