"""
This file stores data structures needed to store blocks of files.
"""
import Config
import time
"""
BlockInfo stores information about physical location / datanode locations of blocks in a file
"""
class BlockInfo:
    def __init__(self, mfilename, minode):
        # Total number of blocks in the file
        self.numBlocks = 0
        # List of class DataBlocks
        # Location i of this list stores information about i'th block of file
        self.dataBlocks = [] # list of DataBlocks
        self.filename = mfilename
        # Indode data structure corresponding to this file
        self.inode = minode

    def __str__(self):
        dataBlockInfo = ','.join([str(d) for d in self.dataBlocks])
        info = "filename={0}, numBlocks={1}, dataBlocks={2}".format(self.filename, self.numBlocks, dataBlockInfo)
        return info

    def getBlockInfo(self, blockNumber):
        """
        Returns the list of datanodes and path at which block `blockNumber` of the file is located
        """
        return self.getDatanodeIdsForBlock(blockNumber)
    
    def addBlock(self, blockNumber, information):
        """
        Adds a new block of file to the metadata
        Implemented in self.addAppendInfo()
        """
        pass
    
    def addNodeToBlock(self, blockNumber, datanode):
        """
        Adds `datanode` as list of possible datanodes at which block `blockNumber` is located
        Implemented in self.addAppendInfo()
        """
        pass
    
    def removeNodeFromBlock(self, blockNumber, datanode):
        """
        Removes `datanode` from list of possible datanodes at which block `blockNumber` is located
        Function not needed in current implementation.
        """
        pass


    def getLastBlockSize(self):
        """
        Gets the size of the latest block of the file
        Needed for appending data to this block
        """
        if len(self.dataBlocks) == 0:
            # Means that no blocks are written to file yet
            return None
        return self.dataBlocks[-1].getBlockSize()

    def getLastBlockNumber(self):
        """
        Returns the blockNumber of last valid block of file.
        If file is empty, returns -1
        Block numbers start from 0
        """
        return len(self.dataBlocks) - 1

    def getNewAppendInfo(self):
        """
        Returns blocknumber and number of bytes which can be appended to last block.
        Needed for append operation.
        """
        if len(self.dataBlocks) == 0:
            return (0, Config.BLOCK_SIZE, True)
        blockNumber = self.getLastBlockNumber()
        bytesToWrite = Config.BLOCK_SIZE - self.getLastBlockSize()
        result = False
        if bytesToWrite <= 0:
            blockNumber += 1
            bytesToWrite = Config.BLOCK_SIZE
            result = True
        return (blockNumber, bytesToWrite, result)


    def addAppendInfo(self, blockNumber, bytesWritten, datanodeId):
        """
        Adds details for the last block written.
        The last written block can either be a fresh block,
        or there can be an append operation to an already existing block.
        """
        # While loop ensures that no index-out-of-bounds error occurs
        while blockNumber >= len(self.dataBlocks):
            bnum = len(self.dataBlocks)
            bpath = self.filename + '.block.' + str(bnum)
            self.dataBlocks.append(DataBlock(bnum, bpath))
        self.dataBlocks[blockNumber].addAppendInfo(bytesWritten, datanodeId)
        self.numBlocks = len(self.dataBlocks)

    def getLastBlockDatanodeIds(self):
        """
        Get the datanode where the last block is written.
        Returns those datanodes also which are dead.
        It is the callers reponsibility to check that returned datanodes are
        running before contacting them.
        If file is empty, it returns empty tuple.
        """
        if len(self.dataBlocks) == 0:
            return ()
        return self.dataBlocks[-1].getDatanodeIds()

    def getDatanodeIdsForBlock(self, blockNumber):
        """
             Get the datanodes where the block in question is written
        """
        # Check Index out of bounds error
        if len(self.dataBlocks) <= blockNumber:
            return ()
        return self.dataBlocks[blockNumber].getDatanodeIds()

    def getNumberOfBlocks(self):
        """
        Return total number of blocks in the file
        """
        return len(self.dataBlocks)


"""
Databock information storing class.
This class stores all the information needed for one block of a file.
Data stored: blockNumber, blockSize, access and modified time, metadata.
Also stores a dictionary of (datanodeId -> size), denoting size of this datablock on each datanode on which this block is hosted
"""
class DataBlock:
    def __init__(self, mblockNumber, mblockPath, mblockSize=0):
        self.blockNumber = mblockNumber # The number in sequence of blocks of the file
        self.blockPath = mblockPath  # The  path in datanode where the block is stored
        self.blockSize = mblockSize  # Size of the block
        self.datanodeSizeInfo = dict()
        self.checksumPath = mblockPath + Config.CHECKSUM_SUFFIX
        self.metadata = None
        self.checksum = None
        self.accessTime = None
        self.modifiedTime = None
        self.nodeID = None

    def __str__(self):
        info = "blockNumber={0}, blockSize={1}, datanodeIndo={2}".format(self.blockNumber, self.blockSize, self.datanodeSizeInfo)
        return info

    def getNode(self):
        """
        Returns the datanode where the block is stored
        """
        pass

    def getBlockNumber(self):
        """
        Return the blockNumber of this block
        """
        return self.blockNumber
    
    def setBlockNumber(self, mblockNumber):
        """
        Sets the blockNumber of this block
        """
        self.blockNumber = mblockNumber

    def getFilename(self):
        """
        Return the filename of this block is a part
        """
        pass
    
    def setFilename(self, mfilename):
        """
        Sets the filename of this block is a part
        """
        pass

    def getStorepath(self):
        """
        Returns the path on datanode where this block is stored
        """
        pass

    def setStorepath(self, mstorePath):
        """
        Sets the path on datanode where this block is stored
        """
        pass

    def getChecksumpath(self):
        """
        Returns the path on datanode where checksum of this block is stored
        Checksum is not currently implemented
        """
        pass

    def getChecksum(self):
        """
        Returns the checksum of this block
        Checksum is not currently implemented
        """
        pass

    def setChecksumpath(self):
        """
        Sets the path on datanode where checksum of this block is stored
        Checksum is not currently implemented
        """
        pass
    
    def getMetadata(self):
        """
        Returns metadata of this block
        Metadata is not currently implemented
        """
        pass

    def setMetadata(self):
        """
        Sets metadata of this block
        Metadata is not currently implemented
        """
        pass

    def getModifiedTime(self):
        """
        Returns the last modified time of the block
        """
        pass
    
    def setModifiedTime(self, mmodifiedTime):
        """
        Sets the last modified time of the block
        """
        pass
    
    def getAccessTime(self):
        """
        Returns the last time block was accessed
        """
        pass
    
    def setAccessTime(self, maccessTime):
        """
        Sets the last access time of the block
        """
        pass

    def getBlockSize(self):
        """
        Returns the total size of this block
        """
        return self.blockSize

    def addAppendInfo(self, bytesWritten, datanodeId):
        """
        Updates the information that on datanode `datanodeId`, `bytesWritten` number of bytes were appended to this block.
        This append operation can also change size of block.
        :param bytesWritten: int
        :param datanodeId: int
        :return: None
        """
        if datanodeId not in self.datanodeSizeInfo:
            self.datanodeSizeInfo[datanodeId] = bytesWritten
        else:
            self.datanodeSizeInfo[datanodeId] += bytesWritten
        self.blockSize = max(self.blockSize, self.datanodeSizeInfo[datanodeId])

    def getDatanodeIds(self):
        """
        Returns a tuple, containing datanodeId's which host this block
        :return:
        """
        ids = tuple([d for d in self.datanodeSizeInfo.keys()])
        return ids
