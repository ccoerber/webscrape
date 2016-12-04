import lxml
from lxml import etree
import requests
import time
import datetime

def getHTMLTree(url):

    params= {'User-agent':'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.87 Safari/537.36'}
    response = requests.get(url, headers=params)
    tree = etree.HTML(response.content)
    return tree
     
def getElemText(tree, path):

    elem = tree.xpath(path)
    if elem is None:
        strval = "Not Found"
    else:
        strval = elem[0].text
        
    return strval.strip()
    
def printProdInfo(prodid):

    # parse html for product info
    url = 'https://www.amazon.com/dp/' + prodid
    tree = getHTMLTree(url)
    
    # time of request
    timeOfReq = datetime.datetime.today().ctime()
    print "Time of request: " + timeOfReq
    
    strprodtitle = getElemText(tree, '//span[@id="productTitle"]')
    print 'Product: ' + strprodtitle
    
    strprice = getElemText(tree, '//span[@id="priceblock_ourprice"]')
    print 'Price: ' + strprice
    
    outfilename = strprodtitle[0:10] + ' - ' + prodid + '.csv'
    outfile = open(outfilename, 'a')
    outfile.write(timeOfReq + '|' + strprice + '\n')
    outfile.close()

if __name__ == "__main__":
    
    freqInMin = 5 # num of minutes to wait between each request
    
    while (1):
        printProdInfo('B003S3RGJO')
        printProdInfo('B01AW1R5TU')
        
        # time.sleep() blocks keyboard interrupt (e.g. Ctrl+C). 
        # call time.sleep(1) multiple times to combat this
        for i in range(60*freqInMin):
            time.sleep(1)