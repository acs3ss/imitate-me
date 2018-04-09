# -*- coding: utf-8 -*-
import pandas as pd
import json
from scipy.spatial.distance import euclidean
from fastdtw import fastdtw
from sklearn import preprocessing

cols = ['accel_x', 'accel_y', 'accel_z', 'gyro_x', 'gyro_y', 'gyro_z', 'orient_x', 'orient_y', 'orient_z']
weights = [21, 20, 20, 5, 5, 5, 8, 8, 8]


def get_dtw(x, y):
    distance, path = fastdtw(x, y, dist=euclidean)
    return distance


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
    dfe.columns = cols
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
    for col in cols:
        name[col+"_diff"] = name.apply(lambda x: x[col] - x[col+"_t"], axis=1)
    return name


def crits(name, agg):
    for col in cols:
        name[col+"_crits"] = abs(name[col]) > (2*agg[col]['std'] + agg[col]['mean'])
        name[col+"_t_crits"] = abs(name[col]) > (2*agg[col+'_t']['std'] + agg[col+'_t']['mean'])
        name[col+"_crits"] = name[col+"_crits"].astype(int)
        name[col+"_t_crits"] = name[col+"_t_crits"].astype(int)
    return name


def comp_crits(name):
    for col in cols:
        name[col+"_crits_roll"] = name[col+"_crits"].rolling(4, win_type='triang').sum()
        name[col+"_t_crits_roll"] = name[col+"_t_crits"].rolling(4, win_type='triang').sum()
    return name


#def aligned_crits(name):
#    for col in cols:
#        name[col+"_crits_roll_same"] = name.apply(lambda x: help_align(x, col))
#    return name
#
#
#def help_align(row, col):
#    if row[col+"_t_crits_roll"] != 0 and row[col+"_crits_roll"] != 0:
#        print('yup')
#        return row[col+"_crits_roll"] + row[col+"_t_crits_roll"]
#    else:
#        print('nope')
#        return 0
#
#
#def get_aligned(name):
#    total = 0
#    for col in cols:
#        total += name[col+"_crits_roll"] + name[col+"_t_crits_roll"] if (name[col+"_t_crits_roll"] > 0) & (name[col+"_crits_roll"] > 0) else 0;
#    return total
#
#
#def better_align(name):
#    count = []
#    for col in cols:
#        count.append(name[(name[col+"_crits_roll"] > 0) & (name[col+"_t_crits_roll"] > 0)].count())
#    return count


def analyze(jsondata, filetest):
    if type(jsondata) != 'json':
        data = json.load(open('../data/data.json'))
    else:
        data = jsondata
    test = json.load(open('../data/' + filetest))

    df = pd.DataFrame(data)
    dft = pd.DataFrame(test)

    mod = clean(df)
    modt = clean(dft)

    df1 = df[df.index % mod == 0].reset_index(drop=True)
    dft1 = dft[dft.index % modt == 0].reset_index(drop=True)

    dft1 = dft1[dft1.index < df1.shape[0]]
    df1 = df1[df1.index < dft1.shape[0]]

    df2 = extract_cols(df1)
    dft2 = extract_cols(dft1)

    test_cols = []
    for col in list(dft2.columns):
        test_cols.append(col+"_t")
    dft2.columns = test_cols

    dfm = pd.concat([df2, dft2], axis=1)
    dfm = dfm.drop(['accelerometer', 'gyroscope', 'orientation', 'accelerometer_t', 'gyroscope_t', 'orientation_t'], axis=1)

    dfscaled = pd.DataFrame(preprocessing.MinMaxScaler().fit_transform(dfm.values))
#    dfscaled.columns = cols+test_cols[3:]+[col+"_diff" for col in cols]
    dfscaled.columns = cols+test_cols[3:]

#    plot_dual_rolling(dfm, 'accel_x')

    dfmdiff = diff(dfm)
    dfagg = dfmdiff.agg(['sum', 'min', 'max', 'mean', 'median', 'std'])

    def why(x):
        try:
            return x['mean']/max(abs(x['min']), x['max'])
        except:
            return 0

#    dfcrits = crits(dfm, dfagg)
#    dfcritsroll = comp_crits(dfcrits)
    dfaggstd = dfagg.apply(lambda x: why(x), axis=0)

    dfaggstd = dfaggstd.drop(cols+test_cols[3:])

    total = 0
    dtw = 0
    i = 0
    for i, col in enumerate(cols):
        to_add = abs(dfaggstd[i])
        total += to_add*weights[i]
        to_add_dtw = get_dtw(dfscaled[col].values, dfscaled[col+'_t'].values)
        dtw += to_add_dtw*weights[i]
    dtw /= 100*dfscaled.shape[0]
    total /= 10
    result = (2- dtw - total)
    print(dtw)
    print(total)
    return result

#print(analyze('yo', "test.json"))
