import os

import numpy as np
from bs4 import BeautifulSoup


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


def extract_data(soup: BeautifulSoup):
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


def create_file(kml_url: str, contents: str):
	prefix = kml_url.rfind('\\')
	if prefix != -1:
		kml_url = kml_url[prefix + 1:]

	csv_url = kml_url.replace('.kml', '.csv')
	destination_folder = os.path.expanduser('~\\Documents\\KMLConverter\\converted\\csv\\')
	csv_url = '{}{}'.format(destination_folder, csv_url)

	if not os.path.exists(destination_folder):
		os.makedirs(destination_folder)

	with open(csv_url, 'w+') as new_file:
		new_file.write(contents)


def convert(file_url: str):
	file_url = file_url.replace('/', '\\')

	if is_convertable(file_url):
		create_file(file_url, convert_file(file_url))
	else:
		print('{} is not in the right format, please ensure that it is a .kml file'.format(file_url))


convert('data/dengue-cases-central-kml.kml')
