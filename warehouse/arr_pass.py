import itertools


def list_handle(my_str):
    my_list = my_str.split()
    unique_list = list(set(my_list))
    permutations = list(itertools.permutations(unique_list))
    with open("output/passwords.txt", "w") as file:
        for perm in permutations:
            pwd = ''.join(str(item) for item in perm)
            file.write(pwd + "\n")
        print(
            "\033[32mAfter the password is generated, please refer to the 'output/passwords.txt' file for "
            "details.\033[0m")
