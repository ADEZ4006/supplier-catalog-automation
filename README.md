# Supplier Catalog Automation

End-to-end automation pipeline that processes a supplier's product catalog - images, descriptions, report and notification email - built as a capstone project of the **Google IT Automation with Python** Professional Certificate(Course 6: *Automating Real-World Tasks with python*)

## What it does

Takes raw supplier data ('.tiff' product photos and '.txt' descriptions) and turns it into an updated web catalog, a PDF sales report, and a email summary - all in one automated run:

**Image processing** -- converts supplier photos from `.tiff` to `.jpeg` and resizes them to 600×400 using PIL/Pillow.
**Image upload** -- uploads every converted image to the web server via HTTP POST (`requests`).
**Catalog upload** -- parses each description file into a structured JSON dictionary (`name`, `weight`, `description`, `image_name`) and POSTs it to the catalog web service (Django backend).
**PDF report** -- generates a processed report with ReportLab summarizing the catalog data.
**Email notification** --  sends the PDF report as an attachment via SMTP using the `email` library.

## Tech stack

-**Python 3** -- scripts developed and debugged by hand; every line reviewed and understood
-**PIL/Pillow** -- image conversion and resizing
-**requests** -- HTTP uploads (images and JSON payloads)
-**ReportLab** -- PDF report generation
-**smtplib / email** -- report delivery by email
-**linux (bash)** -- scripts are executable, run on a Linux VM

## Project structure

.
├── changeImage.py            # .tiff 
-> .jpeg, resize 600x400
├── supplier_image_upload.py  # POST images to the web server
├── run.py                    # parse description files -> JSON -> POST catalog data
├── reports.py                # PDF generation helper (lab-provided)
├── report_email.py           # build report paragraph, generate PDF, send summary email
└── emails.py                 # email composition/sending helper (lab-provided)

## How to run

```bash
# 1. Convert and resize the supplier images
./changeImage.py

# 2. Upload the images to the web server
./supplier_image_upload.py

# 3. Upload catalog data to the web service
./run.py

# 4. Generate the PDF report and email it
./report_email.py

These scripts ran on the Qwiklabs lab VM (~/supplier-data/..., Django catalog service); paths and service URLs are lab-specific.

Skills demonstrated
•
Writing automation scripts that chain file processing, HTTP APIs, document generation and email
•
Parsing unstructured text files into structured JSON payloads
•
Debugging real HTTP/server errors (trailing-slash POST URLs, case-sensitive JSON keys, integer-vs-string fields)
•
Verifying results at the destination (web catalog, rendered PDF, delivered attachment) — not just "it ran without errors"
Author
Alvaro Hernandez — Fayetteville, Arkansas
•
GitHub: ADEZ4006
•
Google IT Automation with Python Professional Certificate (completed October 2026); working toward cloud engineering / DevOps.