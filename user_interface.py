##User inteface asking user to input info#
import os
from format_templates import *
from format_logic import parse_source_data, format_input_data, confim_new_name, confirm_input
from HTML_logic import html_new_single_source, html_append_single_source
from file_parser import parse_docs, check_file_name_exsists
			
##function that is when user wants to make a new document 
def new_source_info():
	while True:
		new_doc_name = input('Please name your new document... ')
		confirm_name_check = confim_new_name(new_doc_name)
		if confirm_name_check is False:
			new_source_info()
		source_type = input('What source type is this? (Journal or Website) ')
		source_type = str.lower(source_type).replace(' ', '')
		input_data = parse_source_data(source_type)
		format_input_data(input_data, source_type)
		html_new_single_source(input_data, source_type, new_doc_name)
		more_user_input = input('Another source? (y / n)')
		more_user_input = str.lower(more_user_input).replace(' ', '')
		if more_user_input == 'n':
			return(False)
		elif more_user_input == 'y':
			adding_sources(new_doc_name)

##function for when user wants to append document 
def append_source_info():
	while True: 
		print('')
		print('Please select which project to append... (enter fullname without extension)')
		print('')
		current_docs = parse_docs()
		print(current_docs)
		print('')
		append_doc_name = input('Name: ')
		if (check_file_name_exsists(append_doc_name, current_docs)) is False:
			print('File does not exsist... Please re-enter name')
			append_source_info()
		adding_sources(append_doc_name)
		continue_decision = input('Would you like to append another project? (y / n)')
		continue_decision = str.lower(continue_decision).replace(' ', '')
		if continue_decision == 'y':
			return True
		elif continue_decision == 'n':
			return False


##function that allows for the continuous 
def adding_sources(doc_name):
		source_type = input('What source type is this? (Journal or Website) ')
		source_type = str.lower(source_type).replace(' ', '')
		input_data = parse_source_data(source_type)
		format_input_data(input_data, source_type)
		confirm_input_check = confirm_input()
		if confirm_input_check is False: 
			adding_sources()

		html_append_single_source(input_data, source_type, doc_name)
		more_user_input = input('Another source? (y / n)')
		more_user_input = str.lower(more_user_input).replace(' ', '')
		if more_user_input == 'n':
			return(False)
		elif more_user_input == 'y':
			adding_sources(doc_name)


