import os, shutil

DATABASE_NAME = 'hdfs'

file_path = os.getcwd()
file_path += '/datanodes/'

try:
    shutil.rmtree(file_path)
except:
    pass

PROJECT_DATA_PATH = file_path

NAMENODE_LOCATION = 'nnode'

DATANODE_LOCATION = 'dnode'
DATANODE_ID_FILE = 'datanodeid'

DATANODE_HEARTBEAT_INTERVAL = 60

CLIENT_LOCATION = 'cnode'

USER_LOCATION = 'unode'


TEST_FILE_PATH = '/home/droid/project_data/test_file.txt'

R_LEASE = 0
W_LEASE = 1
