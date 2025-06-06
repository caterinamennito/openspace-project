#the function opens and reads a file of colleagues
def file_utils(file_path):
    with open(file_path, 'r') as my_file:
            #put list of colleagues in a list
            list_colleagues = my_file.read()
            print(list_colleagues)
    return list_colleagues
    
    
        
 

file_utils('./utils/colleagues.csv')