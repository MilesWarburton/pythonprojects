#!/usr/bin/python

import glob, os, pwd, sys, csv
from sys import argv

class UserDiskUsage:

        def __init__(self):
                self.FileOwnerUIDList=[]
                self.FileSizeList=[]
                self.FileList = []


        def getFileName(self, args):
                fileList = self.FileList
                filepath = args[1]
                listing = glob.glob(filepath+'*')
                for files in listing:
                        fileList.append(os.path.join(filepath, files))
                return fileList


        def getFileSize(self):
                fileList = self.FileList
                filesize = self.FileSizeList
                for i in fileList:
                        filesize.append(os.path.getsize(i))
                return filesize


        def getFileOwner(self):
                fileList = self.FileList
                FileOwnerUIDList = self.FileOwnerUIDList
                for i in fileList:
                        FileOwnerUIDList.append(pwd.getpwuid(os.stat(i).st_uid).pw_name)
                return FileOwnerUIDList

