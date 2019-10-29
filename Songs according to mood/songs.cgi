#!/usr/bin/python3
import numpy
import cgi
import cgitb # to show Common error in web browser cgiTraceBack

import googlesearch

cgitb.enable()

print("Content-type:text/html")
print("")

webdata = cgi.FieldStorage() #This will collect all the HTML code with data

#Now Extracting Value of x

mymood = webdata.getvalue('mood')
mysonglist=[]

for url in googlesearch.search_videos(mymood,stop=11):
        #url = url.replace("watch","embed")
        mysonglist.append(url)

songnum = numpy.random.random_integers(1,10)

print('<html>')

print('  <head>')

print('    <meta http-equiv="refresh" content="0;url='+mysonglist[songnum]+'" />')

print('  </head>')

print('</html>')
