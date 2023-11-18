import openpyxl

File = ""

wb = openpyxl.Workbook()
sheet = wb.active


def write_file(cell: str, value: str):
    if File == "":
        print("did nothing, file is not initialized")
        pass
    else:
        sheet[cell] = value
        wb.save(File)
