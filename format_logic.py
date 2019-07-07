##logic for formatting inputed source and parsing for input
from format_templates import source_info

##parse data to allow for user input 
def parse_source_data(source_type):
	file_output = {}
	for info in source_info[source_type]:
		file_output[info] = input(info + ': ')
	return file_output

##Old code for when I thought I could print to terminal with text format... 
##Currently used to show user whats been inputed
def format_input_data(input_data, source_type):
	output_string  = ''
	if source_type  == 'journal':
		for key, val in input_data.items():
			output_string = output_string + val + ', '
		print(output_string)
	elif source_type == 'website':
		for key, val in input_data.items():
			output_string = output_string + val + ', '
		print(output_string)

##confirm new doc name is what user wants
def confim_new_name(new_doc_name):
	print(new_doc_name)
	confim_name = input('Are you sure? (y / n) ')
	confim_name = str.lower(confim_name).replace(' ', '')
	if confim_name == 'n':
		return False
	if confim_name == 'y':
		return True

##confirm user input is correct
def confirm_input():
	confirm_user_source_input = input('Is the following information above corret? (y / n)')
	confirm_user_source_input = str.lower(confirm_user_source_input).replace(' ', '')
	if confirm_user_source_input == 'y':
		return (True)
	else: 
		return (False)
