# Import the os module to interact with the operating system
import os

def list_directory_contents(directory):
    """
    Lists the contents of the specified directory.

    Parameters:
    directory (str): The path to the directory to list.
    """
    try:
        # List all files and directories in the specified directory
        contents = os.listdir(directory)
        
        # Print the contents of the directory
        print(f"Contents of '{directory}':")
        for item in contents:
            print(item)  # Print each item in the directory
    except FileNotFoundError:
        # Handle the case where the directory does not exist
        print(f"The directory '{directory}' does not exist.")
    except PermissionError:
        # Handle the case where permission is denied to access the directory
        print(f"Permission denied for accessing '{directory}'.")

if __name__ == '__main__':
    # Use the current directory as the default directory
    current_directory = os.getcwd()  # Get the current working directory
    
    # Call the function to list the contents of the current directory
    list_directory_contents(current_directory)