# KML to CSV Converter
## Description
### What is this?
This is a KML converter that uses libraries like [BeautifulSoup](https://www.crummy.com/software/BeautifulSoup/bs4/doc) and [PyQt4](https://pypi.org/project/PyQt4/).

It aims to be able to convert KML files to other file types like CSV or to simply extract the coordinates part of the KML file.
### Why make it?
I needed it for a school project that needed to analyse .csv files and thought it would be fun to take this opportunity to learn about PyQt.

## Usage Guide
### Pre-requisites
1. [BeautifulSoup](https://www.crummy.com/software/BeautifulSoup/bs4/doc/#installing-beautiful-soup)
2. [PyQt4](https://riverbankcomputing.com/software/pyqt/download)
3. [lxml](http://lxml.de/installation.html)

#### Note that the file will be saved to the folder ~/Documents/KMLConverter/converted

### Using the GUI
1. Navigate to the folder with the file `main_window.py`
2. Run the file and the GUI will appear
3. Select the file that you want to convert
4. Select the convert options
5. Press the convert button
6. You will see a confirmation message if there were no conversion errors

```bash
cd KMLConverter/
ls
python main_window.py
```
