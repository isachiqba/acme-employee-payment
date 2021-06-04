import re
from typing import TextIO

from .dataclasses import Employee
from .dataclasses import EmployeeShift
from .utils import period_to_timedelta_range


class EmployeeScheduleParserTxt1:
    SHIFT_REGEX = re.compile(r"([A-Z]{2})([0-9]{1,2}:[0-9]{1,2}-[0-9]{1,2}:[0-9]{1,2})")

    def __init__(self, infile: TextIO):
        self.entries = infile.read().strip().splitlines()

    def parse(self):
        return [self.__parse(entry) for entry in self.entries]

    def __parse(self, entry: str):
        name, shifts = entry.split("=", 1)
        return Employee(
            name=name,
            shifts=[
                EmployeeShift(day=day, **period_to_timedelta_range(period))
                for day, period in self.SHIFT_REGEX.findall(shifts)
            ],
        )


class EmployeeScheduleParser:

    PARSERS = {
        "txt": {
            1: EmployeeScheduleParserTxt1,
        },
    }

    @classmethod
    def get(cls, *args, fmt="txt", ver=1, **kwargs):
        if fmt in cls.PARSERS and ver in cls.PARSERS[fmt]:
            return cls.PARSERS[fmt][ver](*args, **kwargs)
        raise NotImplementedError(f"ScheduleParser for fmt='{fmt}' and ver={ver}")
