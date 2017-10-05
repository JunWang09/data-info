'''
code to pull data from
https://data.medicare.gov/data/archives/hospital-compare
'''

import pandas as pd
import numpy as np

from StringIO import StringIO
import urllib
import zipfile
import os
    
path = 'C:/Users/junwan/Desktop/Projects/Hospital/data/'

file_list = [
'2005/May/HOSArchive_20050501.zip'
,'2005/September/HOSArchive_20050901.zip'
,'2005/December/HOSArchive_20051201.zip'

,'2006/March/HOSArchive_20060301.zip'
,'2006/June/HOSArchive_20060601.zip'
,'2006/December/HOSArchive_20061201.zip'

,'2007/March/HOSArchive_20070301.zip'
,'2007/June/HOSArchive_20070601.zip'
,'2007/September/HOSArchive_20070901.zip'
,'2007/December/HOSArchive_20071201.zip'

,'2008/April/HOSArchive_20080401.zip'
,'2008/August/HOSArchive_20080801.zip'
,'2008/October/HOSArchive_20081001.zip'
,'2008/December/HOSArchive_20081201.zip'

,'2009/March/HOSArchive_20090301.zip'
,'2009/July/HOSArchive_20090701.zip'
,'2009/September/HOSArchive_20090901.zip'
,'2009/December/HOSArchive_20091201.zip'

,'2010/March/HOSArchive_20100301.zip'
,'2010/June/HOSArchive_20100601.zip'
,'2010/July/HOSArchive_20100701.zip'
,'2010/October/HOSArchive_20101001.zip'
,'2010/December/HOSArchive_20101201.zip'

,'2011/April/HOSArchive_20110401.zip'
,'2011/August/HOSArchive_20110801.zip'
,'2011/October/HOSArchive_20111001.zip'

,'2012/January/HOSArchive_20120101.zip'
,'2012/April/HOSArchive_20120401.zip'
,'2012/May/HOSArchive_20120501.zip'
,'2012/July/HOSArchive_20120701.zip'
,'2012/October/HOSArchive_20121001.zip'
,'2012/December/HOSArchive_20121201.zip'

,'2013/April/HOSArchive_20130401.zip'
,'2013/July/HOSArchive_20130701.zip'
,'2013/October/HOSArchive_20131001.zip'

,'2014/January/HOSArchive_20140101.zip'
,'2014/April/HOSArchive_20140417.zip'
,'2014/July/HOSArchive_20140717.zip'
,'2014/October/HOSArchive_20141023.zip'
,'2014/December/HOSArchive_20141218.zip'

,'2015/January/HOSArchive_20150122.zip'
,'2015/April/HOSArchive_20150416.zip'
,'2015/May/HOSArchive_20150506.zip'
,'2015/July/HOSArchive_20150716.zip'
,'2015/October/HOSArchive_20151008.zip'
,'2015/December/HOSArchive_20151210.zip'

,'2016/May/HOSArchive_20160504.zip'
,'2016/August/HOSArchive_20160810.zip'
,'2016/October/Hospital_20161110.zip'
]

fold_name = []

for f in file_list:
    url = "http://medicare.gov/download/HospitalCompare/" + f  
    file_name = url.split('/')[-1]
    fold = file_name[-12:-4]
    os.mkdir(path+fold)
    fold_name.append(fold)
    u = urllib.urlopen(url)
    z = zipfile.ZipFile(StringIO(u.read()))
    try:
        z.extract('Hospital.mdb', path+fold)
    except KeyError:
        z.extract('hospital.mdb', path+fold)
        

"""
['20050501', '20050901', '20051201', '20060301', '20060601', '20061201', '20070301',
 '20070601', '20070901', '20071201', '20080401', '20080801', '20081001', '20081201',
 '20090301', '20090701', '20090901', '20091201', '20100301', '20100601', '20100701',
 '20101001', '20101201', '20110401', '20110801', '20111001','20120101', '20120401', 
 '20120501', '20120701', '20121001', '20121201', '20130401', '20130701', '20131001',
 '20140101', '20140417', '20140717', '20141023', '20141218', '20150122', '20150416',
 '20150506', '20150716', '20151008', '20151210', '20160504', '20160810', '20161110']
"""
 
fold_name = []

