import os
import random
import shutil
import sys
import math

def group_files(source_dir, dest_dir, output_dir, files_per_folder):
    # Get a list of all the files in the source directory
    files = os.listdir(source_dir)
    # Shuffle the list randomly
    random.shuffle(files)
    # Calculate the number of files per folder
    num_folders = math.ceil(len(files) / files_per_folder)
    # Create the destination folders
    for i in range(num_folders):
        os.makedirs(os.path.join(dest_dir, f"batch{i + 1}"))
        os.makedirs(os.path.join(output_dir, f"batch{i + 1}"))
    # Copy files to the destination folders
    for i, file in enumerate(files):
        folder_index = i // files_per_folder
        folder_name = f"batch{folder_index + 1}"
        shutil.copy(os.path.join(source_dir, file), os.path.join(dest_dir, folder_name))

source_dir = "/expanse/lustre/projects/sds194/amazamontesinos/input_sequences"
dest_dir = "/expanse/lustre/projects/sds194/amazamontesinos/batches"
output_dir = "/expanse/lustre/projects/sds194/amazamontesinos/output_models"
try:
	files_per_folder = int(sys.argv[1])
except:
	files_per_folder = 10
group_files(source_dir, dest_dir, output_dir, files_per_folder)
