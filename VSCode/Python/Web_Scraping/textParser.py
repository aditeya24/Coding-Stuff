import requests
from bs4 import BeautifulSoup

page = requests.get("https://donboscovaduthala.in/u.php?id=20200")
soup = BeautifulSoup(page.content, 'lxml')

name_element = soup.find(text="Class:").parent.parent.next_element.next_element.next_element

#print(name_element)
image = soup.find('img'.src)

print(image)
