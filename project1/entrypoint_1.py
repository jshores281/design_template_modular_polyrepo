
import os, sys
import __init__





def entrypoint_project1():
	from packages.package1.connectors.db1_conn import db1_conn
	from packages.package1.queries.db1_query import Query1
	from packages.package1.queries.query_executor import Query_exe
	from packages.package1.transformers.db_etl_1 import ETL_1


	server_ip = "192.168.1.2"
	server_db = "phase2.db"

	db_conn_obj = db1_conn(server_ip, server_db)
	query_obj = Query1(server_db)
	query_results = Query_exe(query_obj, db_conn_obj)
	# print(query_results)

	cleaned_data = ETL_1(query_results)

	return cleaned_data


eproj1 = entrypoint_project1()
print(eproj1)

