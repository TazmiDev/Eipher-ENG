import itertools


def list_handle(my_str):
    my_list = input_str.split()
    unique_list = list(set(my_list))
    with open("output/passwords.txt", "w") as file:
        for length in range(1, len(unique_list) + 1):
            combinations = itertools.combinations(unique_list, length)
            for comb in combinations:
                pwd = ''.join(str(item) for item in comb)
                file.write(pwd + "\n")
    print("\033[32mAfter the password is generated, please refer to the 'output/passwords.txt' file for details.\033[0m")
