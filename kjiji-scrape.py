from bs4 import BeautifulSoup
import requests as request
vergeShill = request.get('https://www.kijiji.ca/b-saskatchewan/bmw/k0l9009')
html = vergeShill.text
soup = BeautifulSoup(html, 'lxml')
kjijiSite = soup.text
startLocation = kjijiSite.find("Top Ads See All")
listings = kjijiSite[startLocation:]
listingsCollected = []

index = 0
for i in listings:
    index += 1
    newListing = ""
    if i == "$":
        nextListing = False
        k = index
        while nextListing is not True:
            if k == 42126:
                nextListing = True
            if listings[k] == "$":
                print(k)
                nextListing = True
            if listings[k] == " ":
                pass
            else:
                newListing += listings[k]
            k += 1
        listingsCollected.append(newListing)

textFile = open("scrape-results.txt", "w")
i = 0
for i in range(len(listingsCollected)):
    lines = listingsCollected[i].split()
    lines = [line for line in lines if line.strip()]
    for line in lines:
        line = line + '\n'
        textFile.write(line)
textFile.close()


