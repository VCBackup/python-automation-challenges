# Write a function that displays the fibonacci sequence up to a certain number
def fibo_creation(desired_length):
    fibo_values = [0, 1]
    while len(fibo_values) < int(desired_length):
        fibo_values.append(fibo_values[len(fibo_values) - 1] + fibo_values[len(fibo_values) - 2])
        if len(fibo_values) == int(desired_length):
            # print(str(fibo_values))
            return fibo_values


def fibo_twenty_one():
    nine_length_fibo = fibo_creation(9)
    print(str(nine_length_fibo[8]) + ", twenty-one")


def convert_number_to_string():
    print("Design a function to convert the returned value to a string")


# print("How many values of fibonacci would you like to see?")
# fibo_length = input()
# print("Great! Let me print out the fibonacci sequence to a length of " + fibo_length + " for you!")
# print(fibo_creation(fibo_length))
fibo_twenty_one()



























