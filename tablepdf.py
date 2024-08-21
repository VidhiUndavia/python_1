from fpdf import FPDF

# Create a PDF class instance
pdf = FPDF()

# Add a page
pdf.add_page()

# Set font for the table (Arial, bold, size 12)
# pdf.set_font("Arial", "B", 12)
pdf.add_font('Chiller', '', 'Chiller.ttf', uni=True)
pdf.set_font('Chiller', '', 16)
pdf.set_text_color(45, 23, 255)

# Table header
header = ['ID', 'Name', 'Age', 'Country']

# Table data
data = [
    ['1', 'John Doe', '28', 'USA'],
    ['2', 'Anna Smith', '23', 'UK'],
    ['3', 'Peter Jones', '35', 'Canada'],
    ['4', 'Emily Davis', '40', 'Australia']
]

# Set column widths for the table
col_width = pdf.w / 4.5  # Calculate width of each column based on page width

# Set height for each row
row_height = 10

# Table header
for col in header:
    pdf.cell(col_width, row_height, col, border=1, align='C')
pdf.ln(row_height)  # Move to the next line after the header

# Table rows
for row in data:
    for item in row:
        pdf.cell(col_width, row_height, item, border=1, align='C')
    pdf.ln(row_height)  # Move to the next line after each row

# Save the PDF file
pdf.output('table_example1.pdf')
