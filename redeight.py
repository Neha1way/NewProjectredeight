from selenium import webdriver
import time
from fpdf import FPDF
import PyPDF2

#Login page
driver=webdriver.Chrome(executable_path="E:/NewProject/Chrome/chromedriver.exe")
driver.maximize_window()
email = "rohit@1wayit.co.uk"
password ="admin786"
driver.get("http://redeightstage.1wayit.com")
driver.find_element_by_name("email").send_keys(email)
driver.find_element_by_name("password").send_keys(password)
submit=driver.find_element_by_xpath("//div[@class='btn-section text-left p-0']/button")
submit.click()
time.sleep(3)

#To create pdf file
pdf = FPDF()
pdf.add_page()
pdf.set_font('Arial','', 14)
pdf.cell(6)
pdf.cell(120, 20, ' Login Successfully into Red Eight Gallery ', 1, 1, 'B')
pdf.output('Login.pdf', 'F')

# Reading data from PDF file
from PyPDF2 import PdfFileReader
# Gave file name from which data has to be extracted
pdf=PdfFileReader('Login.pdf')
# Created pdf file page reader
page_1_object = pdf.getPage(0)
# Created pdf file page text reader
page_1_text = page_1_object.extractText()
# Printed output from pdf file
print(page_1_text)
driver.quit()
