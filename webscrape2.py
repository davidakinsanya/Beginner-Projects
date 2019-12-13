from bs4 import BeautifulSoup as soup
from urllib.request import urlopen as uopen

my_url = 'https://www.footasylum.com/nike-air-max-95-trainers/?size=7&category=FM_SNEAKERS'

client = uopen(my_url)
page = client.read()
client.close()

page_soup = soup(page, "html.parser")

get_crep = page_soup.findAll("li",{"class":"left"})


print("")

try:
    for crp in get_crep:

        product = crp.p.text
        link = crp.span.text
        
        print(product)
        print(link)
        print("")

except:
    print("")
    print("All the AM95's on footasylum in size 7")


