import os, shutil
from os.path import expanduser

DATABASE_NAME = 'hdfs'

home = expanduser("~")
home += '/datanodes/'


try:
    shutil.rmtree(home)
except:
    pass

PROJECT_DATA_PATH = home

NAMENODE_LOCATION = 'nnode'

DATANODE_LOCATION = 'dnode'
DATANODE_ID_FILE = 'datanodeid'

# TODO: change it to 60 finally
DATANODE_HEARTBEAT_INTERVAL = 3
CLIENT_HEARTBEAT_INTERVAL = 60
CLIENT_HARD_LIMIT = 120

CLIENT_LOCATION = 'cnode'
CLIENT2_LOCATION = 'cnode2'

USER_LOCATION = 'unode'

DATANODE_HEARTBEAT_LOCATION = 'hbpnode'

BLOCK_REPLICATION_FACTOR = 2

TEST_FILE_PATH = '/home/droid/project_data/test_file.txt'

# TODO : make block size more!
BLOCK_SIZE = 1000

TEST_FILE_PATH = '/home/droid/project_data/test_file.txt'

R_LEASE = 0
W_LEASE = 1

CHECKSUM_SUFFIX = '.checksum'

# TODO - set to 600 sec
DATANODE_HEARTBEAT_TIMEOUT = 30 # 10 min

# TODO - set to 100 sec
DATANODE_HEARTBEAT_CHECK_INTERVAL = 5