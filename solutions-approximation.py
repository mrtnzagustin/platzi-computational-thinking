def run():
    number = int(input("Give me a number: "))
    exponential = int(input("Give me a exponential: "))
    epsilon = 0.01
    step = epsilon ** 2
    result = step

    while abs(result ** exponential - number) > epsilon and result < number:
        result += step
    
    if abs(result ** exponential - number) < epsilon:
        print(f'The result for {str(number)}^1/{str(exponential)} is {str(result)}')
    else:
        print(f"There is no close result for {number}^1/{exponential}")


if __name__ == '__main__':
    run()