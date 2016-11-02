

import urllib2
from obtainer import DataArray

print "<============== Files Available in news ==============>\n"
news = DataArray("http://www.textfiles.com/news")
print "\n"
print news.getAllFiles()

