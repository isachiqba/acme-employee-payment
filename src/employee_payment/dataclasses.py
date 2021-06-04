from dataclasses import dataclass
from datetime import timedelta
from decimal import Decimal


@dataclass
class EmployeeShift:
    day: str
    start: timedelta
    end: timedelta


@dataclass
class Employee:
    name: str
    shifts: list[EmployeeShift]


@dataclass
class PaymentShift:
    rate: Decimal
    start: timedelta
    end: timedelta
