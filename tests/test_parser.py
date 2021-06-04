import io

from pytest import raises

from employee_payment import EmployeeScheduleParser

sample = """
RENE=MO10:00-12:00,TU10:00-12:00,TH01:00-03:00,SA14:00-18:00,SU20:00-21:00
ASTRID=MO10:00-12:00,TH12:00-14:00,SU20:00-21:00
"""


def test_unsupported_parser():
    with raises(NotImplementedError):
        EmployeeScheduleParser.get(infile=io.StringIO(sample), fmt="json", ver=1)
    with raises(NotImplementedError):
        EmployeeScheduleParser.get(infile=io.StringIO(sample), fmt="txt", ver=2)


def test_supported_parser():
    employees = EmployeeScheduleParser.get(infile=io.StringIO(sample), fmt="txt", ver=1).parse()
    assert len(employees) == 2
    employee = employees[0]
    assert employee.name == "RENE"
    assert len(employee.shifts) == 5
    assert employee.shifts[0].day == "MO"
    assert employee.shifts[0].start.total_seconds() == 36000
    assert employee.shifts[0].end.total_seconds() == 43200
