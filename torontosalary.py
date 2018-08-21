import xlrd
import os

file_location = os.getcwd() + "/uoftsalaries.xlsx"

workbook = xlrd.open_workbook(file_location)
sheet = workbook.sheet_by_index(0)

for row in range(1, 215):
    if sheet.cell_value(row, 10) == "PEY" and sheet.cell_value(row, 7) in ["Toronto", "Oakville"]:
        print("PEY " + "Salary: " + sheet.cell_value(row, 11) + " Location: " + sheet.cell_value(row, 7) + " Title: " + sheet.cell_value(row,8))

    
