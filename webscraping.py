from bs4 import BeautifulSoup as soup
from urllib.request import urlopen as uopen

my_url = 'https://www.footlocker.co.uk/en/men/_air-max-95?shoesize=7'

client = uopen(my_url)
page = client.read()
client.close()

page_soup = soup(page, "html.parser")


grab_crep = page_soup.findAll("div",{"class":"fl-category--productlist--item"})

print("")

for crp in grab_crep:
    
    print(crp.a.span.string.replace(" - Men Shoes",""))
    print(crp.a.get('href'))
    print("")
    print("")
    



