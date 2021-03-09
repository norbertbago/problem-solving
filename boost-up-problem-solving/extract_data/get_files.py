import requests
from bs4 import BeautifulSoup
import os.path

save_path = './files'

url = "https://www.udemy.com/course/python-for-beginner/"
webpage_data = requests.get(url)

webpage = webpage_data.content
soup = BeautifulSoup(webpage, "html.parser")

mydivs = soup.find_all("span", {"class": "section--item-title--2k1DQ"})
count = 0

for i in mydivs[7:]:
    name = i.string.replace("-"," ")

    comment = "# Problem Solving Challange: {}".format(name)
    file_name = name.lower().replace(" ", "_")
    print(file_name)
    print(comment)

    complete_file_name = os.path.join(save_path, file_name + ".py")

    f = open(complete_file_name, "w")
    f.write(comment)
    f.close()
