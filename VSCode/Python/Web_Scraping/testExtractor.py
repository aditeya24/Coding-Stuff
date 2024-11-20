import requests
from bs4 import BeautifulSoup
import csv
import re

details_list = []

for x in range(17460,17484,4):
    y = str(x)
    z = int((x-17180)/4)
    url = "https://donboscovaduthala.in/u.php?id="+y

    page = requests.get(url)
    soup = BeautifulSoup(page.content, 'lxml')


    name = soup.find(text="Name of the Student:").parent.parent.next_element.next_element.next_element
    print(name)