# -*- coding: utf-8 -*-
"""
Created on Sat Apr  7 14:11:10 2018

@author: student
"""
import math
import pandas as pd
import json
import matplotlib.pyplot as plt


def clean(name):
    i = 1
    while (name.accelerometer[0]['x'] == name.accelerometer[i]['x']) {
        i++
    }
    return i;


def extract_cols(df):
    accel_x, accel_y, accel_z, gyro_x, gyro_y, gyro_z, orient_x, orient_y, orient_z = [], [], [], [], [], [], [], [], []
    extractions = [accel_x, accel_y, accel_z, gyro_x, gyro_y, gyro_z, orient_x, orient_y, orient_z]
    
    for i, row in df.iterrows():
        accel_x.append(row.accelerometer['x'])
        accel_y.append(row.accelerometer['y'])
        accel_z.append(row.accelerometer['z'])
        gyro_x.append(row.gyroscope['x'])
        gyro_y.append(row.gyroscope['y'])
        gyro_z.append(row.gyroscope['z'])
        orient_x.append(row.orientation['x'])
        orient_y.append(row.orientation['y'])
        orient_z.append(row.orientation['z'])
        
    dfe = pd.DataFrame(extractions)
    dfe = dfe.transpose()
    dfe.columns = ['accel_x', 'accel_y', 'accel_z', 'gyro_x', 'gyro_y', 'gyro_z', 'orient_x', 'orient_y', 'orient_z']
    return = pd.concat([df, dfe], axis=1)

#def plot_rolling_accel_x(df):
#    rolling = df['accel_x'].rolling(2, center=True)
#    
#    data = pd.DataFrame({'input': df['accel_x'],
#                         'one-year rolling_mean': rolling.mean(),
#                         'one-year rolling_std': rolling.std()})
#    ax = data.plot(style=['-', '--', ':'])
#    ax.lines[0].set_alpha(0.3)


data = json.load(open('data.json'))
test = json.load(open('test.json'))

df = pd.DataFrame(data)
dft = pd.DataFrame(test)

mod = clean(df)
modt = clean(dft)

df1 = df[df.index % mod == 0].reset_index(drop=True)
dft1 = dft[dft.index % modt == 0].reset_index(drop=True)

dft1 = dft1[dft1.index < df1.shape[0]]

df2 = extract_cols(df1)
dft2 = extract_cols(dft1)

#plot_rolling_accel_x(df2)
