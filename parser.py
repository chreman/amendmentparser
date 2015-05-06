#!/usr/bin/python
# -*- coding: utf-8 -*-

"""
The amendment document has to be saved in html first.
"""

__author__ = "Christopher Kittel"
__copyright__ = "Copyright 2015"
__license__ = "MIT"
__version__ = "0.2"
__maintainer__ = "Christopher Kittel"
__email__ = "web@christopherkittel.eu"



import config
from bs4 import BeautifulSoup
import glob
import re


class Amendment(object):
    """docstring for Amendment"""
    def __init__(self, target_text, amendment_text, author):
        #super(Amendment, self).__init__()
        self.target = get_target(target_text)
        self.target_text = target_text
        self.amendment_text = amendment_text
        self.deletion = check_for_deletion(amendment_text)
        self.author = author

    def __repr__(self):
        text = "This amendment is proposed by {0}.\nIt refers to part '{1}' of the original proposal.\n\
It replaces the following passage: \n\
{2} \n\
with \n\
{3}".format(self.author, self.target, self.target_text, self.amendment_text)
        return text


def main(document):
    """
    Takes an html-document as input,
    returns an iterator of amendment-objects.
    """
    doc = read_file(document)
    soup = soupify(doc)
    #print soup.prettify()
    authors = find_authors(soup)
    tables = find_tables(soup)
    for next_author, table in zip(authors, tables):

        try:
            author = get_text(next_author).encode("utf-8")
        except:
            author = next_author.encode("utf-8")
        cells = get_table_cells(table)
        target_text = get_text(cells[3]).encode("utf-8")
        if len(target_text) < 1:
            target_text = "New entry."
        amendment_text = get_text(cells[4]).encode("utf-8")


        yield Amendment(target_text, amendment_text, author)



def read_file(filename):
    """

    """
    with open(filename, "r") as infile:
        return infile.read()


def soupify(document):
    """
    Takes an html-document and returns a BeautifulSoup object.
    """
    return BeautifulSoup(document)


def find_tables(soup):
    return soup.body.findAll("table")

def get_table_cells(table):
    return table.findAll("td")


def get_text(element):
    return element.text


def get_target(target_text):
    if target_text:
        target = re.match(r"[A-Za-z0-9]?.", target_text)
        return target.group(0)

def check_for_deletion(amendment_text):
    if amendment_text == "deleted" or "delete":
        return True
    else:
        return False

def find_authors(soup):
    paragraphs = soup.body.findAll("p")
    for para in paragraphs:
        spans = para.findAll("span", {"class":"HideTWBExt"})
        for span in spans:
            if span.text == "<RepeatBlock-By><Members>":
                yield span.next_sibling
    

###    MAIN   ###


if __name__ == '__main__':
    main(config.datapath+"amendments280.html")