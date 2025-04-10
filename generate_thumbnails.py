from pdf2image import convert_from_path
from pathlib import Path
import shutil

# For a windows machine do the following to get poppler installed if not already installed
# Download Poppler from: https://github.com/oschwartz10612/poppler-windows/releases/
# Unzip and place it somewhere (e.g., C:\poppler, or c:\util)
#Add the bin folder to your system's PATH environment variable.
#Optionally, specify the path directly in the script:
# poppler_path = r"C:\util\popper...\bin"  # put the full install path here

pdf_dir =  Path("*") # put the location of the pdfs
output_root = Path("thumbnails") # output location of all the newly created folders and thumbnails
output_root.mkdir(exist_ok=True)

for pdf_file in pdf_dir.glob("*.pdf"):
    # Create a subdirectory named after the PDF file (without extension)
    folder_name = pdf_file.stem
    pdf_output_dir = output_root / folder_name
    pdf_output_dir.mkdir(parents=True, exist_ok=True)

    # Convert only the first page of the PDF to a thumbnail, this was the best way to generate a thumbnail quickly
    pages = convert_from_path(
        str(pdf_file),
        first_page=1,
        last_page=1,
        poppler_path=poppler_path  # This is required only on Windows
    )

    # Save the thumbnail using the same name as the PDF but with .jpg
    thumbnail_path = pdf_output_dir / f"{folder_name}.jpg"
    pages[0].save(thumbnail_path, "JPEG")

    # Copy the original PDF into the same folder
    shutil.copy(pdf_file, pdf_output_dir / pdf_file.name)
    # Finish statement 
    print("Finished conversion")