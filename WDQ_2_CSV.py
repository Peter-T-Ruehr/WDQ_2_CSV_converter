'''
Created 2022-08-10

@author: Peter T. Rühr

based on a script by samper (https://github.com/sdp8483/windaq3)

Python 3
'''

# Import libraries and windaq.py. windaq.py must be in the same directory as this script
import windaq as wdq
import os
from pathlib import Path
import pandas as pd

# create directory to store output files
os.mkdir('./csv')

for file in os.listdir("."):
    if file.endswith(".WDQ"):
        print("Converting " + file)
        
        # Open file
        wfile = wdq.windaq(file)

        # # Get channel 1 units
        # print(wfile.unit(1))

        # Read all data into a pandas Dataframe
        df = pd.DataFrame({'t':               wfile.time(),
                           'voltage':         wfile.data(1)})

        # print(df.head())

        # # round time column - some have times e.g. like 0.15000000000000002 instead of 0.15
        # df = df.round({'t': 2, 'voltage': 6})

        # # multiply t by 1000 to get from seconds to milliseconds
        # df.t *= 1000

        # write as CSV
        base = os.path.splitext(file)[0]
        file_name_out = './csv/' + base + '.csv'
        print("to " + file_name_out)

        # file_name = './F1_CF_1.csv'
        df.to_csv(file_name_out, sep=',', index=False)

        # # Plot
        # import matplotlib.pyplot as plt
        # fig = plt.figure(num=1, figsize=(16,9), dpi=80, facecolor='w', edgecolor='k')
        # plt.plot(df['t'], df['voltage'], label='voltage')
        # plt.show()
        
        print('*************************')
       
# remove pycache folder
os.popen('pyclean .')
       
print('All done!')
