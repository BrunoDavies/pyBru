##where everything is run from
from user_interface import new_source_info, append_source_info

##what runs the whole thing (need to just have it automatically run)
def run_pyBru():
	while True:
		entry_type = input('New project or append or exit? (new/n or append/a or exit/e) ')
		entry_type = str.lower(entry_type).replace(' ', '')
		if entry_type == 'new':
			new_source_info()
		elif entry_type == 'append':
			append_source_info()
		elif entry_type == 'exit':
			return False 

run_pyBru()