from builtins import int
import pandas as pd
from datetime import datetime
def excel_time_2_string(excel_time):
    t = pd.to_datetime('1899-12-30') + pd.to_timedelta(excel_time,'D')
    return t.strftime('%d.%m.%Y')

def excel_time_2_ay(excel_time):
    '''
    converts excel float format to pandas datetime object
    then converts to month as integer
    '''
    t = pd.to_datetime('1899-12-30') + pd.to_timedelta(excel_time,'D')
    return t.strftime('%m')

def excel_time_2_gun(excel_time):
    '''
    converts excel float format to pandas datetime object
    then converts to day as integer
    '''
    t = pd.to_datetime('1899-12-30') + pd.to_timedelta(excel_time,'D')
    return t.strftime('%d')

def str_to_day(day):
    dummy = datetime.strptime(day,'%d.%m.%Y')
    epoch_time = datetime.timestamp(dummy)
    day = epoch_time/(3600*24)
    return day

def difference(a,b):
    difference = str_to_day(a)-str_to_day(b)
    return int(difference)
