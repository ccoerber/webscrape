import lxml
from lxml import etree
import requests
import time

def printProdInfo():
    
    prodid = 'B005MQRAAK'
    outfilename = prodid + '.csv'
    url = 'https://www.amazon.com/dp/' + prodid
    params= {'User-agent':'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.87 Safari/537.36'}

    outfile = open(outfilename, 'a')
    response = requests.get(url, headers=params)

    # parse html for product info
    tree = etree.HTML(response.content)
    elem = tree.xpath('//span[@id="priceblock_ourprice"]')
    if elem == None:
        strprice = "$0.00"
    else:
        print elem[0].text
        strprice = elem[0].text
    
    outfile.write(elem[0].text + '|')
    outfile.close()

if __name__ == "__main__":
    
    for i in range(1):
        printProdInfo()
        time.sleep(1)