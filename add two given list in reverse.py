def add(list_1, list_2):
    update_list_1 = list_1[::-1]
    update_list_2 = list_2[::-1]

    first_number = ''
    second_number = ''

    for number in update_list_1:
        first_number += str(number)
    for number in update_list_2:
        second_number += str(number)

    result = int(first_number) + int(second_number)
    final_list = [int(char) for char in str(result)][::-1]

    return final_list


l1 = [2,4,3]
l2 = [5,6,4]

print(add(l1, l2))
