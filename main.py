from fpdf import FPDF
import pandas as pd
import glob

filepaths = glob.glob("invoice/*.xlsx")

df_list = [pd.read_excel(filepath, sheet_name="Sheet 1") for filepath in filepaths]

