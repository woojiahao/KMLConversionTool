from bs4 import BeautifulSoup

def convert (file_url : str):
	file_url = file_url.replace('/', '\\')

	with open(file_url) as before_file:
		soup = BeautifulSoup(before_file, 'lxml-xml')
		print(soup.prettify())



convert('data/dengue-cases-central-kml.kml')