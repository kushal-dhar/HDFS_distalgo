"""
   A common config file to hold hard coded values used all across the file-system
"""
import os, shutil
from os.path import expanduser

DATABASE_NAME = 'hdfs'

home = expanduser("~")
home += '/datanodes/'

try:
    os.rmdir(home)
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

# TODO : make block size more!
BLOCK_SIZE = 1000

R_LEASE = 0
W_LEASE = 1

CHECKSUM_SUFFIX = '.checksum'

# TODO - set to 600 sec
DATANODE_HEARTBEAT_TIMEOUT = 30 # 10 min

# TODO - set to 100 sec
DATANODE_HEARTBEAT_CHECK_INTERVAL = 5
