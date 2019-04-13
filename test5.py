import os

print(os.listdir(os.getcwd()))


def print_directory_contents(sPath):
    """
    This function takes the name of a directory 
    and prints out the paths files within that 
    directory as well as any files contained in 
    contained directories. 
    This function is similar to os.walk. Please don't
    use os.walk in your answer. We are interested in your 
    ability to work with nested structures. 
    """

    
    current_directory_contents = os.listdir(sPath)
        
    for content in current_directory_contents:

        child_Path = os.path.join(sPath,content)

        if os.path.isfile(child_Path):
            print(content)
        if os.path.isdir(child_Path):
            print_directory_contents(child_Path)


dir_Content_List = "C:/ides"
print_directory_contents(dir_Content_List)