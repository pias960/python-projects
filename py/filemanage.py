import os
import shutil

# Get the current working directory
path = os.getcwd()

# List all files and directories in the current directory
folder = os.listdir(path)

for files in folder:
    # Check if it is a file (to avoid directories)
    if os.path.isfile(os.path.join(path, files)):
        # Get the filename and extension
        filename, extension = os.path.splitext(files)
        
        # Extract extension (without the dot)
        extension1 = extension[1:]
        
        # Build the folder path for the extension
        folder_path = os.path.join(path, extension1)
        
        # Check if the folder exists, if not create it
        if not os.path.exists(folder_path):
            os.makedirs(folder_path)
        
        # Move the file to the respective folder
        shutil.move(os.path.join(path, files), os.path.join(folder_path, files))
        for i in 
    
        
