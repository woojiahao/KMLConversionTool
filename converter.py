import os

from bs4 import BeautifulSoup


class Converter:
	def _is_convertable(self, file_url: str):
		extension_position = file_url.rfind('.')

		if not os.path.exists(file_url):
			return False

		if extension_position == -1:
			return False
		else:
			extension = file_url[extension_position + 1:]
			return extension == 'kml'

	def _get_soup(self, file_url: str):
		with open(file_url) as before_file:
			soup = BeautifulSoup(before_file, 'lxml-xml')

		return soup
