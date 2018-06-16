from bs4 import BeautifulSoup


def is_convertable(file_url: str):
	extension_position : int = file_url.rfind('.')
	if extension_position == -1:
		return False
	else:
		extension: str = file_url[extension_position + 1:]
		return extension == 'kml'


def convert_file (file_url : str):
	with open(file_url) as before_file:
		soup: BeautifulSoup = BeautifulSoup(before_file, 'lxml-xml')
		columns: list = soup.find_all('SimpleField')

		print(columns)


def convert(file_url: str):
	file_url = file_url.replace('/', '\\')

	if is_convertable(file_url):
		convert_file(file_url)
	else:
		print('{} is not in the right format, please ensure that it is a .kml file'.format(file_url))

convert('data/dengue-cases-central-kml.kml')
convert('data/dengue-cases-central-kml')
convert('test.xml')
