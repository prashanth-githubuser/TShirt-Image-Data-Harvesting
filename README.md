 # TShirt-Image-Data-Harvesting

The TShirt-Image-Data-Harvesting application employs web scraping techniques to amass images of T-shirts, thereby generating a versatile dataset for applications encompassing image analysis, machine learning, and e-commerce visualization.

## Overview

This Python-based web scraper targets Myntra's men's t-shirts section and navigates through several pages, gathers assorted data points, and saves the collated data into a CSV file utilizing the Selenium library.

### Folder Structure

The project folder hierarchy appears as follows:

    project_root/
    ├── components/
    │   ├── scraper_pipeline.py
    │   └── streamlit_app.py
    ├── config/
    │   └── configuration.py
    ├── research/
    │   └── trial.ipynb
    ├── utils/
    │   └── web_scraper.py
    └── scrapper.py

## Setup

To prepare for execution, fine-tune the configurations found in `configuration.py`:

```python
# configuration.py
from dataclasses import dataclass

@dataclass
class ScraperConfig:
    '''URL Works only for myntra.com domain'''
    
    URL = "https://www.myntra.com/men-tshirts"
    page_from: int = 1
    page_to: int = 1000
    check_point: int = 500
    csv_location: str = r'D:\Python\Test\selenium\artifacts'
```

## Execution

Launch the scraper by executing the `scrapper.py` script as displayed below:

```perl
python path/to/scrapper.py
```

Upon completion of execution, observe snapshots displaying Sample\_1 and Sample\_2 showcases.

## Output Format

 Based on the provided naming conventions for the generated CSV files, there seem to be two types of filenames used depending upon the content stored within the respective files. Let's understand what they represent:

**First Filename Convention:**

* `tshirt_{date}_pg{page_number}_cp{check_point}.csv`
	+ `tshirt_` - Denotes the type of items being scraped (T-shirts).
	+ `{date}` - Represents the date when the data was scraped.
	+ `pg{page_number}` - Indicates which page the scraper had reached.
	+ `cp{check_point}` - Shows the checkpoint where the scraper had completed processing.

An example of this convention would be something like this:

* `tshirt_2023-03-21_pg50_cp2500.csv`

This indicates that the scraper successfully processed the first 50 pages until reaching the checkpoint at 2500 before encountering an issue or requiring manual intervention.

**Second Filename Convention:**

* `title_{date}_PageNo_{last_processed_page}.csv`
	+ `title_` - Signifies the nature of the contents inside the file (titles of products).
	+ `{date}` - Represents the date when the data was scraped.
	+ `PageNo_{last_processed_page}` - Demonstrates which page contained the last successful record before termination.

An instance of this convention could appear like this:

* `title_2023-03-21_PageNo_50.csv`

This signifies that the scraper managed to extract titles from the first 50 pages but encountered issues afterward, leading to its stoppage.

When handling interrupted sessions, you need to take note of both the current page numbers and the checkpoints mentioned in the filenames. Merge the fragments based on consistent column structures, ensuring no duplicates exist, resulting in a complete dataset containing all scraped records.

## Recovering From Interruptions

 To recover from interruptions and resume the scraper after it has stopped at a certain point, here are some simplified steps to follow:

1. Identify the last processed page number before the interruption occurred. In the given example, let's assume the scraper stopped at page 50 (pg50).
2. Update the `ScraperConfig` class definition in the `configuration.py` file. Change the value of the `page_from` parameter to start collecting data from the next unvisited page. In this case, change `page_from: int = 1` to `page_from: int = 51`. The updated code should look like this:
   ```python
   @dataclass
   class ScraperConfig:
       '''URL Works only for myntra.com domain'''
       
       URL = "https://www.myntra.com/men-tshirts"
       page_from: int = 51  # Changed this value
       page_to: int = 1000
       check_point: int = 500
       csv_location: str = r'D:\Python\Test\selenium\artifacts'
   ```
3. After updating the configuration, re-run the `scrapper.py` file to collect the remaining data starting from the updated page number.
4. When merging the data from different instances, ensure consistency in column names and order. If needed, process the individual CSV files first to standardize the structure before combining them into a single comprehensive dataset.

By following these simple steps, you can efficiently handle unexpected interruptions during the scraping process and continue the collection seamlessly. Just remember to document the stopping point and adjust the configuration accordingly before restarting the scraper.

## Ethical Considerations

Exercise caution and maintain responsibility regarding usage since this scraper serves solely academic interests and must comply strictly with the targeted site's Terms of Service.
