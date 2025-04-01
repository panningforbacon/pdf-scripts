import os
from PyPDF2 import PdfReader, PdfWriter

def remove_last_page_from_pdfs(directory):
    for filename in os.listdir(directory):
        if filename.lower().endswith(".pdf"):
            filepath = os.path.join(directory, filename)
            reader = PdfReader(filepath)

            if len(reader.pages) <= 1:
                print(f"Skipping {filename} (only 1 page or empty)")
                continue

            writer = PdfWriter()
            for page in reader.pages[:-1]:  # Exclude the last page
                writer.add_page(page)

            with open(filepath, "wb") as f_out:
                writer.write(f_out)

            print(f"Trimmed last page from {filename}")

# Example usage
remove_last_page_from_pdfs("working_directory")
