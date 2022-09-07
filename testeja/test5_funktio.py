def delete_odd(num_list):
    new_list = list(num_list)
    for num in new_list[:]:
        if num % 2 == 1:
            new_list.remove(num)
    return new_list

num_list = [0, 3, 4, 6, 7, 13, 16, 19, 21, 23]

print(num_list)

num_list = (delete_odd(num_list))


print(delete_odd(num_list))


