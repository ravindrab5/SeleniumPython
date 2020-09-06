import xlrd

class ExcelReader:

    def __init__(self, filepath, sheetname):
        self.filepath = filepath
        self.sheetname = sheetname


    def readData(self):
        loc = (self.filepath)
        workbook = xlrd.open_workbook(loc)
        sheet = workbook.sheet_by_name(self.sheetname)
        row_count = sheet.nrows
        col_count = sheet.ncols
        data = [[str(sheet.cell_value(i, j)) for j in range(0, col_count)] for i in range(0, row_count)]
        return data

