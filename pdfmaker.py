from fpdf import FPDF
pdf = FPDF()

# Add a page
pdf.add_page()

# Set font
pdf.set_font("Arial", size = 12)

# Add a cell
pdf.cell(200, 10, txt = "Hello World!", ln = True, align = 'C')

# Save the PDF with name .pdf
pdf.output("simple_demo.pdf")