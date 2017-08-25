from bs4 import BeautifulSoup
import requests as request
import re
kjijiSite = request.get('https://www.kijiji.ca/b-saskatchewan/bmw/k0l9009')
html = kjijiSite.text
soup = BeautifulSoup(html, 'lxml')
kjijiSite = soup.text
startLocation = kjijiSite.find("Top Ads See All")
endLocation = kjijiSite.find("Page:")
listings = kjijiSite[startLocation:endLocation]
listingsCollected = []

index = 0
for i in listings:
    index += 1
    newListing = ""
    if i == "$":
        nextListing = False
        k = index
        while nextListing is not True:
            if k == 11652:
                nextListing = True
            if listings[k] == "$":
                nextListing = True
            else:
                newListing += listings[k]
            k += 1
        listingsCollected.append(newListing)

textFile = open("scrape-results.txt", "w")
finalAds = []
for lines in listingsCollected:
    newListing = '$'
    for line in lines:
        re.sub(' +', ' ', line)
        if line == '\n':
            pass
        else:
            newListing += line
    newListingList = list(newListing)
    for i in range(len(newListingList)):
        if i + 1 != len(newListingList) and newListingList[i] + newListingList[i + 1] == "  ":
            newListingList[i] = ''
    finalListing = ''.join(newListingList)
    finalAds.append(finalListing)
for ads in finalAds:
    textFile.write('\n' + ads)
textFile.close()


