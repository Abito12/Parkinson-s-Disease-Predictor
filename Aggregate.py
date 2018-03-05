import os
import math
from datetime import datetime
import pandas as pd


def rms(x, y, z):
    return math.sqrt(x*x + y*y + z*z)

root = "UpdatedData"
#Add all the users here
Users = ["APPLE"]


for user in Users:
    path = os.path.join(root, user + "-hdl_accel_updated.csv")
    print(path)
    df = pd.read_csv(path)

    #Modify all X attribute values
    df['x.mean'] = df['x.mean'].apply(lambda x: float(x))
    df['x.absolute.deviation']  = df['x.absolute.deviation'].apply(lambda x: float(x))
    df['x.standard.deviation'] = df['x.standard.deviation'].apply(lambda x: float(x))
    df['x.max.deviation'] = df['x.max.deviation'].apply(lambda x: float(x))
    df['x.PSD.1'] = df['x.PSD.1'].apply(lambda x: float(x))
    df['x.PSD.3'] = df['x.PSD.3'].apply(lambda x: float(x))
    df['x.PSD.6'] = df['x.PSD.6'].apply(lambda x: float(x))
    df['x.PSD.10'] = df['x.PSD.10'].apply(lambda x: float(x))
    #print type(df['x.PSD.6'].iloc[0])

    #Modify all Y attribute values
    df['y.mean'] = df['y.mean'].apply(lambda x: float(x))
    df['y.absolute.deviation']  = df['y.absolute.deviation'].apply(lambda x: float(x))
    df['y.standard.deviation'] = df['y.standard.deviation'].apply(lambda x: float(x))
    df['y.max.deviation'] = df['y.max.deviation'].apply(lambda x: float(x))
    df['y.PSD.1'] = df['y.PSD.1'].apply(lambda x: float(x))
    df['y.PSD.3'] = df['y.PSD.3'].apply(lambda x: float(x))
    df['y.PSD.6'] = df['y.PSD.6'].apply(lambda x: float(x))
    df['y.PSD.10'] = df['y.PSD.10'].apply(lambda x: float(x))
    # print type(df['y.PSD.3'].iloc[0])

    #Modify all Z attribute values
    df['z.mean'] = df['z.mean'].apply(lambda x: float(x))
    df['z.absolute.deviation']  = df['z.absolute.deviation'].apply(lambda x: float(x))
    df['z.standard.deviation'] = df['z.standard.deviation'].apply(lambda x: float(x))
    df['z.max.deviation'] = df['z.max.deviation'].apply(lambda x: float(x))
    df['z.PSD.1'] = df['z.PSD.1'].apply(lambda x: float(x))
    df['z.PSD.3'] = df['z.PSD.3'].apply(lambda x: float(x))
    df['z.PSD.6'] = df['z.PSD.6'].apply(lambda x: float(x))
    df['z.PSD.10'] = df['z.PSD.10'].apply(lambda x: float(x))

    #print (df['time'].iloc[0])
    #Parse time attribute
    df['daytime'] = df['time'].apply(lambda x: datetime.strptime(x, '%Y-%m-%d %H:%M:%S'))
    df['day'] =  df['daytime'].apply(lambda x: x.day)
    df['time'] = df['daytime'].apply(lambda x: x.time()) #Object
    df['hour'] = df['daytime'].apply(lambda x: x.hour)
    df['minute'] = df['daytime'].apply(lambda x: x.minute)

    #Aggregate accelerometer data by second
    df_seconds = df.groupby(['daytime', 'day', 'time', 'hour','minute']).agg({
        'x.mean' : 'mean',
        'x.standard.deviation' : 'mean',
        'x.absolute.deviation' : 'mean',
        'x.max.deviation': 'mean',
        'x.PSD.1': 'mean',
        'x.PSD.3': 'mean',
        'x.PSD.6': 'mean',
        'x.PSD.10': 'mean',
        'y.mean' : 'mean',
        'y.standard.deviation' : 'mean',
        'y.absolute.deviation' : 'mean',
        'y.max.deviation': 'mean',
        'y.PSD.1': 'mean',
        'y.PSD.3': 'mean',
        'y.PSD.6': 'mean',
        'y.PSD.10': 'mean',
        'z.mean' : 'mean',
        'z.standard.deviation' : 'mean',
        'z.absolute.deviation' : 'mean',
        'z.max.deviation': 'mean',
        'z.PSD.1': 'mean',
        'z.PSD.3': 'mean',
        'z.PSD.6': 'mean',
        'z.PSD.10': 'mean'
    })

    df_seconds.to_csv('test.csv', sep='\t', encoding='utf-8')

