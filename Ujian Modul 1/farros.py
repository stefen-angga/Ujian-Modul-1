# Question 1

def hashtag(input_string):
    result_string = "#"

    for word in input_string.split():
        result_string += word[0].upper() + word[1:].lower()

    if len(result_string) == 1:
        return False

    if len(result_string) > 141:
        return False

    return result_string


# Test function
input_string = " Hello there how are you doing"
# input_string = "   Hello    World  "
# input_string = ""  # return False

result = hashtag(input_string)
print(result)


# Question 2

def create_phone_number(number):
    result_string = "("

    for i in range(0, 3):
        result_string += str(number[i])

    result_string += ") "

    for i in range(3, 6):
        result_string += str(number[i])

    result_string += "-"

    for i in range(6, 10):
        result_string += str(number[i])

    return result_string


# Test function
number = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
result = create_phone_number(number)
print(result)

# Question 3
# odd number = ascending
# even number = descending

def sort_odd_even(list_num):
    even_list = []
    odd_list = []
    result_list = []

    for num in list_num:
        if num % 2 == 0:
            even_list.append(num)
        else:
            odd_list.append(num)

    odd_list.sort()
    even_list.sort(reverse=True)

    i = 0
    j = 0
    for num in list_num:
        if num % 2 == 0:
            result_list.append(even_list[i])
            i += 1
        else:
            result_list.append(odd_list[j])
            j += 1

    return result_list


# Test function

list_num = [5, 3, 2, 8, 1, 4]

result = sort_odd_even(list_num)
print(result)

# Question 4


def hollow_triangle(num):
    result_str = ""
    for row in range(1, num + 1):
        for col in range(1, 2 * num):
            if row == num or row + col == num + 1 or col - row == num - 1:
                result_str += "#"
            else:
                result_str += "_"
        result_str += "\n"
    return result_str


# Test function

# result = hollow_triangle(1)
# result = hollow_triangle(2)
# result = hollow_triangle(3)
# result = hollow_triangle(4)
# result = hollow_triangle(5)
result = hollow_triangle(6)
print(result)
