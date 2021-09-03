# Import the required Module
import tabula
# Read a PDF File
df = tabula.read_pdf("/Users/paww/Documents/GitHub/NLP-project-Radix/assets/pdf/14.pdf", pages='all')[0]
# convert PDF into CSV
tabula.convert_into("/Users/paww/Documents/GitHub/NLP-project-Radix/assets/pdf/14.pdf", "/Users/paww/Documents/GitHub/NLP-project-Radix/assets/pdf/14.csv", output_format="csv", pages='all')
print(df)