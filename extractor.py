from config.configuration import Image_Extraction_Config
from utils.general_helper import extract_images_from_metadata_file, extract_images_from_metadata_folder

from_metadata_file = Image_Extraction_Config().from_metadata_file
starting_index = Image_Extraction_Config().from_index
ending_index = Image_Extraction_Config().to_index
from_metadata = Image_Extraction_Config().from_metadata
image_output_path = Image_Extraction_Config().image_output_path

extract_images_from_metadata_folder(from_metadata, image_output_path)
#if from_metadata_file is not None:
    #extract_images_from_metadata_file(from_metadata_file, image_output_path)
#elif (starting_index is not None) and (ending_index is not None) :
    #extract_images_from_metadata_file(from_metadata_file, image_output_path, index_range=(starting_index, ending_index))
#elif from_metadata is not None:
    #extract_images_from_metadata_folder(from_metadata, image_output_path)
