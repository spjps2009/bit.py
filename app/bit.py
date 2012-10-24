import string 
import random

urlslist = {}
shorturlslist={}
def main():
	
	while True:
	    b = input("1.Url Shortner \n2.Quit\n")
	    if b==1:
		while True:
		    url = raw_input("Enter URL: ")
		    shortenedlength = input("Enter Length of Shortened URL: ")
		    if (checkurl(url) == True):
		        break
		    print 'Error! Try Again.'
		print shortenurl(url, shortenedlength)
	    elif b==2:
		break
	    else:
		break

def shortenurl(url, length):
    shortlist = []
    short=""
    if url in urlslist:
        return urlslist[url]
    for i in range(0, length):
        shortlist.append(random.choice(string.ascii_letters+ string.digits))
    shorturl = "www.urlshortner.com/" + short.join(shortlist)
    while shorturl in shorturlslist:
        for i in range(0, length):
            shortlist.append(random.choice(string.ascii_letters+ string.digits))
        shorturl = "www.urlshortner.com/" + short.join(shortlist)
    urlslist[url]=shorturl
    shorturlslist[shorturl]=url
    print urlslist, shorturlslist, "\n"
    return shorturl
    
def checkurl(url):
    if '.' in url and len(url) >3 :
        return True
    return False
    
if __name__ == '__main__':
	main()
