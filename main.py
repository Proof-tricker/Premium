import os,platform
print('[+] Whatsapp Join ')
os.system('xdg-open https://chat.whatsapp.com/LB2ucS3nw2z31ENTQnUCZq')
BXI=platform.architecture()[0]
if BXI=="32bit":
    __import__("Premium32")

elif BXI=="64bit":
    __import__("Premium64")
