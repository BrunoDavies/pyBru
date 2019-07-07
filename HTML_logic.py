##logic to create HTML doc's that allow for correct formatting
from format_templates import html_new_doc, html_format

##adding a source to a new, not created, document 
def html_new_single_source(input_data, source_type, new_doc_name):
	counter = 0
	if source_type == "journal":
		html_doc = open(new_doc_name +'.html', 'w')
		for element in html_new_doc:
			if element == "</body>":
				for key, val in input_data.items():
					html_doc.write(html_format['journal']['begin'][counter])
					html_doc.write(val)
					html_doc.write(html_format['journal']['end'][counter])
					counter = counter + 1
			html_doc.write(element)
		html_doc.close()
	
	if source_type == "website":
		html_doc = open(new_doc_name + '.html', 'w')
		for element in html_new_doc:
			if element == "</body>":
				for key, val in input_data.items():
					html_doc.write(html_format['website']['begin'][counter])
					html_doc.write(val)
					html_doc.write(html_format['website']['end'][counter])
					counter = counter + 1
			html_doc.write(element)
		html_doc.close()

##adding a source to an already created document 
def html_append_single_source(input_data, source_type, append_doc_name):
	counter = 0
	if source_type == "journal":
		html_doc = open(append_doc_name + '.html', 'a')
		for element in html_new_doc:
			if element == "</body>":
				html_doc.write("<p>")
				for key, val in input_data.items():
					html_doc.write(html_format['journal']['begin'][counter])
					html_doc.write(val)
					html_doc.write(html_format['journal']['end'][counter])
					counter = counter + 1
				html_doc.write("</p>")
			html_doc.write(element)
		html_doc.close()
	
	if source_type == "website":
		html_doc = open(append_doc_name + '.html', 'a')
		for element in html_new_doc:
			if element == "</body>":
				html_doc.write("<p>")
				for key, val in input_data.items():
					html_doc.write(html_format['website']['begin'][counter])
					html_doc.write(val)
					html_doc.write(html_format['website']['end'][counter])
					counter = counter + 1
				html_doc.write("</p>")
			html_doc.write(element)
		html_doc.close()
