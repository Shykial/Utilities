import datetime as dt
import re
from typing import Union

from decorators import timer


@timer
def delta_times(filepath_: str, time_delta_: dt.timedelta, time_format: str = '%H:%M:%S,%f',
                time_pattern: Union[re.Pattern, str] = re.compile(r'\d{2}:\d{2}:\d{2},\d{3}')):
    if type(time_pattern) != re.Pattern:
        time_pattern = re.compile(time_pattern)

    with open(filepath_, 'r') as f:
        contents = f.read()

    time_strs = time_pattern.findall(contents)

    for time_str in time_strs:
        old_time = dt.datetime.strptime(time_str, time_format)
        new_time = old_time + time_delta_
        new_time_str = new_time.strftime(time_format)[:-3]
        contents = contents.replace(time_str, new_time_str)

    with open(filepath_, 'w') as f:
        f.write(contents)
