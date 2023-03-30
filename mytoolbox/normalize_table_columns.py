from unidecode import unidecode
import re

def snake_small_case(column):
	column_lower = column.lower()
	column_unidecode = unidecode(column_lower)
	column_alphanumeric = re.sub('[^A-Za-z0-9]+', ' ', column_unidecode)
	column_split = column_alphanumeric.split(' ')
	column_empty = [x for x in column_split if x != '']
	column = '_'.join(column_empty)
	return column
	


	
