# Submitted By
# avinasharma9099@gmail.com
 

import requests
from bs4 import BeautifulSoup
import csv

class NASAEarthDataScraper:
    def __init__(self):
        self.base_url = "https://www.earthdata.nasa.gov/engage/open-data-services-and-software/api"
        self.output_file = "nasa_earth_data.csv"

    def scrape_data(self):
        # Sending a GET request to the NASA Earth Data website
        response = requests.get(self.base_url)

        if response.status_code == 200:
            # Parse the HTML content of the page
            soup = BeautifulSoup(response.text, "html.parser")
 
            data_elements = soup.select('p')

            # Extracting and processing the data as needed
            data_list = []
            for element in data_elements:
                if element.find('a', class_='anchors') is not None:
                    data_name = element.text.strip()
                    data_description = element.next_sibling.next_sibling.text.strip()
                    data_list.append([data_name, data_description])

            # Saving the data to a CSV file
            self.save_to_csv(data_list)
        else:
            print("Failed to fetch data from NASA Earth Data website.")

    def save_to_csv(self, data_list):
        with open(self.output_file, mode="w", newline="", encoding="utf-8") as file:
            writer = csv.writer(file)
            writer.writerow(["Data Name", "Data Description"])
            writer.writerows(data_list)

if __name__ == "__main__":
    scraper = NASAEarthDataScraper()
    scraper.scrape_data()
