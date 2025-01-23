import markdown
from xhtml2pdf import pisa

def convert_md_to_pdf(md_file_path, pdf_file_path):
    # Read Markdown file
    with open(md_file_path, 'r', encoding='utf-8') as md_file:
        md_content = md_file.read()

    # Convert Markdown to HTML
    html_content = markdown.markdown(md_content)
    with open(pdf_file_path, "wb") as pdf_file:
        pisa_status = pisa.CreatePDF(html_content, dest=pdf_file)

if __name__ == "__main__":
    md_file_path = 'index.md'  # Path to your Markdown file
    pdf_file_path = 'Tianqing_LIU.pdf'  # Desired output PDF file path

    convert_md_to_pdf(md_file_path, pdf_file_path)