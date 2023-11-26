import pyshorteners

url = input("Enter url : ")
s = pyshorteners.Shortener()
print(f"Short Url :  {s.tinyurl.short(url)}")