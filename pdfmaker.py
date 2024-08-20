from fpdf import FPDF

# Create instance of FPDF class
pdf = FPDF()

# Add a page
pdf.add_page()

# Set font
pdf.set_font("Arial", size=12)

# Add a cell (a cell is a rectangular area, possibly framed, which contains some text)
pdf.cell(200, 10, txt="Welcome to FPDF tutorial!", ln=True, align='C')

# Add another cell
pdf.cell(200, 10, txt="This is a simple PDF created using FPDF in Python.", ln=True, align='C')
pdf.cell(200, 10, txt="hello good morning", ln=True, align='C')
pdf.cell(200, 10, txt="Welcome to the easy learn academy Drashti and Vatsal", ln=True, align='C')
# Save the pdf with name .pdf
pdf.output("simple_demo.pdf")
