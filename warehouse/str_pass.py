import itertools

def str_handle(my_str, min, max):
    unique_list = list(set(my_str))
    new_str = ''.join(unique_list)
    combinations = itertools.chain.from_iterable(
        itertools.product(new_str, repeat=i) for i in range(min, max + 1))
    with open('output/passwords.txt', 'w') as f:
        for combination in combinations:
            f.write(''.join(combination) + '\n')
        print("\033[32mAfter the password is generated, please refer to the 'output/passwords.txt' file for details.\033[0m")
