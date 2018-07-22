# KML to CSV Converter
The application currently has only been tested and should only work on a windows system, support for other OSs will be included in due time

Check out my blog post about my experience making this converter: [Blog Post](https://woojiahao.github.io/blog/2018-06-20/Learning-About-KML)
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

### Using the GUI
1. Ensure that you have all the libraries needed downloaded
2. Navigate to the folder with the file `main_window.py`
3. Run the file and the GUI will appear
4. Select the file that you want to convert
5. Select the convert options
6. Press the convert button
7. You will see a confirmation message if there were no conversion errors

```bash
cd KMLConverter/
ls
python main_window.py
```
