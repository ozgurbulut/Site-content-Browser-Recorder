import urllib
import urllib.request
from bs4 import BeautifulSoup

file = open("data.dat","w")

def call_data(url):

	page = urllib.request.urlopen(url)
	datas =BeautifulSoup(page,"html.parser")

	return datas

core_data = ""

searc_result = call_data("https://www.basketball-reference.com/players/b/")

for records in searc_result.findAll('tr'):
	for data in records.findAll('td'):
		core_data=core_data+" , "+data.text


file.write(core_data)
file.close()
