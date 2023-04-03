from fpdf import FPDF
import pandas as pd

pdfdocument = FPDF(orientation="P", unit="mm", format="A4")
pdfdocument.set_auto_page_break(auto=False, margin=0)

dataframe = pd.read_csv("topics.csv")

for index, row in dataframe.iterrows():
    pdfdocument.add_page()

    
    pdfdocument.set_font(family="Futura", style="B", size=24)
    pdfdocument.set_text_color(100, 100, 100)
    pdfdocument.cell(w=0, h=12, txt=row["Topic"], align="L",
         ln=1)
    for y in range(20, 298, 10):
        pdfdocument.line(10, y, 200, y)

    
    pdfdocument.ln(265)
    pdfdocument.set_font(family="Futura", style="I", size=8)
    pdfdocument.set_text_color(180, 180, 180)
    pdfdocument.cell(w=0, h=10, txt=row["Topic"], align="R")


    for i in range(row["Pages"] - 1):
        pdfdocument.add_page()

        
        pdfdocument.ln(277)
        pdfdocument.set_font(family="Futura", style="I", size=8)
        pdfdocument.set_text_color(180, 180, 180)
        pdfdocument.cell(w=0, h=10, txt=row["Topic"], align="R")

        for y in range(20, 298, 10):
            pdfdocument.line(5, y, 200, y)

pdfdocument.output("output.pdf")