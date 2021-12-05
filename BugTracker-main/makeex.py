# STIL UNFINISHED
import xlsxwriter
from models import bug_report

reports = bug_report.query.order_by(bug_report._id).all()
outWorkbook = xlsxwriter.Workbook("out.xls")
outSheet = outWorkbook.add_worksheet()
# Create file workbook
for report in reports:
    print('wrote ' + str(report._id))
    outSheet.write("A" + str(report._id + 1),  report.reporter_name)
    outSheet.write("B" + str(report._id + 1),  report.reporter_email)
    outSheet.write("C" + str(report._id + 1),  report.reporter_phone)
    outSheet.write("D" + str(report._id + 1),  report.system)
    outSheet.write("E" + str(report._id + 1),  report.severity)
    outSheet.write("F" + str(report._id + 1),  report.steps)
    outSheet.write("G" + str(report._id + 1),  report.message)
    outSheet.write("H" + str(report._id + 1),  report.status)
    outSheet.write("I" + str(report._id + 1),  report.time_of_report)

outWorkbook.close()
