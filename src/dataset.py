#! /usr/bin/python
# *-* coding: utf-8 *-*

import xlrd

class Dataset:
    """ A class that to load data from specified spreadsheet. """

    def __init__(self):
        ds = xlrd.open_workbook('COMP40511_2010_dataset_4.xls')
        sheet = ds.sheet_by_index(0)
        self.name = sheet.name
        self.wmax = sheet.cell_value(rowx=2, colx=1)
        self.vmax = sheet.cell_value(rowx=3, colx=1)
        self.fmax = 0.
        self.items = {}
        for r in range(7, 35):
            self.items[r - 7] = {'w': sheet.cell(r, 1).value,
                                 'v': sheet.cell(r, 2).value,
                                 'p': sheet.cell(r, 3).value}
            self.fmax += sheet.cell(r, 3).value # the total fitness

    def get_wmax(self):
        return self.wmax

    def get_vmax(self):
        return self.vmax

    def get_items(self):
        return self.items