import os
from mbox_parser import parse_mbox_file
import subprocess
import shutil

def list_mbox_files(target_dir):
    mbox_files = []
    for root, _, files in os.walk(target_dir):
        for file in files:
            extention = str(file).split('.')[-1]
            if 'mbox' in extention.lower():
                mbox_path = os.path.join(root, file)
                mbox_files.append(mbox_path)
                
    for root, _, files in os.walk('mbox_dir'):
        for file in files:
            extention = str(file).split('.')[-1]
            if 'mbox' in extention.lower():
                mbox_path = os.path.join(root, file)
                mbox_files.append(mbox_path)
    return mbox_files

def pst_to_mbox(target_dir, mbox_dir):
    if not os.path.exists(mbox_dir):
        os.makedirs(mbox_dir)
    for root, _, files in os.walk(target_dir):
        for file in files:
            if file.endswith(".pst") or file.endswith(".ost"):
                command = ["readpst", "-D", "-b", "-o", f"./{mbox_dir}", f"{file}"]
                subprocess.run(command, check=True)



if __name__ == '__main__':
    target_dir = 'target_files'
    mbox_dir = 'mbox_dir'
    pst_to_mbox(target_dir,mbox_dir)
    mbox_file_list = list_mbox_files(target_dir)
    for mbox_file in mbox_file_list:
        print(f'working on {mbox_file}')
        data = parse_mbox_file(mbox_file)
    shutil.rmtree(mbox_dir)
    
