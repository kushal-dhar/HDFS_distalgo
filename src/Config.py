import os, shutil

DATABASE_NAME = 'hdfs'

file_path = os.getcwd()
file_path += '/datanodes/'

'''
try:
    shutil.rmtree(file_path)
except:
    pass
'''
PROJECT_DATA_PATH = '/home/kushal/Documents/Async/HDFS/latest_commit/src/'

NAMENODE_LOCATION = 'nnode'

DATANODE_LOCATION = 'dnode'
DATANODE_ID_FILE = 'datanodeid'

DATANODE_HEARTBEAT_INTERVAL = 60
CLIENT_HEARTBEAT_INTERVAL = 60
CLIENT_HARD_LIMIT = 300

CLIENT_LOCATION = 'cnode'
CLIENT2_LOCATION = 'cnode2'

USER_LOCATION = 'unode'

BLOCK_REPLICATION_FACTOR = 2

TEST_FILE_PATH = '/home/droid/project_data/test_file.txt'

# TODO : make block size more!
BLOCK_SIZE = 5

TEST_FILE_PATH = '/home/droid/project_data/test_file.txt'

R_LEASE = 0
W_LEASE = 1

CHECKSUM_SUFFIX = '.checksum'
