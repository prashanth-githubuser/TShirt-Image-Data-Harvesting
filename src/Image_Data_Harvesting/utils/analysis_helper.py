import os
from pathlib import Path
import requests
import pandas as pd
from tabulate import tabulate
from tqdm import tqdm




def duplicate_details_in_metadata_file(metadata_path: Path):
    """
    Takes a Path object as input and processes metadata files to find duplicate details.
    """
    try:
        # Converting to list
        metadata_path_list = list(metadata_path.glob("*.csv"))

        duplicate_details_productLink = get_duplicate_details_df(metadata_path_list, 'Images')
        duplicate_details_zoomedimages = get_duplicate_details_df(metadata_path_list, 'ZoomedImages')


        productlink_distinct_count_df = distinct_Count(duplicate_details_productLink)
        zoomedimages_distinct_count_df = distinct_Count(duplicate_details_zoomedimages)


        print('Files contains duplicate Images links')
        print(tabulate(duplicate_details_productLink, headers='keys', tablefmt='pretty'))
        print(tabulate(productlink_distinct_count_df, headers='keys', tablefmt='pretty'),'\n')
        print('Files contains duplicate Zoomed Images links')
        print(tabulate(duplicate_details_zoomedimages, headers='keys', tablefmt='pretty'))
        print(tabulate(zoomedimages_distinct_count_df, headers='keys', tablefmt='pretty'))


        print('------------------------------------------------------------------------------------')

        if productlink_distinct_count_df['Distinct_Count'].sum() > zoomedimages_distinct_count_df['Distinct_Count'].sum():
            print("Images Link has more Distinct Count Dropping duplicate Images Link")

            return metadata_path_list
        else: 
            print("Zoomed Images has more Distinct Count Hence cleaning cannot be proceeded, Exiting......\n")
            return metadata_path_list #None
    except Exception as e:
        print(e)

def get_duplicate_details_df(metadata_path_list, column_name:str):
    """
    Function to generate a DataFrame with duplicate details from a list of metadata paths and a specific column name.
    :param metadata_path_list: List of paths to metadata files
    :param column_name: Name of the column to analyze for duplicates
    :return: DataFrame with columns for file names, distinct count, and duplicate count
    """
    try:
        details = {'FileName':[], 'DistinctCount':[], 'DuplicateCount':[]}
        for path in tqdm(metadata_path_list, desc="Analyzing..."):
            df = pd.read_csv(path)
            result = df[column_name].duplicated().value_counts().to_dict()
            details['FileName'].append(path.name)
            details['DistinctCount'].append(result[False])
            details['DuplicateCount'].append(result[True])
        df = pd.DataFrame(details)

        return df
    except Exception as e:
        print(e)
        
def distinct_Count(df):
    """
    Calculate the distinct count, duplicate count, and total count of a DataFrame.

    :param df: The input DataFrame
    :return: A DataFrame containing the distinct count, duplicate count, and total count
    """
    try:

        result = {"Distinct_Count":df['DistinctCount'].sum(),
                "Duplicate_Count":df['DuplicateCount'].sum(),
                "Total":df['DistinctCount'].sum() + df['DuplicateCount'].sum()}
        result_df = pd.DataFrame([result])

        return result_df
    except Exception as e:
        print(e)


