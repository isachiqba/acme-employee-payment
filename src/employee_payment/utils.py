import re
from datetime import timedelta

timedelta_default_regex = re.compile(r"(?P<hours>[0-9]{1,2}):(?P<minutes>[0-9]{1,2})")


def timedelta_from_string(string, regex=timedelta_default_regex):
    match = regex.match(string)
    return timedelta(**{key: int(val) for key, val in match.groupdict().items()})


def period_to_timedelta_range(period):
    parts = period.split("-", 1)
    start = timedelta_from_string(parts[0])
    end = timedelta(hours=24) if parts[1] == "00:00" else timedelta_from_string(parts[1])
    if start > end:
        raise ValueError(f"Invalid Period start='{start}' end='{end}'")
    return {
        "start": start,
        "end": end,
    }
