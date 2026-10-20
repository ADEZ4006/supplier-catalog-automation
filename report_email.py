#!/usr/bin/env python3

import os
import datetime
import reports
import emails

def process_data():
    desc_dir = os.path.join(os.path.expanduser("~"), "supplier-data/descriptions")
    paragraph = []
    for file in os.listdir(desc_dir):
        ruta = os.path.join(desc_dir, file)
        with open(ruta, "r") as f:
            name = f.readline().strip()
            weight = int(f.readline().strip())
            paragraph += "name: " + name + "<br/><br/>weight: " + weight + "<br/><br/><br/>"
    return paragraph

if __name__ == "__main__":
    paragraph = process_data()
    title = "Processed Update on " + datetime.datetime.today().strftime("%B %d, %Y")
    attachment = "/tmp/processed.pdf"
    reports.generate_report(attachment, title, paragraph)
    message = emails.generate_email("automation@example.com", "student@example.com", "Upload Completed - Online Fruit Store", "All fruits are uploaded to our website successfully. A detailed list is attached to this email.", attachment)
    emails.send_email(message)