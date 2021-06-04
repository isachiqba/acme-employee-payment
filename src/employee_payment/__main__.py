import argparse

from employee_payment import EmployeePaymentEngine
from employee_payment import EmployeeScheduleParser


def entry_point():
    """
    Command-Line Interface entry-point, used when run as a script.
    """
    parser = argparse.ArgumentParser()
    parser.add_argument("infile", type=argparse.FileType("r"))
    args = parser.parse_args()

    try:
        engine = EmployeePaymentEngine()
        employees = EmployeeScheduleParser.get(infile=args.infile).parse()
        for employee in employees:
            print(f"The amount to pay {employee.name} is: {engine.get_payment(employee)} USD")
    except Exception as exc:
        parser.exit(1, f"{exc.__class__.__name__}: {exc}\n")
    finally:
        args.infile.close()
