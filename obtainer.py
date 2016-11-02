import urllib2

class DataArray():
	# Initialization just sets up the system with the url given.
	def __init__(self, target_url):
		self.url = target_url
		self.available_files = []
		self.fullText = " "

		self.data = urllib2.urlopen(self.url)

		print "\n<========= Initializing Access File Method =========>\n"
		self.accessFiles()
		print "\n<========== Preparing for text extraction ==========>\n"
		self.fileExtraction()

	# Returns all of the files in the specified url.
	def getAllFiles(self):
		return self.available_files

	# Gets the text from all of the text files in the given url
	def fileExtraction(self):
		self.fullText = " "
		for file in self.available_files:
			setURL = self.url+"/"+file
			data = urllib2.urlopen(setURL)
			self.fullText = self.fullText+data
	# gets all of the available text files in the url
	def accessFiles(self):
		for line in self.data:
                        if ".txt" in line:
                                for word in line.split():
                                        if "txt" in word:
                                                txtFile=word[word.index('>')+1:len(word)-4]
						self.available_files.append([txtFile])
