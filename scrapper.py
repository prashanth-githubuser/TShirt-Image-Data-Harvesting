from selenium.webdriver.common.by import By
from utils.web_scrapper import Scrape_Data
from config.configration import Scrapper_Config



"""
Scrapes data from a given URL across multiple pages, extracts various data points,
and saves the data to a CSV file.
Parameters: 
Note : Below defined parameters can be used with configration.py if data pipline is used
"""

# configration
scraper_config = Scrapper_Config()

# initialize the web scraper
data_scraper = Scrape_Data(URL="https://www.myntra.com/men-tshirts",
                    page_from=scraper_config.page_from,
                    page_to=scraper_config.page_to,
                    check_point=scraper_config.check_point)  

page_count = 1
total_data_points = 0
try:
    for j in range(scraper_config.page_from,(scraper_config.page_to)+1):
        Elements = data_scraper.search_elements(value="li.product-base")

        if len(Elements) != 0:

            for i in range(len(Elements)):
                
                # Extracting the data points
                try:product_brand = Elements[i].find_element(By.CLASS_NAME, "product-brand").text
                except:product_brand = None
                try:product_name = Elements[i].find_element(By.CLASS_NAME, "product-product").text
                except:product_name = None
                try:discounted_price = Elements[i].find_element(By.CLASS_NAME, "product-discountedPrice").text
                except:discounted_price = None
                try:original_price = Elements[i].find_element(By.CLASS_NAME, "product-strike").text
                except:original_price = Elements[i].find_element(By.XPATH, ".//div[@class='product-price']/span").text
                try:discount_percentage = Elements[i].find_element(By.CLASS_NAME, "product-discountPercentage").text
                except:discount_percentage = None


                # Extracting the Product link
                try:product_link = Elements[i].find_element(By.CSS_SELECTOR, "a[data-refreshpage='true']").get_attribute("href")
                except:product_link = None

                # Extracting the Image links
                try:
                    image_srcset = Elements[i].find_element(By.CSS_SELECTOR, "source").get_attribute("srcset")
                    image_urls = [url.strip() for url in image_srcset.split('\n')]
                    image_url = image_urls[1]
                    zoomed_image_url= image_urls[2:]
                except:image_srcset = None

                try:
                
                    # Appending Extracted data points in required column names
                    data_scraper.data['Brand'].append(product_brand)
                    data_scraper.data['Desc'].append(product_name)
                    data_scraper.data['DiscountPrice'].append(discounted_price)
                    data_scraper.data['OriginalPrice'].append(original_price)
                    data_scraper.data['DiscountPercentage'].append(discount_percentage)
                    data_scraper.data['ProductLink'].append(product_link)
                    data_scraper.data['DetailedDesc'].append(product_link.split("/")[-3].replace("-", " ").title()) # Extracting Detailed Description from link
                    data_scraper.data['Images'].append(image_url)
                    data_scraper.data['ZoomedImages'].append(zoomed_image_url)
                    # Getting Total Data Points
                    total_data_points += 1
                except Exception as e:
                    print(e)
            # Next Page
            data_scraper.driver.find_element(By.CSS_SELECTOR,"li.pagination-next").click()
            print(f"Progress: Page {j} || Data Collected: {50*(page_count)}\n-------------------------------------------------------")
            page_count += 1

            # Saving Data at given check point
            if total_data_points % data_scraper.check_point == 0:
                data_scraper.save_to_csv(scraper_config.csv_location, page=j,total_data_points=total_data_points),

                                                
except Exception as e:
    data_scraper.save_to_csv(scraper_config.csv_location,page=j, total_data_points=total_data_points)
    print(f"An error occurred: {e}")

finally:
    data_scraper.driver.close()



