# pdfimages_thumbnails
This Python script scans a specified (defined) directory for PDF files and processes each one by in order to generate thumbnails
1. Creating a subfolder and thumbnail named after the PDF file (without the .pdf extension).
2. Generating a thumbnail image of the first page of the PDF.
3. Saving both the original PDF and its corresponding thumbnail image into the newly created subfolder.
4. This helps organize PDFs and their previews neatly for browsing, display, or archiving purposes in order to copy this data up to an S3 bucket for ingestion and preservation
