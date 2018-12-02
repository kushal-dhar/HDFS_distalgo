import time

class Inode:
    """
    Inode stores metadata information about a file.
    Namenode stores Inode corresponding to each file in memory.
    """
    def __init__(self, filename):
        self._filename = filename
        self._namespace = None
        self._size = 0
        currentTime = time.clock()
        self._modifiedTime = currentTime
        self._accessTime = currentTime
        self._permissions = None
    
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
    We need to store meta-data about the lease taken by the user on thd file
    """
    def __init__(self, client, filename,leaseType):
        self.client = client
        self.filename  = filename
        self.leaseType = leaseType
        self.prevLeaseTS = None

