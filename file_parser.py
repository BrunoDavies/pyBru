import os

##function that parses for files of user
def parse_docs():
	current_docs = []
	for root, dirs, files in os.walk("./"):
		for file in files: 
			if file.endswith(".html"):
				current_docs.append(file)
	return (current_docs)

##check user input to see if they typed correct 
def check_file_name_exsists(file_name, current_docs):
	for doc in current_docs:
		if file_name + '.html' == doc:
			return True
	return False
