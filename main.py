# -*- coding: utf-8 -*-
"""
Created on Sun May  2 13:38:13 2021

@author: louis
"""

#import math
#from PIL import Image
#from cimage import *
#import turtle
import gmaps
import gmaps.datasets

gmaps.configure(api_key='AIzaSyBweyv6KcCMpgd-lfa1GDNYkKHAU5o6fIM')

earthquake_df = gmaps.datasets.load_dataset_as_df('earthquakes')
earthquake_df.head()

locations = earthquake_df[['latitude', 'longitude']]
weights = earthquake_df['magnitude']
fig = gmaps.figure()
fig.add_layer(gmaps.heatmap_layer(locations, weights = weights))
fig