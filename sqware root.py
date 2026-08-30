def square_numbers(start, end):
    odd = []
    even = []

    for num in range(start, end + 1):
        square = num ** 2

        if square % 2 == 0:
            even.append(square)
        else:
            odd.append(square)

    print("Even squares:", even)
    print("Odd squares:", odd)


square_numbers(1, 10)
