from bs4 import BeautifulSoup
import requests

#setting url variable to the url of a graphics card on newegg
url = "https://www.newegg.com/gigabyte-geforce-rtx-3080-ti-gv-n308tgaming-oc-12gd/p/N82E16814932436?Description=gigabyte%20rtx%203080%20ti&cm_re=gigabyte_rtx%203080%20ti-_-14-932-436-_-Product"

#setting result variable to use the requests.get method and passing in the url variable argument
result = requests.get(url)

#setting the doc variable to be used in the find_all method
doc = BeautifulSoup(result.text, "html.parser")

#setting the find_all to look for the $ tag, the first one that returns is the price
prices = doc.find_all(text="$")

#setting parent variable to jump to the parent html of the of $
parent = prices[0].parent
strong = parent.find("strong")

#adding the sup variable - sup is the parent of the .99 cents of the price
sup = parent.find("sup")

#manually printing $, while concatenating the values that return the whole dollar amount + the value of cents
print("The current price for the Gigabyte RTX 3080ti is:")
print("$" + strong.string + sup.string)






