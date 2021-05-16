import os
from datetime import datetime as dt


def date_parser(input_string):
    return dt.strptime(input_string, "%Y-%m-%d")


def datetime_parser(input_string):
    return dt.strptime(input_string, "%Y-%m-%d %H:%M:%S")
    

def datetime_to_str(datetime):
    return f"{datetime.year}{str(datetime.month).zfill(2)}{str(datetime.day).zfill(2)}{str(datetime.hour).zfill(2)}{str(datetime.minute).zfill(2)}{str(datetime.second).zfill(2)}"


def date_to_str(date):
    return f"{date.year}{str(date.month).zfill(2)}{str(date.day).zfill(2)}000000"


def quote(input_string):
    return "\"" + input_string + "\""


def recode(file_path, source_encoding="utf-8", target_encoding="windows-1250"):
    """
    Changing file encoding shouldn't be necessary on Windows.
    """
    source = open(file_path, encoding=source_encoding)
    target = open(file_path + "_temp", "w", encoding=target_encoding)

    target.write(source.read().encode(target_encoding))
    source.close()
    target.close()
    os.remove(file_path)
    os.rename(file_path + "_temp", file_path)
    