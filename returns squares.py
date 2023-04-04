def numbers(input_list):
    output_list= []
    for number in input_list:
        output_list .append(number ** 2)
    return output_list

input_list = [input("Enter a number: "),input("Enter another number: "), input("Enter a number: "), input("Enter a number: ")]
input_list = [int(number) for number in input_list]

output_list = numbers(input_list)
print(output_list)


