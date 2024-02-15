from fpdf import FPDF
import pandas as pd
import glob
from pathlib import Path

filepaths = glob.glob("invoice/*.xlsx")

for filepath in filepaths:
    df = pd.read_excel(filepath, sheet_name="Sheet 1")
    pdf = FPDF(orientation="P", unit="mm", format="A4")
    pdf.add_page()

    filename= Path(filepath).stem
    invoice_nr = filename.split("-")[0]
    date = filename.split("-")[1]

    pdf.set_font(family="Times", style="B", size=16)
    pdf.set_text_color(0, 0, 0)
    pdf.cell(w=0, h=12, txt="Invoice nr. " + invoice_nr, 
             align="L", ln=1)
    pdf.cell(w=50, h=8, txt="Date " + date, align="L", ln=1)
    
    print(date)

    pdf.output(f"PDFs/{invoice_nr}.pdf")
