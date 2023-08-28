



def Query_exe(query, engine):
	import time

	query_exe = engine % query
	
	print("\nstarting query operation:")
	time.sleep(3)
	print(query_exe)

	query_obj = {"row1": 10, "row2": "name", "row3": "address"}

	return query_obj


