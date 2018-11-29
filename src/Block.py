

"""
BlockInfo stores information about physical location of blocks in a file
"""
class BlockInfo:
    def __init__():
        self.numBlocks = 0
        self.dataBlocks = None # list of DataBlocks
        self.filename = None
        self.inode = None
    
    def getBlockInfo(blockNumber):
        """
        Returns the list of datanodes and path at which block `blockNumber` of the file is located
        """
        pass
    
    def addBlock(blockNumber, information):
        """
        Adds a new block of file to the metadata
        """
        pass
    
    def addNodeToBlock(blockNumber, datanode):
        """
        Adds `datanode` as list of possible datanodes at which block `blockNumber` is located
        """
        pass
    
    def removeNodeFromBlock(blockNumber, datanode):
        """
        Removes `datanode` from list of possible datanodes at which block `blockNumber` is located
        """
        pass

"""
Databock information storing object
"""
class DataBlock:
    def __init__():
        self._nodeID = None
        self._datanode = None
        self._filename = None
        self._blockNumber = None
        self._storePath = None
        self._checksumPath = None
        self._metadata = None
        self._checksum = None
        self._accessTime = None
        self._modifiedTime = None
    
    def getNode():
        """
        Returns the datanode where the block is stored
        """
        pass

    def getBlockNumber():
        """
        Return the blockNumber of this block
        """
        pass
    
    def setBlockNumber():
        """
        Sets the blockNumber of this block
        """
        pass

    def getFilename():
        """
        Return the filename of this block is a part
        """
        pass
    
    def setFilename():
        """
        Sets the filename of this block is a part
        """
        pass

    def getStorepath():
        """
        Returns the path on datanode where this block is stored
        """
        pass

    def setStorepath():
        """
        Sets the path on datanode where this block is stored
        """
        pass

    def getChecksumpath():
        """
        Returns the path on datanode where checksum of this block is stored
        """
        pass

    def getChecksum():
        """
        Returns the checksum of this block
        """
        pass

    def setChecksumpath():
        """
        Sets the path on datanode where checksum of this block is stored
        """
        pass
    
    def getMetadata():
        """
        Returns metadata of this block
        """
        pass

    def setMetadata():
        """
        Sets metadata of this block
        """
        pass

    def getModifiedTime():
        """
        Returns the last modified time of the block
        """
        pass
    
    def setModifiedTime(modifiedTime):
        """
        Sets the last modified time of the block
        """
        pass
    
    def getAccessTime():
        """
        Returns the last time block was accessed
        """
        pass
    
    def setAccessTime(accessTime):
        """
        Sets the last access time of the block
        """
        pass