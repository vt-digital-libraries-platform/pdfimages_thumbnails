# 📄 pdfimages_thumbnails

This Python script scans a specified directory for PDF files and processes each one to generate and organize thumbnails to be used in the S3 previews.

## 🔍 What It Does

For each PDF file in the given folder, the script:

1. **Creates a subfolder** named after the PDF file (excluding the `.pdf` extension).
2. **Generates a thumbnail** of the first page of the PDF.
3. **Saves both the original PDF and the thumbnail** inside the new subfolder.
4. **Organizes files for easier browsing, display, or archiving and to uploaded into the S3.**


