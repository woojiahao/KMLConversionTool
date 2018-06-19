import os
from collections import OrderedDict

from bs4 import BeautifulSoup

from converter import Converter
from logger import Logger


class CSVConverter2(Converter):
	def __init__(self):
		self.__logger = Logger()
		self.__data = OrderedDict()

	def __extract_columns(self, soup: BeautifulSoup):
		columns = soup.find_all('SimpleField')
		for col in columns:
			self.__data[col.get('name')] = []

	def __extract_data(self, soup: BeautifulSoup):
		placemarks = soup.find_all('Placemark')
		for placemark in placemarks:
			extended_data = placemark.ExtendedData.SchemaData.find_all('SimpleData')
			for simple_data in extended_data:
				name: str = simple_data.get('name')
				val: str = '|'.join([data for data in simple_data.contents])
				if name in self.__data.keys():
					self.__data[name].append(val)

	def __consolidate_data(self):
		headers: str = ','.join(self.__data.keys())
		body: list = []
		for i in range(len(self.__data.values())):
			body.append(','.join([self.__data[key][i] for key in self.__data.keys()]))

		return '{}\n{}'.format(headers, '\n'.join(body))

	def __create_file(self, kml_url: str):
		prefix = kml_url.rfind('\\')
		if prefix != -1:
			kml_url = kml_url[prefix + 1:]

		csv_url = kml_url.replace('.kml', '.csv')
		try:
			destination_folder = os.path.expanduser('~\\Documents\\KMLConverter\\converted\\csv\\')
		except OSError:
			self.__logger.err('Error in converting file path')
		csv_url = '{}{}'.format(destination_folder, csv_url)

		if not os.path.exists(destination_folder):
			os.makedirs(destination_folder)

		with open(csv_url, 'w+') as new_file:
			new_file.write(self.__consolidate_data())

		self.__logger.suc('Successfully converted the file, you can find it at {}'.format(csv_url))

	def convert(self, file_url: str):
		file_url = file_url.replace('/', '\\')

		if self._is_convertable(file_url):
			soup = self._get_soup(file_url)
			self.__extract_columns(soup)
			self.__extract_data(soup)

			if len(self.__data) > 0:
				self.__create_file(file_url)
			else:
				self.__logger.info(
					'The target file does not contain any information that is suitable for a .csv file.')
		else:
			self.__logger.err('{} is invalid, please ensure that it is a .kml file that exists'.format(file_url))
