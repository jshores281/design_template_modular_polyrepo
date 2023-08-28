


def db1_conn(server, database):
	import time
	"""
	Allows variable connections and executes a given query
	"""

	server = server
	database = database

	print('connecting to server...')
	time.sleep(3)
	conn_comf = "connected! server = {}: database = {}".format(server,database)
	print(conn_comf)

	conn_obj = "\ndb connection session: \nQUERY: %s"

	return conn_obj



# print(db1_conn("192.168.1.1", "dbo.test-db"))

