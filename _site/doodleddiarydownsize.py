import os
from PIL import Image

# Define input and output folder paths
input_folder = "./doodleddiarylarge"
output_folder = "./images/doodleddiary"

# Create the output folder if it doesn't exist
os.makedirs(output_folder, exist_ok=True)

# Define the downsample factor (e.g., 2 for reducing dimensions by half)
downsample_factor = 2

# Iterate over all files in the input folder
for file_name in os.listdir(input_folder):
    # Check if the file is a PNG
    if file_name.lower().endswith('.png'):
        input_path = os.path.join(input_folder, file_name)
        output_path = os.path.join(output_folder, file_name)

        # Skip processing if the output file already exists
        if os.path.exists(output_path):
        #    print(f"Skipping {file_name}: Already exists.")
            continue
        else: 
            print(f"Processing {file_name}...")
            try:
                # Open the image
                with Image.open(input_path) as img:
                    # Downsample the image
                    new_width = img.width // downsample_factor
                    new_height = img.height // downsample_factor
                    downsampled_img = img.resize((new_width, new_height), Image.Resampling.LANCZOS)

                    # Save the downsampled image to the output folder
                    downsampled_img.save(output_path)
                    print(f"Processed {file_name}: Saved to {output_folder}.")
            except Exception as e:
                print(f"Error processing {file_name}: {e}")
