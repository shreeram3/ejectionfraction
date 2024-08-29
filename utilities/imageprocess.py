import os
import cv2

def apply_bilateral_filter(input_folder, output_folder):
    # Create the output folder if it doesn't exist
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    # Get a list of all files in the input folder
    input_files = os.listdir(input_folder)

    for filename in input_files:
        if filename.endswith(('.jpg', '.png', '.jpeg')):
            # Read the frame
            frame_path = os.path.join(input_folder, filename)
            img = cv2.imread(frame_path)

            # Apply bilateral filter
            bilateral = cv2.bilateralFilter(img, d=15, sigmaColor=75, sigmaSpace=75)

            # Save the filtered frame to the output folder
            output_path = os.path.join(output_folder, filename)
            cv2.imwrite(output_path, bilateral)




# Define input and output folder paths in Google Drive
# input_folder_path = '/content/drive/MyDrive/all work-BACKUP/automation folder/frames/2'
# output_folder_path= '/content/drive/MyDrive/all work-BACKUP/automation folder/image processed images/2ch'

# apply_bilateral_filter(input_folder_path, output_folder_path)