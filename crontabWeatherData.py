
"""
Created on Mon Oct 03 12:47:56 2016

@author: junwan

crontab -e

0 22 * * * /home/jun/anaconda2/bin/python /home/jun/Documents/GL/weather/weather.py
"""

import pandas as pd
import numpy as np

from geopy.geocoders import Nominatim
import geopy
import logging
 
path = '/home/jun/Documents/GL/weather/'
 
logging.basicConfig(format="[%(asctime)s] %(levelname)s\t%(message)s",
                     filename=path + "weather.log",
                     filemode='a',
                     level=logging.DEBUG,
                     datefmt='%m/%d/%y %H:%M:%S')
formatter = logging.Formatter("[%(asctime)s] %(levelname)s\t%(message)s", datefmt='%m/%d/%y %H:%M:%S')
console = logging.StreamHandler()
console.setFormatter(formatter)
console.setLevel(logging.INFO)
logging.getLogger().addHandler(console)
 
logger = logging.getLogger(__name__)
 
'''
df = pd.read_csv(path + 'ghcnd_stations.csv')

len(df.state.unique())
st = ['AL','AK','AZ','AR','CA','CO','CT','DE','FL','GA','HI','ID','IL','IN','IA','KS','KY','LA','ME','MD','MA','MI','MN','MS','MO','MT','NE','NV','NH','NJ','NM','NY','NC','ND','OH','OK','OR','PA','RI','SC','SD','TN','TX','UT','VT','VA','WA','WV','WI','WY']


df_us = df[df.state.isin(st)]

df.to_csv(path + 'us_stations.csv')
'''

logger.info("...loading current station data...")
df = pd.read_csv(path + 'us_stations.csv')
df = df[['id','latitude','longitude','state']]
logger.info("Current station data has %d Columns and %d Rows",df.shape[0], df.shape[1])

df_us = df[:5000]

df = df[5000:]
logger.info("New station data has %d Columns and %d Rows",df.shape[0], df.shape[1])
logger.info("...saving new station data...")
df.to_csv(path + 'us_stations.csv')

logger.info("...reverse geocoding...")
logger.info("reversing %d records...",df_us.shape[0])

lat = list(df_us['latitude'])
lng = list(df_us['longitude'])

postalcode=[]
county=[]
for i in range(df_us.shape[0]):
    g =geocoder.google([lat[i], lng[i]], method='reverse')
    postalcode.append(g.postal)
    county.append(g.county)

df_us['zipcode'] = postalcode
df_us['county'] = county

logger.info("...loading current zipcode data...")
zipcode = pd.read_csv(path + 'zipcode.csv')
zipcode = zipcode[['id', 'latitude', 'longitude', 'state', 'zipcode','county']]
logger.info("Current zipcode data has %d Columns and %d Rows",zipcode.shape[0], zipcode.shape[1])


zipcode = zipcode.append(df_us)
logger.info("New zipcode data has %d Columns and %d Rows",zipcode.shape[0], zipcode.shape[1])

logger.info("...saving new zipcode data...")
zipcode.to_csv(path + 'zipcode.csv')


