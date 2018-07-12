#importing libraries
from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup
#url
my_url='https://www.amazon.in/s/ref=nb_sb_noss?url=search-alias%3Daps&field-keywords=earphones'
#Connecting with the url
uClient = uReq(my_url)
page_html = uClient.read()
uClient.close()
#Downloading url
page_soup = soup(page_html, "html.parser")
#Search for content
search = page_soup.find("span",{"id":"s-result-count"}).span.span.text.strip()
filename = "products.csv"
f = open(filename, "w")
headers = "Name , Brand, Amazon Price, MRP, Savings, Service, Ratings\n"
f.write(headers)
#grabs each product
containers = page_soup.findAll("div",{"class":"s-item-container"})
for container in containers:
	 product_name = container.h2["data-attribute"]
	 brand_name = container.span.next.next.text
	 amazon_price = container.find("span",{"class":"a-size-base a-color-price s-price a-text-bold"}).text.strip()
	 mrp = container.find("span",{"class":"a-size-small a-color-secondary a-text-strike"}).text.strip()
	 savings = container.find("span",{"class":"a-size-small a-color-price"}).text.strip().replace("\n","").replace(" ","")
	 service = container.find("span",{"class":"a-icon-alt"}).text
	 if service=="prime":
	 	service = "prime"
	 else:
	 	service = "regular"
	 ratings = container.find("a",{"class":"a-popover-trigger a-declarative"}).i.span.text
	 print("Product Name : " + product_name)
	 print("Brand Name : " + brand_name)
	 print("Amazon Price : " + amazon_price)
	 print("Original Price : " + mrp)
	 print("Total Savings : " + savings)
	 print("Service : " + service) 
	 print("Ratings : " + ratings + "\n\n")
	 f.write(product_name.replace(",","'") + "," + brand_name + "," + amazon_price.replace(",","'") + "," + mrp.replace(",","'") + "," + savings.replace(",","'") + "," + service + "," + ratings + "\n")
f.close()