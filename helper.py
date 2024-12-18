import os
import shutil
import random

# Rename all images in ascending order
def rename_files(folder):

    # Define the directory containing the files
    directory = folder
    # Define the new naming convention prefix
    new_name_prefix = 'file_'

    # Get a list of all files in the directory
    files = os.listdir(directory)

    # Sort files if necessary (e.g., by name or by creation date)
    files.sort()

    # Loop through the files and rename them
    for i, filename in enumerate(files):
        # Construct the old file path
        old_file_path = os.path.join(directory, filename)

        # Skip directories and non-files
        if not os.path.isfile(old_file_path):
            continue

        # Extract the file extension
        file_extension = os.path.splitext(filename)[1]

        # Construct the new file name
        new_file_name = f"{i + 1}{file_extension}"

        # Construct the new file path
        new_file_path = os.path.join(directory, new_file_name)

        # Rename the file
        os.rename(old_file_path, new_file_path)

        print(f"Renamed '{filename}' to '{new_file_name}'")

    print("Batch renaming completed.")

# Train Val Test split for dataset

def split_dataset(image_dir, label_dir, output_dir, train_ratio=0.8, val_ratio=0.1):
    # Get all image files
    images = [f for f in os.listdir(image_dir) if os.path.isfile(os.path.join(image_dir, f))]

    # Shuffle the dataset
    random.shuffle(images)

    # Calculate the number of images for each set
    total_images = len(images)
    train_count = int(total_images * train_ratio)
    val_count = int(total_images * val_ratio)
    test_count = total_images - train_count - val_count

    # Define the splits
    train_images = images[:train_count]
    val_images = images[train_count:train_count + val_count]
    test_images = images[train_count + val_count:]

    # Helper function to copy files
    def copy_files(file_list, src_img_dir, src_lbl_dir, dest_img_dir, dest_lbl_dir):
        for file_name in file_list:
            base_name = os.path.splitext(file_name)[0]
            img_file = os.path.join(src_img_dir, file_name)
            lbl_file = os.path.join(src_lbl_dir, f"{base_name}.txt")

            if os.path.exists(img_file) and os.path.exists(lbl_file):
                shutil.copy(img_file, dest_img_dir)
                shutil.copy(lbl_file, dest_lbl_dir)
            else:
                print(f"Warning: File pair for {file_name} not found!")

    # Create the output directories if they don't exist
    os.makedirs(output_dir, exist_ok=True)
    for folder in ['train', 'val', 'test']:
        os.makedirs(os.path.join(output_dir, 'images', folder), exist_ok=True)
        os.makedirs(os.path.join(output_dir, 'labels', folder), exist_ok=True)

    # Copy the files to their respective directories
    copy_files(train_images, image_dir, label_dir, os.path.join(output_dir, 'images', 'train'),
               os.path.join(output_dir, 'labels', 'train'))
    copy_files(val_images, image_dir, label_dir, os.path.join(output_dir, 'images', 'val'),
               os.path.join(output_dir, 'labels', 'val'))
    copy_files(test_images, image_dir, label_dir, os.path.join(output_dir, 'images', 'test'),
               os.path.join(output_dir, 'labels', 'test'))

    print("Dataset split completed successfully!")
