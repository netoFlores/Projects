import re
import urllib2

#a = r'<p>(.*)</p>)'

def patron(etiquetas, texto):
	patron = re.compile(etiquetas)
	find_text = patron.search(texto)
	if not find_text:
		return ''
	return find_text.group(1)

def coleccion_tags(url):
	collection = {}
	try:
		for file in url:
			#print file 
			web = urllib2.urlopen(file)
			text = web.read()
			web.close()
			collection[file] = {}
			collection[file]['tags'] = {}
			collection[file]['tags']['title'] = patron('<title>(.*)</title>', text)
			collection[file]['tags']['p'] = patron('<p> (.*)</p>', text)
	except urllib2.URLError, e:
		print e.reason
	return collection

url = ['http://google.com', 'http://facebook.com', 'http://twitter.com', 'http://ugb.edu.sv', 'http://elsalvador.com', 'http://as.com', 'http://marca.com', 'http://www.elfaro.net/']

coleccion = coleccion_tags(url)
#print coleccion
for i in coleccion:
	#print coleccion[i]
	print ':' * 80
	print coleccion[i]['tags']['title']
	print '-' * 80
	print coleccion[i]['tags']['p']
	print ':' * 80

