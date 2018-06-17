from bs4 import BeautifulSoup
import numpy as np


def is_convertable(file_url: str):
	extension_position = file_url.rfind('.')
	if extension_position == -1:
		return False
	else:
		extension = file_url[extension_position + 1:]
		return extension == 'kml'


def get_soup(file_url: str):
	with open(file_url) as before_file:
		soup = BeautifulSoup(before_file, 'lxml-xml')

	return soup


def extract_columns(soup: BeautifulSoup):
	return [col.get('name') for col in soup.find_all('SimpleField')]


def extract_data(soup : BeautifulSoup):
	result = ''
	placemarks = soup.find_all('Placemark')
	for placemark in placemarks:
		extended_data = placemark.ExtendedData.SchemaData.find_all('SimpleData')
		rows = np.ndarray.flatten(np.array([data.contents for data in extended_data])).tolist()
		result += ','.join(rows)
		result += '\n'
	return result


def convert_file(file_url: str):
	contents = ''

	soup = get_soup(file_url)
	contents += ','.join(extract_columns(soup))
	contents += '\n'
	contents += extract_data(soup)

	return contents


def convert(file_url: str):
	file_url = file_url.replace('/', '\\')

	if is_convertable(file_url):
		converted = convert_file(file_url)
	else:
		print('{} is not in the right format, please ensure that it is a .kml file'.format(file_url))


convert('data/dengue-cases-central-kml.kml')
# convert('data/dengue-cases-central-kml')
# convert('test.xml')
