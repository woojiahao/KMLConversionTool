# KML to CSV Converter
## Description
### What is this?
This is a KML to CSV converter that uses libraries like [BeautifulSoup](https://www.crummy.com/software/BeautifulSoup/bs4/doc) and [PyQt4](https://pypi.org/project/PyQt4/).
### Why make it?
I needed it for a school project that needed to analyse .csv files and thought it would be fun to take this opportunity to learn about PyQt.

## Usage Guide
### Pre-requisites
1. [BeautifulSoup](https://www.crummy.com/software/BeautifulSoup/bs4/doc/#installing-beautiful-soup)
2. [PyQt4](https://riverbankcomputing.com/software/pyqt/download)
3. [lxml](http://lxml.de/installation.html)

### Using the CLI
1. Navigate to the folder with the file `converter.py`
2. Run the method `convert(file_url)` replaced `file_url` with the intended file name
#### Note that the file will be saved to the folder C:\\Documents

```bash
cd KMLConverter/
ls
python -c 'import converter; convert(test.kml)'
```

### Using the GUI
1. Navigate to the folder with the file `main_window.py`
2. Run the file and the GUI will appear
3. Select the file that you want to convert
4. Press the convert button
5. You will see a confirmation message if there were no conversion errors

```bash
cd KMLConverter/
ls
python main_window.py
```
