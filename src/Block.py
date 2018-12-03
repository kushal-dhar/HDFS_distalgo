
import Config
import time
"""
BlockInfo stores information about physical location of blocks in a file
"""
class BlockInfo:
    def __init__(self, mfilename, minode):
        self.numBlocks = 0
        self.dataBlocks = [] # list of DataBlocks
        self.filename = mfilename
        self.inode = minode

    def __str__(self):
        #TODO - replace , with \n
        dataBlockInfo = ','.join([str(d) for d in self.dataBlocks])
        info = "filename={0}, numBlocks={1}, dataBlocks={2}".format(self.filename, self.numBlocks, dataBlockInfo)
        return info

    def getBlockInfo(self, blockNumber):
        """
        Returns the list of datanodes and path at which block `blockNumber` of the file is located
        """
        pass
    
    def addBlock(self, blockNumber, information):
        """
        Adds a new block of file to the metadata
        """
        pass
    
    def addNodeToBlock(self, blockNumber, datanode):
        """
        Adds `datanode` as list of possible datanodes at which block `blockNumber` is located
        """
        pass
    
    def removeNodeFromBlock(self, blockNumber, datanode):
        """
        Removes `datanode` from list of possible datanodes at which block `blockNumber` is located
        """
        pass


    def getLastBlockSize(self):
        if len(self.dataBlocks) == 0:
            # Means that no blocks are written to file yet
            return None
        return self.dataBlocks[-1].getBlockSize()

    def getLastBlockNumber(self):
        return len(self.dataBlocks) - 1

    def getNewAppendInfo(self):
        """
        Returns blocknumber and number of bytes which can be appended to last block
        :return:
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
        while blockNumber >= len(self.dataBlocks):
            bnum = len(self.dataBlocks)
            bpath = self.filename + '.block.' + str(bnum)
            self.dataBlocks.append(DataBlock(bnum, bpath))
        self.dataBlocks[blockNumber].addAppendInfo(bytesWritten, datanodeId)
        self.numBlocks = len(self.dataBlocks)

    def getLastBlockDatanodeIds(self):
        if len(self.dataBlocks) == 0:
            return ()
        return self.dataBlocks[-1].getDatanodeIds()

    def getDatanodeIdsForBlock(self, blockNumber):
        # TODO - Check Index out of bounds error
        return self.dataBlocks[blockNumber].getDatanodeIds()

    def getNumberOfBlocks(self):
        return len(self.dataBlocks)


"""
Databock information storing object
"""
class DataBlock:
    def __init__(self, mblockNumber, mblockPath, mblockSize=0):
        self.blockNumber = mblockNumber
        self.blockPath = mblockPath
        self.blockSize = mblockSize
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

    def getBlockSize(self):
        return self.blockSize

    def addAppendInfo(self, bytesWritten, datanodeId):
        if datanodeId not in self.datanodeSizeInfo:
            self.datanodeSizeInfo[datanodeId] = bytesWritten
        else:
            self.datanodeSizeInfo[datanodeId] += bytesWritten
        self.blockSize = max(self.blockSize, self.datanodeSizeInfo[datanodeId])

    def getDatanodeIds(self):
        ids = tuple([d for d in self.datanodeSizeInfo.keys()])
        return ids