file_list = [
'2012/July/HOSArchive_Revised_Flatfiles_20120701.zip'
,'2012/July/HOSArchive_Flatfiles_20120701.zip'
,'2012/October/HOSArchive_Revised_Flatfiles_20121001.zip'

,'2013/April/HOSArchive_Revised_Flatfiles_20130401.zip'
,'2013/April/HOSArchive_Flatfiles_20130401.zip'
,'2013/July/HOSArchive_Revised_Flatfiles_20130701.zip'
,'2013/October/HOSArchive_Revised_Flatfiles_20131001.zip'

,'2014/January/HOSArchive_Revised_Flatfiles_20140101.zip'
,'2014/April/HOSArchive_Revised_Flatfiles_20140417.zip'
,'2014/July/HOSArchive_Revised_Flatfiles_20140717.zip'
,'2014/October/HOSArchive_Revised_Flatfiles_20141023.zip'
,'2014/December/HOSArchive_Revised_Flatfiles_20141218.zip'

,'2015/January/HOSArchive_Revised_Flatfiles_20150122.zip'
,'2015/April/HOSArchive_Revised_Flatfiles_20150416.zip'
,'2015/May/HOSArchive_Revised_Flatfiles_20150506.zip'
,'2015/July/HOSArchive_Revised_FlatFiles_20150716.zip'
,'2015/October/HOSArchive_Revised_FlatFiles_20151008.zip'
,'2015/December/HOSArchive_Revised_FlatFiles_20151210.zip'

,'2016/May/HOSArchive_Revised_FlatFiles_20160504.zip'
,'2016/August/HOSArchive_Revised_FlatFiles_20160810.zip'
,'2016/October/Hospital_Revised_FlatFiles_20161110.zip'
]

for f in file_list:
    print f
    url = "http://medicare.gov/download/HospitalCompare/" + f  
    file_name = url.split('/')[-1]
    fold = file_name[:-4]
    os.mkdir(path+fold)
    fold_name.append(fold)
    u = urllib.urlopen(url)
    z = zipfile.ZipFile(StringIO(u.read()))
    z.extractall(path+fold)
 
""" 
['HOSArchive_Revised_Flatfiles_20120701',
 'HOSArchive_Flatfiles_20120701',
 'HOSArchive_Revised_Flatfiles_20121001',
 'HOSArchive_Revised_Flatfiles_20130401',
 'HOSArchive_Flatfiles_20130401',
 'HOSArchive_Revised_Flatfiles_20130701',
 'HOSArchive_Revised_Flatfiles_20131001',
 'HOSArchive_Revised_Flatfiles_20140101',
 'HOSArchive_Revised_Flatfiles_20140417',
 'HOSArchive_Revised_Flatfiles_20140717',
 'HOSArchive_Revised_Flatfiles_20141023',
 'HOSArchive_Revised_Flatfiles_20141218',
 'HOSArchive_Revised_Flatfiles_20150122',
 'HOSArchive_Revised_Flatfiles_20150416',
 'HOSArchive_Revised_Flatfiles_20150506',
 'HOSArchive_Revised_FlatFiles_20150716',
 'HOSArchive_Revised_FlatFiles_20151008',
 'HOSArchive_Revised_FlatFiles_20151210',
 'HOSArchive_Revised_FlatFiles_20160504',
 'HOSArchive_Revised_FlatFiles_20160810',
 'Hospital_Revised_FlatFiles_20161110'] 
""" 
 
 
#---------------------------------------------
#  The following code is run in python 32bit 
#---------------------------------------------
 
import pyodbc
import csv

MDB = 'C:/Users/junwan/Desktop/Projects/Hospital/data/'
DRV = '{Microsoft Access Driver (*.mdb, *.accdb)}'

folders = ['20050501', '20050901', '20051201', '20060301', '20060601', '20061201', '20070301',
 '20070601', '20070901', '20071201', '20080401', '20080801', '20081001', '20081201',
 '20090301', '20090701', '20090901', '20091201', '20100301', '20100601', '20100701',
 '20101001', '20101201', '20110401', '20110801', '20111001','20120101', '20120401', 
 '20120501', '20120701',             '20121201', '20130401', '20130701', '20131001',
 '20140101', '20140417','20140717', '20141023', '20141218', '20150122', '20150416',
 '20150506', '20150716', '20151008', '20151210', '20160504', '20160810', '20161110']

for folder in folders:
    print folder
    try:
        cnxn = pyodbc.connect('DRIVER={};DBQ={}'.format(DRV, MDB+folder+'/Hospital.mdb'))
    except KeyError:
        cnxn = pyodbc.connect('DRIVER={};DBQ={}'.format(DRV, MDB+folder+'/hospital.mdb'))
        
    cursor = cnxn.cursor()
    try:
        cursor.execute("SELECT * FROM HQI_HOSP")
    except:
        cursor.execute("SELECT * FROM dbo_vwHQI_HOSP")

    f = csv.writer(file(MDB+folder+'/hospital.csv', 'wb'))
    f.writerow([d[0] for d in cursor.description])
    for rows in cursor.fetchall():
        f.writerow([unicode(s).encode("utf-8") for s in rows])

 
 
 
