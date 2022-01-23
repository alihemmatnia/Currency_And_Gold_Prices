#pip install bs4
#pip install requests
#pip install inputimeout

from bs4 import BeautifulSoup
from requests import get
import os
from inputimeout import inputimeout, TimeoutOccurred

class color:
    zero = '\033[94m'
    high = '\033[92m'
    low = '\033[93m'
    warning = '\033[1m'
    White = '\033[97m'

def getcolor(change_value):
    if change_value == ['low']:
        return color.low
    elif change_value == ['high']:
        return color.high
    else : 
        return color.zero

def getspace(value,space_int,character):
    space = ""
    range_int = int(space_int)-len(value)
    for n in range(range_int):
        space += character
    return space

def main():
    gold=get("https://www.tgju.org/").text
    soup = BeautifulSoup(gold, 'html.parser')

    bitcoin = [soup.find("li",{"id":"l-crypto-bitcoin"}).find("span",{"class":"info-value"}).find("span",{"class":"info-price"}).text,
    soup.find("li",{"id":"l-crypto-bitcoin"}).find("span",{"class":"info-change"}),
    soup.find("li",{"id":"l-crypto-bitcoin"}).get("class")]

    dollar=[soup.find("tr",{"data-market-row":"price_dollar_rl"}).find("td",{"class":"nf"}).text,
    soup.find("tr",{"data-market-row":"price_dollar_rl"}).find_all("td")[1].find("span")]
    
    euro=[soup.find("tr",{"data-market-row":"price_eur"}).find("td",{"class":"nf"}).text,
    soup.find("tr",{"data-market-row":"price_eur"}).find_all("td")[1].find("span")]

    pond=[soup.find("tr",{"data-market-row":"price_gbp"}).find("td",{"class":"nf"}).text,
    soup.find("tr",{"data-market-row":"price_gbp"}).find_all("td")[1].find("span")]
    
    gold_18_750=[soup.find("tr",{"data-market-row":"geram18"}).find("td",{"class":"nf"}).text,
    soup.find("tr",{"data-market-row":"geram18"}).find_all("td")[1].find("span")]

    gold_24=[soup.find("tr",{"data-market-row":"geram24"}).find("td",{"class":"nf"}).text,
    soup.find("tr",{"data-market-row":"geram24"}).find_all("td")[1].find("span")]

    gold_dast=[soup.find("tr",{"data-market-row":"gold_mini_size"}).find("td",{"class":"nf"}).text,
    soup.find("tr",{"data-market-row":"gold_mini_size"}).find_all("td")[1].find("span")]

    gold_mesgal=[soup.find("tr",{"data-market-row":"mesghal"}).find("td",{"class":"nf"}).text,
    soup.find("tr",{"data-market-row":"mesghal"}).find_all("td")[1].find("span")]
    print(f"""
-[    Name    ]-[Exchange Rate]{getspace("[Exchange Rate]",17,"-")}[---------   Change   ---------]
{getcolor(gold_18_750[1].get("class"))}| Gold_18_750 : {gold_18_750[0]} R{getspace(gold_18_750[0],16," ")}{gold_18_750[1].text}{getspace(gold_18_750[1].text,17," ")}<--> {gold_18_750[1].get("class")}
{getcolor(gold_24[1].get("class"))}| Gold_24     : {gold_24[0]} R{getspace(gold_24[0],16," ")}{gold_24[1].text}{getspace(gold_24[1].text,17," ")}<--> {gold_24[1].get("class")}
{getcolor(gold_dast[1].get("class"))}| Gold_DastDo : {gold_dast[0]} R{getspace(gold_dast[0],16," ")}{gold_dast[1].text}{getspace(gold_dast[1].text,17," ")}<--> {gold_dast[1].get("class")}
{getcolor(gold_mesgal[1].get("class"))}| Gold_Mesgal : {gold_mesgal[0]} R{getspace(gold_mesgal[0],16," ")}{gold_mesgal[1].text}{getspace(gold_mesgal[1].text,17," ")}<--> {gold_mesgal[1].get("class")}
{getcolor(dollar[1].get("class"))}| Dollar      : {dollar[0]} R{getspace(dollar[0],16," ")}{dollar[1].text}{getspace(dollar[1].text,17," ")}<--> {dollar[1].get("class")}
{getcolor(euro[1].get("class"))}| Euro        : {euro[0]} R{getspace(euro[0],16," ")}{euro[1].text}{getspace(euro[1].text,17," ")}<--> {euro[1].get("class")}
{getcolor(pond[1].get("class"))}| Pound       : {pond[0]} R{getspace(pond[0],16," ")}{pond[1].text}{getspace(pond[1].text,17," ")}<--> {pond[1].get("class")}
{getcolor(bitcoin[2])}| BitCoin     : {bitcoin[0]} ${getspace(bitcoin[0],16," ")}{bitcoin[1].text}{getspace(bitcoin[1].text,17," ")}<--> {bitcoin[2]}
{color.White}| ------------------------>
| Exit : Q  Reload:R """)
    

def runapp():
    main()
    try:
        input_text = inputimeout(prompt='| >>', timeout=20)
    except TimeoutOccurred:
        os.system("cls")
        runapp()
    try:
        if input_text == "r" or input_text == "R":
            os.system("cls")
            runapp()
        elif  input_text == "q" or input_text == "Q":
            exit
        else:
            runapp()
    except: pass

if __name__ == "__main__":
    os.system("cls")
    runapp()
    
