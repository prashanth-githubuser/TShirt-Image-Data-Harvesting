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

For each specified time interval, the accumulated information is archived under a uniquely named CSV filename structured as illustrated:

```
tshirt_{date}_pg{page_number}_cp{check_point}.csv
title_{date}_PageNo_{last_processed_page}.csv
```

## Recovering From Interruptions

Should the web scraper experience an abrupt halt prior to accomplishing designated objectives, jot down the final productively handled page number. Thereafter, update the script to proceed with gathering residual information beginning from the subsequent untouched page pursuant to the documented checkpoint. Ultimately, merge fragmented data acquired throughout disparate instances into a coherent conclusive compilation.

## Resumption Process

Assume the scenario wherein the scraper ceases operation at `pg50_cp_2500`, undertake remediation steps as demonstrated below:

```python
# configuration.py
from dataclasses import dataclass

@dataclass
class ScraperConfig:
    '''URL Works only for myntra.com domain'''
    
    URL = "https://www.myntra.com/men-tshirts"
    page_from: int = 51
    page_to: int = 1000
    check_point: int = 500
    csv_location: str = r'D:\Python\Test\selenium\artifacts'
```

## Ethical Considerations

Exercise caution and maintain responsibility regarding usage since this scraper serves solely academic interests and must comply strictly with the targeted site's Terms of Service.
