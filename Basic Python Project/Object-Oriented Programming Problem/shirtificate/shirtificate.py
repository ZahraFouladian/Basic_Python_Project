from fpdf import FPDF
def main():
    name = input("Name:")
    pdf = FPDF()
    pdf.add_page(orientation="portrait", format="a4")
    pdf.image("./shirtificate.png", x=20, y=60)
    pdf.output("shirtificate.pdf")
