# Sequential_Filenaming.py
# Date: 2021-05-17
# Rename all images in a folder to be sequentially numbered (0.png, 1.png, 2.png, etc.)

import os

def rename_images(folder_path):
    # Get a list of all files in the folder
    files = os.listdir(folder_path)
    
    # Filter out non-image files (assuming they have a .png extension)
    images = [f for f in files if f.endswith('.png')]
    
    # Sort the images to ensure they are renamed in order
    images.sort()
    
    # Rename each image
    for index, image in enumerate(images):
        old_path = os.path.join(folder_path, image)
        new_path = os.path.join(folder_path, f"{index}.png")

        # Check if the new filename already exists
        if os.path.exists(new_path):
            print(f"File {new_path} already exists, skipping.")
            continue

        os.rename(old_path, new_path)
        print(f"Renamed {old_path} to {new_path}")

# Replace 'your_folder_path' with the actual path to your folder
# rename_images('D:\Users\Ejay2049\OneDrive - University of Iowa\OpenCV\GitHub\OpenCV\Cpp\OpenCV-Cpp_Projects\workspace\SNR_Calculation\data\May17\Naming_Number')  #your_folder_path, Example: rename_images('C:/Users/Username/Pictures') # NG, please use forward slashes
rename_images(r'D:\Users\Ejay2049\OneDrive - University of Iowa\OpenCV\GitHub\OpenCV\Cpp\OpenCV-Cpp_Projects\workspace\SNR_Calculation\data\May17\Naming_Number')  # Use raw string with r'' if you have backslashes in your path
# rename_images('D:/Users/Ejay2049/OneDrive - University of Iowa/OpenCV/GitHub/OpenCV/Cpp/OpenCV-Cpp_Projects/workspace/SNR_Calculation/data/May17/Naming_Number')  # Use forward slashes
