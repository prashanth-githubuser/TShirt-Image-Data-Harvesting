from dataclasses import dataclass

@dataclass
class Scrapper_Config:
    '''URL Works only for myntra.com domain'''
    
    URL= "https://www.myntra.com/men-tshirts"
    page_from: int = 1
    page_to: int = 1000
    check_point: int = 500
    csv_location: str = r'D:\Python\Test\selenium\artifacts'
