#!/bin/env python

# import requests
from lxml import etree
import html2text

# url = "https://pillow.readthedocs.io/en/stable/"
# page = requests.get(url)

file = open("pillow_doc_image.html", "r")
tree = etree.HTML(file.read())
sections = tree.xpath("//article[@role='main']/section//section")

h = html2text.HTML2Text()
h.mark_code = True

for idx, section in enumerate(sections):
    print(idx)
    html_out = etree.tostring(section, pretty_print=True, encoding='unicode')
    md_out = h.handle(html_out)
    with open(f"output/{idx}.md", "w") as f:
        f.write(md_out.strip())

file.close()
