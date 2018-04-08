# -*- coding: utf-8 -*-
import math
import pandas as pd
import json

# joblib.dump(lin_reg, "linear_regression_model.pkl")


def clean(name):
    i = 1
    while name.accelerometer[0]['x'] == name.accelerometer[i]['x']:
        i += 1
    return i


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
    return pd.concat([df, dfe], axis=1)


def plot_rolling(df, col):
    rolling = df[col].rolling(2, center=True)

    data = pd.DataFrame({'input': df[col],
                         'rolling_mean': rolling.mean(),
                         'rolling_std': rolling.std()})
    ax = data.plot(style=['-', '--', ':'])
    ax.set_xticklabels(col)
    ax.lines[0].set_alpha(0.3)


def plot_dual_rolling(df, col):
    rolling_o = df[col].rolling(2, center=True)
    rolling_y = df[col+'_t'].rolling(2, center=True)

    data = pd.DataFrame({'original': rolling_o.mean(),
                         'yours': rolling_y.mean()})
    ax = data.plot(style=['-', '--'])
    ax.set_xticklabels(col)
    ax.lines[0].set_alpha(0.3)


def diff(name):
    cols = ['accel_x', 'accel_y', 'accel_z', 'gyro_x', 'gyro_y', 'gyro_z', 'orient_x', 'orient_y', 'orient_z']
    for col in cols:
        name[col+"_diff"] = name.apply(lambda x: x[col] - x[col+"_t"], axis=1)
    return name


def crits(name):
    cols = ['accel_x', 'accel_y', 'accel_z', 'gyro_x', 'gyro_y', 'gyro_z', 'orient_x', 'orient_y', 'orient_z']
    for col in cols:
        name[col+"_crits"] = abs(name[col]) > (2*dfagg[col]['std'] + dfagg[col]['mean'])
        name[col+"_t_crits"] = abs(name[col]) > (2*dfagg[col+'_t']['std'] + dfagg[col+'_t']['mean'])
#        name[col+"_t_crits"] = name.apply(lambda x: abs(x[col]) > (2*dfagg[col+'_t']['std'] + dfagg[col+'_t']['mean']), axis=1)
#        name[col+"_crits"] = name.apply(lambda x: abs(x[col]) > (2*dfagg[col]['std'] + dfagg[col]['mean']), axis=1)
    return name


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

test_cols = []
for col in list(dft2.columns):
    test_cols.append(col+"_t")
dft2.columns = test_cols

dfm = pd.concat([df2, dft2], axis=1)

plot_dual_rolling(dfm, 'accel_x')

dfmdiff = diff(dfm)
dfagg = dfmdiff.agg(['sum', 'min', 'max', 'mean', 'median', 'std'])

dfcrits = crits(dfm)
