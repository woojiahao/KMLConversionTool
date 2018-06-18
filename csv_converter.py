import os

import numpy as np
from bs4 import BeautifulSoup

from converter import Converter
from logger import Logger


class CSVConverter(Converter):
	def __init__(self):
		self.__logger = Logger()

	def __extract_columns(self, soup: BeautifulSoup):
		return [col.get('name') for col in soup.find_all('SimpleField')]

	def __extract_data(self, soup: BeautifulSoup):
		result = ''
		placemarks = soup.find_all('Placemark')
		for placemark in placemarks:
			extended_data = placemark.ExtendedData.SchemaData.find_all('SimpleData')
			rows = np.ndarray.flatten(np.array([data.contents for data in extended_data])).tolist()
			result += ','.join(rows)
			result += '\n'
		return result

	def __create_file(self, kml_url: str, contents: str):
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

		self.__logger.suc('Successfully converted the file, you can find it at {}'.format(csv_url))

	def __convert_file(self, file_url: str):
		soup = self._get_soup(file_url)
		return '{}\n{}'.format(','.join(self.__extract_columns(soup)), self.__extract_data(soup))

	def convert(self, file_url: str):
		file_url = file_url.replace('/', '\\')

		if self._is_convertable(file_url):
			contents = self.__convert_file(file_url)
			if contents.strip() != '':
				self.__create_file(file_url, contents)
		else:
			self.__logger.err('{} is invalid, please ensure that it is a .kml file that exists'.format(file_url))
