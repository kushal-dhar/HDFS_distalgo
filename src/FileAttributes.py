import time

class Inode:
    """
    Inode stores metadata information about a file.
    Namenode stores Inode corresponding to each file in memory.
    """
    def __init__(self, filename):
        self.filename = filename
        self.namespace = None
        self.size = 0
        currentTime = time.clock()
        self.modifiedTime = currentTime
        self.accessTime = currentTime
        self.permissions = None
    
    def getFileName():
        """
        Returns the name of the file
        """
        pass
    
    def getFileSize():
        """
        Returns the size of the file in bytes
        """
        pass
    
    def getModifiedTime():
        """
        Returns the last modified time of the file
        Return Type: DataTime
        """
        pass
    
    def setModifiedTime(modifiedTime):
        """
        Sets the last modified time of the file
        """
        pass
    
    def getAccessTime():
        """
        Returns the last time file was accessed
        Return Type: DataTime
        """
        pass
    
    def setAccessTime(accessTime):
        """
        Sets the last access time of the file
        """
        pass
    
    def getNamespace():
        """
        Returns the namespace for the file
        """
        pass
    
    def setNamespace(namespace):
        """
        Sets the namespace for the file
        Return Type: None
        """
        pass

    def getPremissions():
        """
        Returns the access permissions for the file
        """
        pass
    
    def setPremissions(permissions):
        """
        Sets the access permissions for the file
        """
        pass


class Lease:
    """
    The  HDFS  client  that  opens  a  file  for  writing  is  granted  a lease for the file;
    no other client can write to the file. The writ-ing  client  periodically  renews
    the  lease  by  sending  a  heartbeat to the NameNode
    We need to store meta-data about the lease taken by the user on the file
    """
    def __init__(self, client, filename,leaseType):
        self.client = client
        self.filename  = filename
        self.leaseType = leaseType
        self.prevLeaseTS = None
        self.readers = 0


    def __str__(self):
        string = "client=%s, filename: %s" %(self.client, self.filename)
        return string

