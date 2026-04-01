#5.Create multiple suitable exceptions for a file handling program. 
try:
    filename = input("Enter a file name: ")

    try:
        with open(filename,"r") as file:
            print("File contents: ")
            print(file.read())
    
    except PermissionError:
        print("Error: You do not have permission to open this file")
    except IsADirectoryError:
        print("Error: Directory Error")
    except Exception as e:
        print("Error: An unexpected error has occured")

except FileNotFoundError:
    print("Error: The file was not found.Please check the name and try again")