#pip install bs4
#pip install requests
#pip install inputimeout

from bs4 import BeautifulSoup
from requests import get
import os
from inputimeout import inputimeout, TimeoutOccurred


def getspace(value,space_int,character):
    space = ""
    range_int = int(space_int)-len(value)
    for n in range(range_int):
        space += character
    return space

def main():
    gold=get("https://www.tgju.org/").text
    soup = BeautifulSoup(gold, 'html.parser')

    dollar=[soup.find("tr",{"data-market-row":"price_dollar_rl"}).find("td",{"class":"nf"}).text,
    soup.find("tr",{"data-market-row":"price_dollar_rl"}).find_all("td")[1].text]
    
    euro=[soup.find("tr",{"data-market-row":"price_eur"}).find("td",{"class":"nf"}).text,
    soup.find("tr",{"data-market-row":"price_eur"}).find_all("td")[1].text]

    pond=[soup.find("tr",{"data-market-row":"price_gbp"}).find("td",{"class":"nf"}).text,
    soup.find("tr",{"data-market-row":"price_gbp"}).find_all("td")[1].text]
    
    gold_18_750=[soup.find("tr",{"data-market-row":"geram18"}).find("td",{"class":"nf"}).text,
    soup.find("tr",{"data-market-row":"geram18"}).find_all("td")[1].text]

    gold_24=[soup.find("tr",{"data-market-row":"geram24"}).find("td",{"class":"nf"}).text,
    soup.find("tr",{"data-market-row":"geram24"}).find_all("td")[1].text]

    gold_dast=[soup.find("tr",{"data-market-row":"gold_mini_size"}).find("td",{"class":"nf"}).text,
    soup.find("tr",{"data-market-row":"gold_mini_size"}).find_all("td")[1].text]

    gold_mesgal=[soup.find("tr",{"data-market-row":"mesghal"}).find("td",{"class":"nf"}).text,
    soup.find("tr",{"data-market-row":"mesghal"}).find_all("td")[1].text]
    space = "     "
    print(f"""
-[    Name    ]-[Exchange Rate]{getspace("[Exchange Rate]",16,"-")}[  Change  ]

| Gold_18_750 : {gold_18_750[0]}{getspace(gold_18_750[0],16," ")}{gold_18_750[1]}
| Gold_24     : {gold_24[0]}{getspace(gold_24[0],16," ")}{gold_24[1]}
| Gold_DastDo : {gold_dast[0]}{getspace(gold_dast[0],16," ")}{gold_dast[1]}
| Gold_Mesgal : {gold_mesgal[0]}{getspace(gold_mesgal[0],16," ")}{gold_mesgal[1]}
| Dollar      : {dollar[0]}{getspace(dollar[0],16," ")}{dollar[1]}
| Euro        : {euro[0]}{getspace(euro[0],16," ")}{euro[1]}
| Pound       : {pond[0]}{getspace(pond[0],16," ")}{pond[1]}

| Exit : Q  Reload:R """)
    


def runapp():
    main()
    try:
        input_text = inputimeout(prompt='>>', timeout=10)
    except TimeoutOccurred:
        os.system("cls")
        runapp()
    if input_text == "q" or input_text == "Q":
        exit
    if input_text == "r" or input_text == "R":
        os.system("cls")
        runapp()

if __name__ == "__main__":
    runapp()
    
