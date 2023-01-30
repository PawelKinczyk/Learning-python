import openpyxl

wb = openpyxl.load_workbook('14.TestSheet.xlsx')
wb.sheetnames
sheet = wb['Arkusz1']
sheet
type(sheet)
sheet.title
active_sheet = wb.active
active_sheet

a1 = sheet['A1']
sheet['A1'].value

'Row %s, Column %s is %s' % (a1.row, a1.column, a1.value)

sheet.cell(row=1, column=2) # get exact cell 

sheet.max_row
sheet.max_column

## Get rows from each colymns

for rowOfCellObjects in sheet['A1':'C3']:
    for cellObj in rowOfCellObjects:
        print(cellObj.coordinate, cellObj.value)
    print('--- END OF ROW ---')

## Get columns 

list(sheet.columns)[1] # Get second column's cells.

for cellObj in list(sheet.columns)[1]:
        print(cellObj.value)

## Creating new sheet

wb.create_sheet(index=0, title='First Sheet')
wb.sheetnames
del wb['First Sheet']