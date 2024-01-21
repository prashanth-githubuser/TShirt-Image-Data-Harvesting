import time
from datetime import datetime
import pandas as pd
from selenium import webdriver
from selenium.common.exceptions import NoSuchWindowException
from selenium.webdriver.common.by import By
import os

class Scrape_Data:
    '''scrape data from a specified URL using Selenium and save the results to a CSV file.

        Initialize the web scraper with the given URL, page range, and check point.
        Parameters:
            URL (str): The URL of the website to scrape.
            page_from (int): The starting page number.
            page_to (int): The ending page number.
            check_point: A value used for checking the progress of the scrape.
        Note: URL Works only for myntra.com domain
    '''
    def __init__(self,
               URL="https://www.myntra.com/men-tshirts", page_from:int=1, page_to:int=1, check_point = 500):
        self.URL = URL
        self.page_from = f"?p={str(page_from)}"
        self.page_to = f"?p={str(page_to)}"
        self.CSS = By.CSS_SELECTOR

        try:
            self.driver = webdriver.Chrome()
            self.driver.get(self.URL+self.page_from )
            #self.driver.maximize_window()
            time.sleep(1)

        except Exception as e:
            print(e)
        # initialize the data dictionary
        self.data = {'Brand': [], 'Desc': [], 'DetailedDesc': [],
                'DiscountPrice': [], 'OriginalPrice': [], 'DiscountPercentage': [],
                'ProductLink': [], 'Images': [], 'ZoomedImages': []}
        self.check_point = check_point
    
    def search_elements(self, value:str = None):
        """ Search for elements using the given CSS selector and return a list of matching elements.
        Args: 
            value: (str) The CSS selector to search for.
        return: (list) A list of matching elements.
        """
        try:
            return self.driver.find_elements(self.CSS, value)
        except Exception as e:
            print(e)

    def save_to_csv(self, artifacts_path = None, page = None, total_data_points = None):
        """
        Save the data to a CSV file.

        Args:
            page (int): The page number of the data.
            total_data_points (int): The total number of data points.

        Returns:
            None
        """
        df = pd.DataFrame(self.data)
        # format the date to dd_mm_yy
        formatted_today_date = datetime.now().strftime("%d_%m_%y")
        # format the file name
        format = f"tshirts_{formatted_today_date}_pg{page}_cp_{total_data_points}.csv"
        full_path = os.path.join(artifacts_path, format)
        # save the file
        df.to_csv(full_path, index=False, encoding='utf-8-sig')
        print(f"File saved as: {format}\n-------------------------------------------------------")