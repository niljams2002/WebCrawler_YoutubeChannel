import requests
import csv
from bs4 import BeautifulSoup

# Function to scrape Google search results
def scrape_google_results(query):
    url = f"https://www.google.com/search?q={query}&num=10000"

    # Set user-agent to avoid blocking by Google
    headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Safari/537.36'
    }

    response = requests.get(url, headers=headers)
    response.raise_for_status()

    soup = BeautifulSoup(response.text, 'html.parser')
    search_results = soup.find_all('div', class_='yuRUbf')

    links = []
    for result in search_results:
        link = result.a['href']
        links.append(link)

    return links

# Function to filter YouTube channel links
def filter_youtube_channels(links):
    youtube_channels = []
    for link in links:
        if 'youtube.com/channel/' in link:
            youtube_channels.append(link)

    return youtube_channels

# Function to write the results to CSV
def write_to_csv(links, filename):
    with open(filename, 'w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow(['YouTube Channel Links'])
        writer.writerows([[link] for link in links])

# Main function
def main():
    query = 'site:youtube.com openinapp.co'
    search_results = scrape_google_results(query)
    youtube_channels = filter_youtube_channels(search_results[:10000])
    write_to_csv(youtube_channels, 'youtube_channels.csv')
    print(f"Scraped {len(youtube_channels)} YouTube channel links and saved to 'youtube_channels.csv'.")

if __name__ == '_main_':
    main()