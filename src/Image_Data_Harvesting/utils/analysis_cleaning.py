from pathlib import Path
from config.configuration import Analysis_Cleaning_Config
from utils.analysis_helper import duplicate_details_in_metadata_file
from utils.general_helper import walk_through_dir
from utils.cleaning_helper import perform_cleaning

config = Analysis_Cleaning_Config()


def analysis():
    """
    Prints folders and subfolders details, asks the user whether to perform cleaning,
    calls the cleaning function if user input is 'yes', and handles other user inputs.
    """
    try:
        # prints folders and sub folders details
        walk_through_dir(config.artifact_dir)
        metadata_path_list = duplicate_details_in_metadata_file(config.metadata_file_dir)

        # Ask the user whether to perform cleaning
        user_input = input("Do you want to perform cleaning? (yes/no/exit): ").lower()
        if user_input == 'yes':
            # Call the cleaning function here
            perform_cleaning(metadata_path_list)
            print("Cleaning completed.")
        elif user_input == 'no':print("No cleaning performed. Exiting.....")
        elif user_input == 'exit': print("Exiting the program.")  
        else: print("Invalid input. Exiting.....")
    except Exception as e:
        print(e)   




