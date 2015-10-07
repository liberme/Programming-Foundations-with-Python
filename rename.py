import os

def rename_file():
    # find the file name
    list_filename = os.listdir(r"C:\Udacity\prank")
    #print(list_filename)
    #print(os.getcwd())
    os.chdir(r"C:\Udacity\prank")
    save_path = os.getcwd()
    print(os.getcwd())

    # then rename
    for file_name in list_filename:
        os.rename(file_name, file_name.translate(None, '0123456789'))
        print("old name:", file_name)
        print("Change to:", file_name.translate(None, '0123456789'))
    os.chdir(save_path)


rename_file()
    
    
