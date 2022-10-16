from web3 import Web3
import json
import csv

RPC_URL = "https://cloudflare-eth.com/"
web3 = Web3(Web3.HTTPProvider(RPC_URL))

class EXCHANGE:
    def __init__(self,name, adress, api):
        self.name=name
        self.contract=web3.eth.contract(address = adress, abi=api)
        aprice= self.contract.functions.getReserves().call()
        self.price=aprice[1]/aprice[0]
    def __str__(self):
        return " 'name'={} , price={}".format(self.name, self.price)

def generatePairs(name1, name2, excahangeDataCSV):
    l=[]
    with open(excahangeDataCSV, 'r') as file:
        reader = csv.reader(file, delimiter = '^')
        for row in reader:
            l.append(EXCHANGE(row[0],row[1],row[2]))
    return l


def retrunBiggestDeviation(pairsList):
    jsonlist=[]
    for row in pairsList:
        l= generatePairs(row[0],row[1],row[0]+'_'+row[1]+'.csv')
        min=l[0]
        max=l[0]
        for el in l:
            if el.price < min.price:
                min = el
            if el.price > max.price:
                max=el
        jsonEl=json.dumps( {"Coin1":row[0], "Coin2":row[1], "maxPriceExchange":max.name, "maxPrice":max.price , "minPriceExchange":min.name, "minPrice":min.price , "deviation":max.price-min.price}  )
        jsonlist.append(jsonEl)
    return jsonlist

