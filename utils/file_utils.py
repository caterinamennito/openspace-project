#the function opens and reads a file of colleagues
def file_utils(file_path):
    with open(file_path, newline='') as my_file:
            #put list of colleagues in a list
            colleagues = my_file.read()
            list_colleagues = colleagues.splitlines()
    return list_colleagues
