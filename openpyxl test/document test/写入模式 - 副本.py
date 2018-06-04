from openpyxl import Workbook
wb = Workbook(write_only = True)
ws = wb.create_sheet()
from openpyxl.worksheet.write_only import WriteOnlyCell
from openpyxl.comments import Comment
from openpyxl.styles import Font
cell = WriteOnlyCell(ws, value="hello world")
cell.font = Font(name='Courier', size=36)
cell.comment = Comment(text="A comment", author="Author's Name")
ws.append([cell, 3.14, None])
wb.save('write_only_file.xlsx')
