import random
import urllib.request

def photo(url):
 name=random.randrange(1,1000)
 photo_name= str(name)+ '.png'
 urllib.request.urlretrieve(url, photo_name)

photo("https://upload.wikimedia.org/wikipedia/commons/f/f9/Phoenicopterus_ruber_in_S%C3%A3o_Paulo_Zoo.jpg")
 
 
 



