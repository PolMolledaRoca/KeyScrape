import requests
from bs4 import BeautifulSoup
import csv
import argparse

def scrape_website(url, keyword, output_file):
    try:
        response = requests.get(url)
        response.raise_for_status()
    except requests.exceptions.RequestException as e:
        print(f"Error fetching the webpage: {e}")
        return
    
    soup = BeautifulSoup(response.text, 'html.parser')
    
    matched_elements = []
    for element in soup.find_all(text=True):
        if keyword.lower() in element.lower():
            matched_elements.append(element.strip())
    
    with open(output_file, 'w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow(["Matched Content"])
        for item in matched_elements:
            writer.writerow([item])
    
    print(f"Scraping completed. Found {len(matched_elements)} matching elements. Data saved in {output_file}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Web Scraper to extract text based on a keyword from a webpage")
    parser.add_argument("url", help="URL of the webpage to scrape")
    parser.add_argument("keyword", help="Keyword to search for in the webpage")
    parser.add_argument("output", help="Output CSV file name", default="output.csv")
    
    args = parser.parse_args()
    scrape_website(args.url, args.keyword, args.output)
