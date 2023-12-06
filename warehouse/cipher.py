from tqdm import tqdm
from time import sleep
import os
from colorama import Fore, Style


# loading
def loading_file(file_path, desc):
    total_size = os.path.getsize(file_path)
    with tqdm(total=total_size,
              desc=f"{Fore.LIGHTBLUE_EX}{desc}{Style.RESET_ALL}",
              unit='B',
              leave=True,
              ncols=100,
              unit_scale=True,
              bar_format='{desc}: {percentage:3.0f}%|{bar}| {n_fmt}/{total_fmt} {unit}',
              colour='blue') as pbar:
        with open(file_path, 'rb') as f:
            for chunk in iter(lambda: f.read(1024), b''):
                sleep(0.5)
                pbar.update(len(chunk))
