import os
import shutil

parent_dir = os.getcwd()
input_folder = os.path.join(parent_dir, 'input')
output_folder = os.path.join(parent_dir, 'project gutenberg books')

if not os.path.exists(output_folder):
os.makedirs(output_folder)

target_substr = 'project gutenberg'

def move_file(file_path):
shutil.move(file_path, output_folder)

for filename in os.listdir(input_folder):
with open(os.path.join(input_folder, filename), 'r') as file:
current_path = file.name
content_lines = file.read().split('\n')
for i in range(10):
if target_substr in content_lines[i]:
move_file(current_path)
break