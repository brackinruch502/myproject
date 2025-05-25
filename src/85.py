import os
import shutil

def move_files(src_dir, dest_dir):
    # Move files from src to dest
    for file in os.listdir(src_dir):
        source_file = os.path.join(src_dir, file)
        target_file = os.path.join(dest_dir, file)
        
        if os.path.isfile(source_file) and os.path.isdir(target_file):
            shutil.move(source_file, target_file)

if __name__ == "__main__":
    src_dir = "path/to/source/directory"
    dest_dir = "path/to/destination/directory"
    
    move_files(src_dir, dest_dir)
