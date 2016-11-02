#=======================================#
#					#
#	Obtainer to get textual data	#
#	  from a specific webpage.	#
#					#
#	    Author: davidkroell		#
#					#
#=======================================#

import urllib2
import sys

# Class to instantiate different websites and obtaining their textfiles.
class DataArray():

	# Initialization just sets up the system with the url given.
	def __init__(self, target_url):
		self.url = target_url
		self.available_files = []
		self.fullText = " "

		self.data = urllib2.urlopen(self.url)

		print "<========= Initializing Access File Method =========>\n"
		self.accessFiles()
		print "<========== Preparing for text extraction ==========>\n"
		print "	   _*_ Note: This may take a few momments"
		self.fileExtraction()

	# Returns all of the files in the specified url.
	def getAllFiles(self):
		return self.available_files

	# Gets the text from all of the text files in the given url
	def fileExtraction(self):

		self.fullText = ""
		i = 0
		printProgress(i, len(self.available_files), prefix = 'Progress:', suffix = 'Complete', barLength = 30)

		try:
			for file in self.available_files:
				setURL = self.url+"/"+str(file)
				dataLines = urllib2.urlopen(setURL)
				for line in dataLines:
					self.fullText = self.fullText+str(line)

				i = i+1
				printProgress(i, len(self.available_files), prefix = 'Progress:', suffix = 'Complete', barLength = 30)

		except KeyboardInterrupt:
			print "\n<================ File Extraction Terminated ==================>"
			sys.exit(0)

	# gets all of the available text files in the url
	def accessFiles(self):
		for line in self.data:
                        if ".txt" in line:
                                for word in line.split():
                                        if "txt" in word:
                                                txtFile=word[word.index('>')+1:len(word)-4]
						self.available_files.append(txtFile)


# Print iterations progress
def printProgress (iteration, total, prefix = '', suffix = '', decimals = 1, barLength = 100):
    formatStr       = "{0:." + str(decimals) + "f}"
    percents        = formatStr.format(100 * (iteration / float(total)))
    filledLength    = int(round(barLength * iteration / float(total)))
    bar             = '=' * filledLength + '-' * (barLength - filledLength)
    sys.stdout.write('\r%s |%s| %s%s %s' % (prefix, bar, percents, '%', suffix)),
    if iteration == total:
        sys.stdout.write('\n')
    sys.stdout.flush()
