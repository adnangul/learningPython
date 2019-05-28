
import sys
from abc import ABC, abstractmethod

"""
    Test/Usage example
    run as  pyhton -i output_list_absract_class.py

    > from data_class_from_csv import read_file
    > data = read_file("Book1.csv")
    > formatter = TextTableFormatter(width=40)
    > print_list(data, ["name", "price"], formatter)  # you cna pass any attribute

    > csv_formatter = CSVTableFormatter()
    > print_list(data, ["name", "price"], csv_formatter)  # you cna pass any attribute

    > html_formatter = HTMLTableFormatter()
    > print_list(data, ["name", "price"], html_formatter)
"""

def print_list(list, attributes, formatter):
    if not isinstance(formatter, TableFormatter):
        raise TypeError("Formatter must be a type of TableFormatter")
    formatter.headings(attributes)

    for obj in list:
       row_values = [str(getattr(obj, attr_name)) for attr_name in attributes]
       formatter.row(row_values)


"""
class TableFormatter(object):
    def __init__(self, outfile=None):
        self.outfile = outfile
    
    def headings(self, headers):
        raise NotImplementedError

    def row(self, row_values):
        raise NotImplementedError

    The above impl will work, but below will raise error as soon as we try to instantiate class/sub-class without absract method, 
    try instantiating another table formatter on interactive session, it will complain about method before trying to invoke
"""

class TableFormatter(ABC):
    def __init__(self, outfile=None):
        self.outfile = outfile
    
    @abstractmethod
    def headings(self, headers):
        raise NotImplementedError

    @abstractmethod
    def row(self, row_values):
        raise NotImplementedError


class TextTableFormatter(TableFormatter):
    def __init__(self, outfile=None, width=10):
        if outfile == None :
            outfile = sys.stdout
        
        self.outfile = outfile
        self.width = width
    
    def headings(self, headers):
        for header in headers:
            print("{:>{}s}".format(header, self.width), end=" ", file=self.outfile)
        print(file=self.outfile)

    def row(self, row_values):
        for value in row_values:
            print("{:>{}s}".format(value, self.width), end=" ", file=self.outfile)

        print()


class CSVTableFormatter(TableFormatter):
    def headings(self, headers):
        print(",".join(headers))

    def row(self, row_values):
        print(",".join(row_values))



class HTMLTableFormatter(TableFormatter):
    #pass  # can be used to skip impl

    def headings(self, headers):
        print("<tr>", end="", file=self.outfile)
        for header in headers:
            print("<th>{}</th>".format(header), end="", file=self.outfile)
        
        print("</tr>", file=self.outfile)

    def row(self, row_values):
        print("<tr>", end="", file=self.outfile)
        for value in row_values:
            print("<td>{}</td>".format(value), end="", file=self.outfile)
        
        print("</tr>", file=self.outfile)


class TestTableFormatter(object):
    pass

class AnotherTableFormatter(TableFormatter):
    pass