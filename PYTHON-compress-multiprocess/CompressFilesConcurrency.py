import bz2
import multiprocessing as mp
import os
from shutil import copyfileobj

''' Input / Output Path '''

ipath = '/home/nguyendotu/Desktop/tund/program-language/PYTHON-compress-multithread/testfile/'
opath = '/home/nguyendotu/Desktop/tund/program-language/PYTHON-compress-multithread/archives/'

''' Number of Processes '''
num_of_proc = 6


def compressFile(fileName, chunkSize=100000000):
    global ipath
    print 'Started Compressing %s to %s' % (fileName, opath)
    inp = open(ipath + fileName, 'rb')
    output = bz2.BZ2File(opath + fileName.split('/')[-1].strip('.csv') + '.bz2', 'wb', compresslevel=9)
    copyfileobj(inp, output, chunkSize)
    print 'Finished Compressing %s to %s' % (fileName, opath)


def process_worker(fileList):
    for ls in fileList:
        for _x in ls:
            compressFile(_x)


def split_list(_tempList):
    a, reList = 0, []
    global num_of_proc
    for _x in range(num_of_proc + 1):
        reList.append([_tempList[a:a + len(_tempList) / num_of_proc]])
        a = a + len(_tempList) / num_of_proc
    return reList


pool = mp.Pool(processes=num_of_proc)
''' Prepare a list of all the file names '''
tempList = [x for x in os.listdir(ipath)]

''' Split the list into sub-lists 
    For example : if I have 90 files and I am using 6 processes 
                  each of the process will work on 15 files each '''

iterList = split_list(tempList)
''' print iterList >> [ [filename1, filename2] , [filename3,filename4], ... ] '''

''' Pass the list consisting of sub-lists to pool '''
pool.map(process_worker, iterList)
