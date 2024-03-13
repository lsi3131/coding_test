import sys
import os

cur_dir = os.getcwd()
print(cur_dir)

file_list = os.listdir(cur_dir)
print(file_list)

from_path_list = [os.path.join(cur_dir, f) for f in file_list if f.startswith('Problem')]
to_path_list = [os.path.join(cur_dir, 'test_' + f.lower()) for f in file_list if f.startswith('Problem')]

print(from_path_list)
print(to_path_list)
path_list = list(zip(from_path_list, to_path_list))
print(path_list)

for from_path, to_path in path_list:
    os.rename(from_path, to_path)
# print('hello')