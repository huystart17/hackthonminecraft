from read_from_minecraft import printBlocksFromFile
import hieu_citydata


def make_office():
    for office in hieu_citydata.officePlace:
        printBlocksFromFile(office['x'], office['y'], office['z'], hieu_citydata.officeFileData)
