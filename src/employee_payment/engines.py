import re
from decimal import Decimal

from .dataclasses import PaymentShift
from .settings import DEFAULT_PAYMENT_SCHEME
from .utils import period_to_timedelta_range


class EmployeePaymentEngine:

    PERIOD_REGEX = re.compile(r"(?P<hours>[0-9]{1,2}):(?P<minutes>[0-9]{1,2})")

    def __init__(self, scheme=DEFAULT_PAYMENT_SCHEME):
        self.scheme = {
            day: sorted(
                [
                    PaymentShift(rate=rate, **period_to_timedelta_range(period))  #
                    for period, rate in shifts.items()
                ],
                key=lambda pshift: (pshift.start, pshift.end),
            ) for day, shifts in scheme.items()
        }

    def get_payment(self, employee):
        return round(sum(self.__payment(eshift) for eshift in employee.shifts),2)

    def __payment(self, eshift):
        payment = Decimal(0)
        eshift_start = eshift.start
        for pshift in self.scheme.get(eshift.day, []):
            # (if)
            # - employee started working after the current payment-shift have started
            # (and)
            # - finished working before the current payment-shift have ended
            if pshift.start <= eshift_start and eshift.end <= pshift.end:
                payment += pshift.rate * Decimal((eshift.end - eshift_start).total_seconds()) / 3600
                return payment
            # (if)
            # - employee started working after the current payment-shift have started
            # (and)
            # - finished working after the current payment-shift have ended
            elif pshift.start <= eshift_start <= pshift.end:
                payment += pshift.rate * Decimal((pshift.end - eshift_start).total_seconds()) / 3600
                eshift_start = pshift.end
            # (if)
            # - employee started working before the current payment-shift have started
            # (and)
            # - finished working before the current payment-shift have ended
            elif pshift.start <= eshift.end <= pshift.end:
                payment += pshift.rate * Decimal((eshift.end - pshift.start).total_seconds()) / 3600
                return payment
            # (if)
            # - employee started working before the current payment-shift have started
            # (and)
            # - finished working after the current payment-shift have ended
            elif eshift_start <= pshift.start and pshift.end <= eshift.end:
                payment += pshift.rate * Decimal((pshift.end - pshift.start).total_seconds()) / 3600
                eshift_start = pshift.end
        return payment
