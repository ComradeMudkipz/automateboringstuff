#! /usr/bin/python
# sendDuesReminders.py - Sends emails based on payment status in spreadsheet.

import openpyxl
import smtplib
import sys


# Open the spreadsheet and get the latest dues status.
wb = openpyxl.load_workbook('duesRecords.xlsx')
sheet = wb.get_sheet_by_name('Sheet1')

lastCol = sheet.get_highest_column()
latestMonth = sheet.cell(row=1, column=lastCol).value

# TODO: Check each member's payment status.


# TODO: Log in to email account.


# TODO: Send out reminder emails.
