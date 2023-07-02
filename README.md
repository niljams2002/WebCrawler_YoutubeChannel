# YouTube Channel Web Crawler
This Python program is a web crawler that can scrape YouTube channel links from the first 10,000 results of a Google search. It utilizes the BeautifulSoup library to parse the search results page and extract the relevant links.

## Requirements
Python 3.x
requests library (pip install requests)
BeautifulSoup library (pip install beautifulsoup4)

## Usage
1. Clone the repository or download the source code.
2. Install the required libraries if they are not already installed. 
3. Open the main.py file in a text editor and modify the query variable in the main function if you want to search for a different term or website. The default query is set to 'site:youtube.com openinapp.co'.
4. Run the program 
5. The program will scrape the first 10,000 search results from Google and filter out the YouTube channel links. The filtered links will be saved to a CSV file named 'youtube_channels.csv' in the same directory as the program.

## Output
The program generates a CSV file named 'youtube_channels.csv' that contains the collected YouTube channel links. Each link is listed in a separate row under the column header 'YouTube Channel Links'.

