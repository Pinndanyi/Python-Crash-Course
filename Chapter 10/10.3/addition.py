while True:
    first_num = input("Please give me a number: ")
    second_num = input("Please give me another number: ")

    try:
        first_num = int(first_num)
        second_num = int(second_num)
    except ValueError:
        print("Please enter the integer numbers.")
    else:
        print("\n" + str(first_num + second_num))