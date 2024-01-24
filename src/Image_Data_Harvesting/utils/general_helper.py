import os
import requests
import pandas as pd
from tqdm import tqdm
from pathlib import Path

def walk_through_dir(dir_path):

    """
    Walks through directory path returning its content.

    Args:
        dir_path (str): The path of the directory to walk through.

    Prints:
        The number of subdirectories and files in each directory within the specified path.
    """
    dir_path = Path(dir_path)
    for dirpath, dirnames, filename in os.walk(dir_path):
        print(f"\nThere are {len(dirnames)} directories and {len(filename)} files in '{dirpath}")
    print('------------------------------------------------------------------------------------')

def download_images_from_url(input_url: str, image_output_dir):
    """
    Download images from the input URL and save them to the specified output directory.

    Args:
        input_url (str): The URL of the image to download.
        image_output_dir: The directory where the images will be saved.

    Returns:
        None
    """
    # Create the output folder if it doesn't exist
    os.makedirs(image_output_dir, exist_ok=True)
    
    # Extract the image file name
    img_name = os.path.join(image_output_dir, input_url.split('/')[-5]+".jpg")
    print(img_name)
    
    # Make a request to the image URL
    img_content = requests.get(input_url).content
    
    # Save the image
    with open(img_name, 'wb') as img_file:
        img_file.write(img_content)
        print(f"Image '{img_name}' downloaded successfully.")

import os
import requests
import pandas as pd

# Function to download an image
def download_image(url, file_name, index, output_folder):
    """
    Download an image from a given URL and save it to the specified output folder.

    Args:
        url (str): The URL of the image to be downloaded.
        file_name (str): The name of the file to be saved.
        index (int): The index of the image.
        output_folder (str): The folder where the image will be saved.

    Returns:
        None
    """
    # Create the output folder if it doesn't exist
    os.makedirs(output_folder, exist_ok=True)

# Extract the image file name (considering )
    post_trimmed_name = file_name.strip('tshirts')[10:-4] + f'_{index}' # removing tshirts_21_01_24_
    
    img_name = os.path.join(output_folder,f"{post_trimmed_name}.jpg")
    #print(f"Downloading image from URL: {url}")

    response = requests.get(url)
    
    # Check if the request was successful (status code 200)
    if response.status_code == 200:
        # Save the image
        with open(img_name, 'wb') as img_file:
            img_file.write(response.content)
            #print(f"Image '{img_name}' downloaded successfully.")
    else:
        print(f"Failed to download image:{img_name}. Status code: {response.status_code}")

def extract_images_from_metadata_file(input_csv_dir: Path, image_output_path, index_range=None):
    """
    Extracts images from a metadata file and downloads them to the specified image output path.

    :param input_csv_dir: The directory of the input CSV file containing metadata
    :param image_output_path: The path where the downloaded images will be saved
    :param index_range: Optional range of indices to process in the DataFrame
    """
    
    try:
            df = pd.read_csv(input_csv_dir, encoding='utf-8-sig')
            file_name = Path(input_csv_dir).name
    except Exception as e:
        print(e)
    
    # Use the entire DataFrame if index_range is not provided
    try:
        if index_range is None:
            index_range = (0, len(df))
        print(f"Download started............. {file_name}")
        for index, row in tqdm(df.loc[index_range[0]:index_range[1]].iterrows()):
            link = row['Images'][:-2]
            try:
                #print(link)
                download_image(link,file_name,index, image_output_path)
            except Exception as e:
                print(e)
    except Exception as e:
        print(e)

def extract_images_from_metadata_folder(input_metadata_dir: Path, image_output_dir):

    csv_path_list = list(Path(input_metadata_dir).glob("*.csv"))

    for path in csv_path_list[1:]:
        extract_images_from_metadata_file(path, image_output_dir)
    