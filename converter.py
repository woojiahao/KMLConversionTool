from bs4 import BeautifulSoup


def is_convertable(file_url: str):
	extension_position = file_url.rfind('.')
	if extension_position == -1:
		return False
	else:
		extension: str = file_url[extension_position + 1:]
		return extension == 'kml'


def convert(file_url: str):
	file_url = file_url.replace('/', '\\')

	if is_convertable(file_url):
		with open(file_url) as before_file:
			soup = BeautifulSoup(before_file, 'lxml-xml')
	else:
		print('{} is not in the right format, please ensure that it is a .kml file'.format(file_url))

convert('data/dengue-cases-central-kml.kml')
convert('data/dengue-cases-central-kml')
convert('test.xml')
