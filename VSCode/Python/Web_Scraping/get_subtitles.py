# Import Required Module
import requests
from bs4 import BeautifulSoup

# Web URL
Web_url = "https://www.opensubtitles.org/en/search/sublanguageid-all/imdbid-tt0052077/sort-7/asc-0"

# Get URL Content
r = requests.get(Web_url)

# Parse HTML Code
soup = BeautifulSoup(r.content, 'html.parser')
print(soup.prettify())
