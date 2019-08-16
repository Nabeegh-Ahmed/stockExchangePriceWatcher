import requests
from bs4 import BeautifulSoup
from datetime import datetime

from apscheduler.schedulers.blocking import BlockingScheduler

tickers = ["MLCF", "HBL", "UBL", "PSO", "HCAR"]

def priceLister():
    now = datetime.now()
    current_time = now.strftime("%H:%M:%S")
    stockPrices = open(current_time + ".txt", "x")

    for ticker in tickers:
        requestLink = "https://dps.psx.com.pk/company/" + ticker
        request = requests.get(requestLink)
        content = request.content
        soup = BeautifulSoup(content, "html.parser")
        element  = soup.find("div", {"class": "quote__close"})
        listOfPrices = ticker + " : " + element.text.strip()
        stockPrices.write(listOfPrices + "\n")
    
    stockPrices.close()

if __name__ == '__main__':
    scheduler = BlockingScheduler()
    scheduler.add_job(priceLister, 'interval', seconds=60)
    scheduler.start()
