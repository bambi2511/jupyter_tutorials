import pandas as pd
import os
from urllib.request import urlretrieve

URL_FREMONT = 'https://data.seattle.gov/api/views/65db-xm6k/rows.csv?accessType=DOWNLOAD'

def get_fremont_data(filename='Fremont.csv',
                     url = URL_FREMONT,
                     force_download=False):
    """Download and cache the Fremont data

    Parameters
    ----------
    filename : string (optional)
               location to save the data
    url : string (optional)
          web location of the data
    force_download : bool (optional)
                     If True then force data download
    Returns
    -------
    data: pandas Dataframe
          the Fremont bridge data
    """
    if force_download or not os.path.exists(filename):
        urlretrieve(url, filename)
    data = pd.read_csv(filename, index_col='Date')
    try:
        data.index = pd.to_datetime(data.index, format='%m/%d/%Y %H:%M:%S %p')
    except TypeError:
        data.index = pd.to_datetime(data.index)
    data.columns = ['West', 'East']
    data['Total'] = data.West + data.East
    return data
