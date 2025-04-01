import os
import re
from PyPDF2 import PdfMerger

def merge_pdf_groups(directory):
    groups = {}

    # Find all PDFs matching the _1.pdf, _2.pdf pattern
    for filename in os.listdir(directory):
        if filename.endswith(".pdf"):
            match = re.match(r"^(.*)_([0-9]+)\.pdf$", filename)
            if match:
                base, index = match.groups()
                groups.setdefault(base, []).append((int(index), filename))

    for base, files in groups.items():
        sorted_files = sorted(files, key=lambda x: x[0])
        merger = PdfMerger()
        for _, filename in sorted_files:
            merger.append(os.path.join(directory, filename))
        output_path = os.path.join(directory, f"{base}.pdf")
        merger.write(output_path)
        merger.close()
        print(f"Merged {len(files)} files into {output_path}")

# Example usage
merge_pdf_groups("working_directory")
