# DATAQ WinDaq WDQ to CSV converter

This project is based on the [windaq3](https://github.com/sdp8483/windaq3) DATAQ file importer by [Sam Perry](https://github.com/sdp8483). I have made no changes to that project's ``windaq.py`` (retrieved 2022-08-10) and used the ``example.ipynb`` (retrieved 2022-08-10) to create my ``WDQ_2_CSV.py``.

Here, I have added a loop to automatically convert all files with the ``*.WDQ`` into ``csv`` format and save them in in a subfolder called ``csv``. WinDaq ``*.WDQ`` is the proprietary, non-human readable file format of the [WinDaq Recording and Playback Software](https://www.dataq.com/products/windaq/).

This version was written to convert time series with two columns. Column one will be called ``t`` and column two ``voltage``. These names can be changed in the lines starting from ``df = pd.DataFrame({`` and new column names can be added there, too.

Before proceeding, make sure you have ``Python 3`` correctly installed.

## Obligatory installation of ``pyclean``
This is a convenient addition to remove the ``\_\_pycache\_\_`` after running the script. It is, however, not mandatory. If you do not install ``pyclean``, the script will end successfully, but with an error message.
  * if ``pip`` is not installed yet, install it from [here](https://pip.pypa.io/en/stable/installation/)
  * run ``pip install pyclean`` in a command prompt to install pyclean

## Usage
  * place the files ``WDQ_2_CSV.py`` and ``windaq.py`` in the same folder as your ``*.WDQ`` files
  * open a command prompt in that folder (e.g. by typing ``cmd`` in the Explorer address bar)
  * run the conversion script via the command ``python WDQ_2_CSV.py`` in the command prompt
 
 ## Operating systems
 Tested with Python 3.9 on a Windows 10 machine for files recorded with a DATAQ DI-149 data acquisition device.
