import os

# Set the path to the folder you want to clean up
folder_path = "D:/data/openfold/openproteinset/pdb"

# Loop through all the items in the folder
for item in os.listdir(folder_path):
    # Construct the full path of the item
    item_path = os.path.join(folder_path, item)

    
    # Check if the item is a directory
    if os.path.isdir(item_path):
        # Loop through all the items in the directory
        for subfolder in os.listdir(item_path):
            # Construct the full path of the subitem
            subfolder_path = os.path.join(item_path, subfolder)
            if os.path.isdir(subfolder_path):
                for subitem in os.listdir(subfolder_path):
                    # Construct the full path of the subitem
                    subitem_path = os.path.join(subfolder_path, subitem)

                    # Move the subitem to the main folder
                    os.rename(subitem_path, os.path.join(item_path, subitem))
                
                # Delete the empty directory
                os.rmdir(subfolder_path)