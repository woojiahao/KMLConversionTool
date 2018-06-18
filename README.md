# KML to CSV Converter
The application currently has only been tested and should only work on a windows system, support for other OSs will be included in due time
## Description
### What is this?
This is a KML converter that uses libraries like [BeautifulSoup](https://www.crummy.com/software/BeautifulSoup/bs4/doc) and [TkInter](https://wiki.python.org/moin/TkInter).

It aims to be able to convert KML files to other file types like CSV or to simply extract the coordinates part of the KML file.
### Why make it?
I needed it for a school project that needed to analyse .csv files and thought it would be fun to take this opportunity to learn about GUI programming in Python.

## Usage Guide
### Pre-requisites
1. [BeautifulSoup](https://www.crummy.com/software/BeautifulSoup/bs4/doc/#installing-beautiful-soup)
2. [lxml](http://lxml.de/installation.html)

#### Note that the file will be saved to the folder ~/Documents/KMLConverter/converted

### To use the application, download the repository and run it using an IDE like PyCharm or Jupyter Notebook (untested), I will be adding support to launch this as an .exe or perhaps as a normal script in due time.

### ~~Using the GUI~~
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
