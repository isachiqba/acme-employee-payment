from employee_payment import EmployeePaymentEngine
from employee_payment.dataclasses import Employee
from employee_payment.dataclasses import EmployeeShift as Shift
from employee_payment.settings import DEFAULT_PAYMENT_SCHEME
from employee_payment.utils import period_to_timedelta_range as period
from decimal import Decimal


def test_engine_shifts_empty():
    engine = EmployeePaymentEngine(scheme=DEFAULT_PAYMENT_SCHEME)
    assert engine.get_payment(Employee(name="name", shifts=[])) == 0

def test_engines_shifts_case1():
    # (if)
    # - employee started working after the current payment-shift have started
    # (and)
    # - finished working before the current payment-shift have ended
    engine = EmployeePaymentEngine(scheme=DEFAULT_PAYMENT_SCHEME)
    assert engine.get_payment(Employee(name="name", shifts=[Shift(day="MO", **period("10:00-12:00"))])) == Decimal('30')

def test_engines_shifts_case2():
    # (if)
    # - employee started working after the current payment-shift have started
    # (and)
    # - finished working after the current payment-shift have ended
    engine = EmployeePaymentEngine(scheme=DEFAULT_PAYMENT_SCHEME)
    assert engine.get_payment(Employee(name="name", shifts=[Shift(day="SU", **period("3:00-12:00"))])) ==  Decimal('239.67')

def test_engines_shifts_case3():
    # (if)
    # - employee started working before the current payment-shift have started
    # (and)
    # - finished working after the current payment-shift have ended
    engine = EmployeePaymentEngine(scheme=DEFAULT_PAYMENT_SCHEME)
    assert engine.get_payment(Employee(name="name", shifts=[Shift(day="SU", **period("6:00-00:00"))])) == Decimal('419.25')

def test_engines_shifts_case4():
    # (if)
    # - employee started working before the current payment-shift have started
    # (and)
    # - finished working before the current payment-shift have ended
    engine = EmployeePaymentEngine(scheme=DEFAULT_PAYMENT_SCHEME)
    assert engine.get_payment(Employee(name="name", shifts=[Shift(day="SU", **period("0:00-18:00")), Shift(day="M0", **period("0:00-18:00"))])) == Decimal('449.17')
