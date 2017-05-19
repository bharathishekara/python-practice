import os
def file_rename():
    #
    file_list = os.listdir(r"C:\Users\bchandr1\Test")
    print(file_list)
    #
    saved_path = os.getcwd()
    os.chdir(r"C:\Users\bchandr1\Test")
    for file_name in file_list:
        os.rename(file_name, file_name.translate(None, "0123456789"))
    os.chdir(saved_path)

file_rename()
