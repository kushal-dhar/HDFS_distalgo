"""
A common config file to hold configurable values used all across the file-system
"""
import os, shutil
from os.path import expanduser

DATABASE_NAME = 'hdfs'

home = expanduser("~")
data_dir = home + '/datanodes/'

def cleanDirectoryBeforeStart():
    try:
        shutil.rmtree(data_dir)
    except:
        pass

PROJECT_DATA_PATH = data_dir

NAMENODE_LOCATION = 'nnode'

DATANODE_LOCATION = 'dnode'
DATANODE_ID_FILE = 'datanodeid'


DATANODE_HEARTBEAT_INTERVAL = 3
CLIENT_HEARTBEAT_INTERVAL = 60
CLIENT_HARD_LIMIT = 120

CLIENT_LOCATION = 'cnode'
CLIENT2_LOCATION = 'cnode2'

USER_LOCATION = 'unode'

DATANODE_HEARTBEAT_LOCATION = 'hbpnode'

BLOCK_REPLICATION_FACTOR = 2


BLOCK_SIZE = 10

R_LEASE = 0
W_LEASE = 1

CHECKSUM_SUFFIX = '.checksum'

#  set to 600 sec according to paper
DATANODE_HEARTBEAT_TIMEOUT = 30 # 30 sec for now

# set to 100 sec for large cluster
DATANODE_HEARTBEAT_CHECK_INTERVAL = 5 # 5 sec
