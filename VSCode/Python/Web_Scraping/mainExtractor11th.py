import requests
from bs4 import BeautifulSoup
import csv
import re

details_list = []

for x in range(17181,17485,4):
    y = str(x)
    z = int((x-17180)/4)
    url = "https://donboscovaduthala.in/u.php?id="+y

    page = requests.get(url)
    soup = BeautifulSoup(page.content, 'lxml')

    all_details = []

    name = soup.find(text="Name of the Student:").parent.parent.next_element.next_element.next_element
    std = soup.find(text="Class:").parent.parent.next_element.next_element.next_element
    division = soup.find(text="Class:").parent.parent.next_element.next_element.next_element.next_element.next_element.next_element
    id = soup.find(text="ID No:").parent.parent.next_element.next_element.next_element

    all_details.append({
        "name": name,
        "class": std,
        "division": division,
        "id": id,
        "url id": x
    })

    details_list.append(all_details)

    z = z+1

a = z 
keys = details_list[0][0].keys()

with open('details.csv', 'w', newline='') as output_file:
    dict_writer = csv.DictWriter(output_file, keys)
    dict_writer.writeheader()
    for z in range(a):
        dict_writer.writerows(details_list[z])
