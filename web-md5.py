
import requests, sys, time
from bs4 import BeautifulSoup
from pyfiglet import Figlet

custom_fig = Figlet(font='big')
print(custom_fig.renderText('MR. MD5'))
print("=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#")
print("# DEVELOPER: ARMAN HOSSAIN ANTU // ANTU1024                    #")
print("# TWITTER  : https://twitter.com/antu1024                      #")
print("# ABOUT IT : MR. MD5 is a Free MD5 Encrypt & Decrypt Tools     #")
print("# VERSION  : @1.0                                              #")
print("=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#")
print("")

print("=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#")
print("")
print("## HASH IS: ", sys.argv[1].lower())
print("")
print("=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#")
print("")
print("")
print("=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#")

def md5_gromweb(password):
    try:
        req = requests.get(url="https://md5.gromweb.com",params={"md5":password})
        source_code = req.content
        soup = BeautifulSoup(source_code,"html.parser")
        brute_text = soup.find_all("em",{"class":"long-content string"})
        plain_text = brute_text[0].text		
        print("[||] md5.gromweb.com ===> ", plain_text)
        print("=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#")
    except IndexError:

        print("[||] md5.gromweb.com ===> Hash Don't Found!")
        print("=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#")
    except requests.ConnectionError or requests.ConnectTimeout:
		
        print("[||] md5.gromweb.com ===> Connection Error!!!")
		
def hashcrack(password):
    try:
        req = requests.post(url="http://hashcrack.com",data={"auth":"8272hgt","hash":password,"string":"","Submit":"Submit"})
        source_code = req.content
        soup = BeautifulSoup(source_code,"html.parser")
        brute_text = soup.find_all("span",{"class":"hervorheb2"})
        plain_text = brute_text[0].text
        print("=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#")
        print("[||] hashcrack.com ===> {}\n{}", plain_text)
        print("=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#")
    except IndexError:
		
        print("[||] hashcrack.com ===> Hash Don't Found!")
        print("=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#")
    except requests.ConnectionError or requests.ConnectTimeout:
		
        print("[||] hashcrack.com ===> Connection Error!!!")
		
def copyright():
		print("")
		print("")
		print("=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#")
		print("")
		print("## Copyright 2020 © By ARMAN HOSSAIN ANTU // ANTU1024          #")
		print("")
		print("=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#") 



if __name__ == '__main__':
    try:
        hash_text = sys.argv[1].lower()
        md5_gromweb(hash_text)
        hashcrack(hash_text)
        copyright()
    except IndexError:
		
        print("Please, Entry A Hash Text!")
        print("=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#")
    except:
        print("")
