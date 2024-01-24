from dataclasses import dataclass
from pathlib import Path

@dataclass
class Scrapper_Config:
    '''URL Works only for myntra.com domain'''
    
    URL= "https://www.myntra.com/men-tshirts"
    page_from: int = 2371
    page_to: int = 2470
    check_point: int = 500
    csv_location: str = r'D:\Python\Test\selenium\artifacts'


@dataclass
class Analysis_Cleaning_Config:
    artifact_dir: Path = Path(r'D:\Python\Test\selenium\artifacts')
    metadata_file_dir: Path = Path(r'D:\Python\Test\selenium\artifacts\metadata')


@dataclass
class Image_Extraction_Config:
    from_url: str = ''
    from_metadata_file: str = None
    # Enter index range if required
    from_index: int = None
    to_index: int = None
    image_output_path: Path = r'D:\Python\Test\selenium\artifacts\images'
    from_metadata: Path =  Path(r'D:\Python\Test\selenium\artifacts\metadata\cleaned_metadata')
    