import os
from mbox_parser import parse_mbox_file


def list_mbox_files(target_dir):
    mbox_files = []
    for root, _, files in os.walk(target_dir):
        for file in files:
            if file.endswith(".mbox"):
                mbox_files.append(file)
    return mbox_files


if __name__ == '__main__':
    # Specify the directory containing .mbox files
    target_dir = "target_files"  # This should match the volume mount point in Docker

    mbox_file_list = list_mbox_files(target_dir)
    print("List of .mbox files:", mbox_file_list)
    for mbox_file in mbox_file_list:
        print("\n#################################################################")
        print(f'working on {mbox_file}')
        data = parse_mbox_file(f'target_files/{mbox_file}')
        print("#################################################################\n")
        print(data)
    
    
