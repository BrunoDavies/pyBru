##Templates for standard reference, project and saved file

##basic html page layout
html_new_doc = ["<html>", "<head></head>", "<body>", "</body>", "</html>"]



##Dict for what each source type needs 
source_info = {'journal': ['Author/s ', 'Title of Paper ', 'Journal ', 'Volume ', 'Number ', 'Pages ', 
				'Date of Publish '],
				'website': ['Author/s ', 'Date of Publish ','Title of Article/Page ', 'Website Name ',
				 'Link ', 'When Accessed ']}




##Dict for specific syntax for each source type, split by beginning and end 
html_format = {'journal': 
				{'begin': ['', '"', '<i>', 'vol. ', 'no. ', 'pg. ', ''], 
				'end': [', ', '", ', '</i>, ', ', ', ', ', ', ', '.']},

				'website': 
				{'begin': ['', '(', '<i>', '', 'Available at: ', ' [Accessed: '],
				'end': [' ', '). ', '</i>. ', ' [Online]. ', ' ', '].']}
				} 	