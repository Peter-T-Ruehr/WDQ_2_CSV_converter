# Example usage of windaq.py

# Import the library, if file is not within the same directory as your script use sys.path.append()
import windaq as wdq
import os
from pathlib import Path
import pandas as pd

# create directory to store output files
os.mkdir('./csv')

for file in os.listdir("."):
    if file.endswith(".WDQ"):
        # print(os.path.join(".", file))
        print("Converting " + file)
        # Path to sample windaq file, this is one of the sample files provided by Dataq when Windaq Waveform Browser is installed
        # f = 'F1_CF_1.WDQ' # 'AUTO.WDQ'

        # Open file
        wfile = wdq.windaq(file)

        # # Get channel 1 units
        # print(wfile.unit(1))

        # Read all data into a pandas Dataframe, this is my prefered way of working with data
        df = pd.DataFrame({'t':               wfile.time(),
                           'voltage':         wfile.data(1)})

        # print(df.head())

        # round time column - some have times e.g. like 0.15000000000000002 instead of 0.15
        df = df.round({'t': 2, 'voltage': 6})

        # multiply t by 1000 to get from seconds to milliseconds
        df.t *= 1000

        # write as CSV
        base = os.path.splitext(file)[0]
        file_name_out = './csv/' + base + '.csv'
        print("to " + file_name_out)
        # print(file_name_out)

        # file_name = './F1_CF_1.csv'
        df.to_csv(file_name_out, sep=',', index=False)

        # # Lets Plot it to make sure it looks like what Windaq Waveform Browser Shows
        # import matplotlib.pyplot as plt
        # fig = plt.figure(num=1, figsize=(16,9), dpi=80, facecolor='w', edgecolor='k')
        # plt.plot(df['t'], df['voltage'], label='voltage')
        # plt.show()
        
        print('*************************')
       
# remove pycache folder
os.popen('find . | grep -E "(__pycache__|\.pyc|\.pyo$)" | xargs rm -rf')
       
print('All done!')