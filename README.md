## **Exercise**

The company ACME offers their employees the flexibility to work the hours they want. They will pay for the hours worked based on the day of the week and time of day, according to the following table:

| Monday - Friday      |
| -------------------- |
| 00:01 - 09:00 25 USD |
| 09:01 - 18:00 15 USD |
| 18:01 - 00:00 20 USD |
| Saturday and Sunday  |
| 00:01 - 09:00 30 USD |
| 09:01 - 18:00 20 USD |



The goal of this exercise is to calculate the total that the company has to pay an employee, based on the hours they worked and the times during which they worked. The following abbreviations will be used for entering data:

|               |
| ------------- |
| MO: Monday    |
| TU: Tuesday   |
| WE: Wednesday |
| TH: Thursday  |
| FR: Friday    |
| SA: Saturday  |
| SU: Sunday    |



Input: the name of an employee and the schedule they worked, indicating the time and hours. This should be a .txt file with at least five sets of data. You can include the data from our two examples below.

Output: indicate how much the employee has to be paid

For example:

Case 1:

INPUT

RENE=MO10:00-12:00,TU10:00-12:00,TH01:00-03:00,SA14:00-18:00,SU20:00-21:00

OUTPUT:

The amount to pay RENE is: 215 USD

Case 2:

INPUT

ASTRID=MO10:00-12:00,TH12:00-14:00,SU20:00-21:00

OUTPUT:

The amount to pay ASTRID is: 85 USD

## Solution

The solution is an installable Python package. It has a command line interface.

It is a decoupled solution, ready for the expansion of its components.

**Entry Point:** It is in charge of reading the file and executing the payment method passing each employee.
**EmployeeScheduleParser**: In charge of analyzing employee data. In the implementation, the Builder design pattern was applied, the creation of an EmployeeScheduleParser object to return a specific implementation of an EmployeeScheduleParser according to the parameters with which it is desired to build.
**EmployeePaymentEngine**: Manages the payment of the employee according to the schedule he wants to work with, completely flexible for a change of schedule.
All possible cases are taken into account when calculating an employee's salary:

1) All employee working hours included in the same shift.
2) The employee's working hours begin on one shift and end on the next.
3) The employee's working time does not start on any specific shift, but ends on a valid shift.
4) Work hours include multiple shifts.

Use of regular expressions for data analysis.
Use of data class for data manipulation.

>

> **`Python 3`**  is required.

```shell
git clone ...
cd acme-employee-payment
python -m venv .venv
source .venv/bin/activate
pip install .

# cleanup
deactivate
rm -rf .venv
```

### Usage

```shell
employee-payment <INPUT>
```
