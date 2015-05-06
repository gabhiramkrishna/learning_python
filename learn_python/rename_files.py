import os

def rename_files():
    # get all file names in a folder
    file_list = os.listdir(r"/home/scorus/prank")
    print(file_list)
    os.chdir(r"/home/scorus/prank")
    # for each file name - rename
    for file_name in file_list:
        os.rename(file_name, file_name.translate(None, "0123456789"))
    print(file_list)

rename_files()
