from bs4 import BeautifulSoup
from requests import get

def main():
    gold=get("https://www.tgju.org/").text
    soup = BeautifulSoup(gold, 'html.parser')
    dollar=soup.find("tr",{"data-market-row":"price_dollar_rl"}).find("td",{"class":"nf"}).text
    euro=soup.find("tr",{"data-market-row":"price_eur"}).find("td",{"class":"nf"}).text
    pond=soup.find("tr",{"data-market-row":"price_gbp"}).find("td",{"class":"nf"}).text
    gold_18_750=soup.find("tr",{"data-market-row":"geram18"}).find("td",{"class":"nf"}).text
    gold_24=soup.find("tr",{"data-market-row":"geram24"}).find("td",{"class":"nf"}).text
    gold_dast=soup.find("tr",{"data-market-row":"gold_mini_size"}).find("td",{"class":"nf"}).text
    gold_mesgal=soup.find("tr",{"data-market-row":"mesghal"}).find("td",{"class":"nf"}).text
    print(f"Gold_18_750 : {gold_18_750}\nGold_24 : {gold_24}\nGold_DastDo : {gold_dast}\nGold_Mesgal : {gold_mesgal}\nDollar : {dollar}\nEuro : {euro}\nPound : {pond}")
    
    
if __name__ == "__main__":
    main()