'''

    #Aggregate accelerometer data by hour

    df_seconds['nsamples'] = 0

    df_hour = df_seconds.groupby(['day', 'hour']).agg({
        'nsamples' : 'count',
        'x.mean' : 'mean',
        'x.standard.deviation' : 'mean',
        'x.absolute.deviation' : 'mean',
        'x.max.deviation': 'mean',
        'x.PSD.1': 'mean',
        'x.PSD.3': 'mean',
        'x.PSD.6': 'mean',
        'x.PSD.10': 'mean',
        'y.mean' : 'mean',
        'y.standard.deviation' : 'mean',
        'y.absolute.deviation' : 'mean',
        'y.max.deviation': 'mean',
        'y.PSD.1': 'mean',
        'y.PSD.3': 'mean',
        'y.PSD.6': 'mean',
        'y.PSD.10': 'mean',
        'z.mean' : 'mean',
        'z.standard.deviation' : 'mean',
        'z.absolute.deviation' : 'mean',
        'z.max.deviation': 'mean',
        'z.PSD.1': 'mean',
        'z.PSD.3': 'mean',
        'z.PSD.6': 'mean',
        'z.PSD.10': 'mean'
    })
    df_hour  = df_hour[df_hour['nsamples'] >= 5]
    df_hour.to_csv('test1.csv', sep='\t', encoding='utf-8')
    df_hour = df_hour.reset_index()
    df_hour.to_csv('test2.csv', sep='\t', encoding='utf-8')
'''

# Take RMS of x-y-z channels
df_combinedxyz = pd.DataFrame()
df_combinedxyz['xyz.mean'] = df.apply(lambda x: rms(x['x.mean'], x['y.mean'], x['z.mean']), axis=1)
df_combinedxyz['xyz.absolute.deviation'] = df.apply(lambda x: rms(x['x.absolute.deviation'], x['y.absolute.deviation'], x['z.absolute.deviation']), axis=1)
df_combinedxyz['xyz.standard.deviation'] = df.apply(lambda x: rms(x['x.standard.deviation'], x['y.standard.deviation'], x['z.standard.deviation']), axis=1)
df_combinedxyz['xyz.max.deviation'] = df.apply(lambda x: rms(x['x.max.deviation'], x['y.max.deviation'], x['z.max.deviation']), axis=1)
df_combinedxyz['xyz.PSD.1'] = df.apply(lambda x: rms(x['x.PSD.1'], x['y.PSD.1'], x['z.PSD.1']), axis=1)
df_combinedxyz['xyz.PSD.3'] = df.apply(lambda x: rms(x['x.PSD.3'], x['y.PSD.1'], x['z.PSD.1']), axis=1)
df_combinedxyz['xyz.PSD.6'] = df.apply(lambda x: rms(x['x.PSD.6'], x['y.PSD.1'], x['z.PSD.1']), axis=1)
df_combinedxyz['xyz.PSD.10'] = df.apply(lambda x: rms(x['x.PSD.10'], x['y.PSD.1'], x['z.PSD.1']), axis=1)

df_combinedxyz.to_csv('.csv', sep='\t', encoding='utf-8')
