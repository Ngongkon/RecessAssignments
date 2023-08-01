import csv
import requests
from bs4 import BeautifulSoup

def extract_bird_species(url):
    response = requests.get(url)
    if response.status_code == 200:
        bird_species_data = response.json().get('recordings')

        return bird_species_data
    else:
        print("Failed to fetch the webpage.")
        return None

def save_csv_file(data, file):
    if data:
        with open(file, 'w', newline='', encoding='utf-8') as csvfile:
            fieldnames = list(data[0].keys())
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerows(data)
        print(f"Dataset {file} successfully.")
    else:
        print("No data to save.")

if __name__ == "__main__":
    url = "https://xeno-canto.org/api/2/recordings?query=cnt:uganda"
    bird_species_data = extract_bird_species(url)
    if bird_species_data:
        save_csv_file(bird_species_data, "bird_species.csv")
