import os
import time

from warehouse.str_pass import str_handle
from warehouse.arr_pass import list_handle
from warehouse import cipher, wordart

version = "1.0.0"
whoami = "TazmiDev"
address = "https://github.com/TazmiDev/"

# File read load
folder_path = 'warehouse'
file_list = os.listdir(folder_path)
for file in file_list:
    if file.endswith('.py'):
        full_path = os.path.join(folder_path, file)
        cipher.loading_file(file_path=full_path, desc="加载文件" + file + "...")

wordart.produce_font()
print("\033[31mVersion:" + version + "\033[0m")
print("\033[31mWhoami:" + whoami + "\033[0m")
print("\033[31mAddress:" + address + "\033[0m")

user_input = input("Please enter:  ")

if user_input == '001' or user_input == '1':
    str_input = input("Please enter the string you want to generate:  ")
    min_len = input("Please enter the minimum length: ")
    max_len = input("Please enter the maximum length: ")
    try:
        min_len = int(min_len)
        max_len = int(max_len)
    except TypeError as e:
        print("Please enter an integer greater than 0!")
    if min_len > 0 and max_len > 0:
        print("\033[31mThe password is being generated. Please wait...\033[0m")
        str_handle(my_str=str_input, min=min_len, max=max_len)
    else:
        print("Please enter an integer greater than 0!")
elif user_input == '002' or user_input == '2':
    str_input = input("Please enter the combination you want to generate (separated by ' '):  ")
    print("\033[31mThe password is being generated. Please wait...\033[0m")
    list_handle(str_input)

elif user_input.lower() == 'exit':
    print("The program has exited, welcome to continue using.")
