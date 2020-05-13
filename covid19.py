import requests
from bs4 import BeautifulSoup
country=input("MASUKAN NAMA NEGARA:")
url="https://www.worldometers.info/coronavirus/country/{}/".format(country)
r=requests.get(url)
s=BeautifulSoup(r.text,"html.parser")
data=s.find_all("div",class_="maincounter-number")
print("""

  ___        __        ____                            
 |_ _|_ __  / _| ___  / ___|___  _ __ ___  _ __   __ _ 
  | || '_ \| |_ / _ \| |   / _ \| '__/ _ \| '_ \ / _` |
  | || | | |  _| (_) | |__| (_) | | | (_) | | | | (_| |
 |___|_| |_|_|  \___/ \____\___/|_|  \___/|_| |_|\__,_|
                                                       
""")

                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        
print("JUMLAH KASUS : ",data[0].text.strip())
print("JUMLAH KEMATIAN : ",data[1].text.strip())
print("JUMLAH KESEMBUHAN : ",data[2].text.strip())
print("""
---------------------------SELALU JAGA KESEHATAN DAN KEBERSIHAN ----------------------------------------  )
                                                __ooooooooo__
              oOOOOOOOOOOOOOOOOOOOOOo
          oOOOOOOOOOOOOOOOOOOOOOOOOOOOOOo
       oOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOo
     oOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOo
   oOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOo
  oOOOOOOOOOOO*  *OOOOOOOOOOOOOO*  *OOOOOOOOOOOOo
 oOOOOOOOOOOO      OOOOOOOOOOOO      OOOOOOOOOOOOo
 oOOOOOOOOOOOOo  oOOOOOOOOOOOOOOo  oOOOOOOOOOOOOOo
oOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOo
oOOOO     OOOOOOOOOOOOOOOOOOOOOOOOOOOOOOO     OOOOo
oOOOOOO OOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOO OOOOOOo
 *OOOOO  OOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOO  OOOOO*
 *OOOOOO  *OOOOOOOOOOOOOOOOOOOOOOOOOOOOO*  OOOOOO*
  *OOOOOO  *OOOOOOOOOOOOOOOOOOOOOOOOOOO*  OOOOOO*
   *OOOOOOo  *OOOOOOOOOOOOOOOOOOOOOOO*  oOOOOOO*
     *OOOOOOOo  *OOOOOOOOOOOOOOOOO*  oOOOOOOO*
       *OOOOOOOOo  *OOOOOOOOOOO*  oOOOOOOOO*      
          *OOOOOOOOo           oOOOOOOOO*      
              *OOOOOOOOOOOOOOOOOOOOO*          
                   ""ooooooooo""

--------------------STAY WITH ME YAHAHA HAIIIYUUKKK-----------------
""")
