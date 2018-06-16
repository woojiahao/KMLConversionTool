def convert (file_url : str):
	# C:\Users\wooji\PycharmProjects\KMLConverter\data
	file_url = file_url.replace('/', '\\')
	print(file_url)


convert('data/dengue-cases-central-kml.kml')