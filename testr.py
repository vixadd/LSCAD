import urllib2

url="http://www.textfiles.com/news"
data = urllib2.urlopen(url)
for line in data:
	if ".txt" in line:
		for word in line.split():
			if "txt" in word:
				print word[word.index('>')+1:len(word)-4]
