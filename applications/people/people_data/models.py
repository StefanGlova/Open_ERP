from django.db import models


class Employee(models.Model):
    """
    Employee class define person, employee with given id,
    recorded first name, last name, address, phone, email,
    emergency contact and start date. End date is optional,
    and will only be recorded when employement ends with
    given employee.
    String representation of Employee class is employee's
    first name <space> employee's last name.
    """

    id = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    address = models.CharField(max_length=250)
    phone = models.CharField(max_length=20, unique=True)
    email = models.EmailField(max_length=100, unique=True)
    emergency_contact = models.CharField(max_length=250)
    employment_start_date = models.DateField()
    employment_end_date = models.DateField(null=True)

    def __str__(self):
        return f"Employee: {self.first_name} {self.last_name}"


class HolidayAllowance(models.Model):
    """
    Holiday Allowance class is used for record of holiday allowance
    for employee by their ID for given year. Holiday allowance is
    recorded in hours per year.
    """

    employee_ID = models.ForeignKey(Employee, on_delete=models.CASCADE)
    year = models.IntegerField()
    number_of_holiday_hours = models.IntegerField()


class HolidayRecords(models.Model):
    """
    HolidayRecords class is used for recording holidays used / booked
    by employee, using employee ID for given year. It records employee,
    year, date of holiday and number of hours for given day. There
    needs to be a new line for each day of holiday.
    """

    id = models.AutoField(primary_key=True)
    employee_ID = models.ForeignKey(Employee, on_delete=models.CASCADE)
    year = models.IntegerField()
    date = models.DateField()
    hours = models.IntegerField()


class AbsenceRecords(models.Model):
    """
    AbsenceRecords class is used for recording absence of employee.
    It records employee ID, year of abasence, date of absence, number
    of hours in given date and reason. There needs to be a new line
    for each day of absence.
    Business choice is boolean value, and is used to record whether
    absence was business decision or employee's decision. If business
    decision, it records True, if employee False. The record is then
    used for disciplinary purposes.
    Authorised is optional and should be recorded only if 'Business choise'
    is False. This then can be used for disciplinary purposes.
    """

    id = models.AutoField(primary_key=True)
    employee_ID = models.ForeignKey(Employee, on_delete=models.CASCADE)
    year = models.IntegerField()
    date = models.DateField()
    hours = models.IntegerField()
    reason = models.CharField(max_length=250)
    business_choice = models.BooleanField()
    authorised = models.BooleanField(null=True)


class Positions(models.Model):
    """
    Positions class is used to record different positions within
    the organisation. It records position title, description and
    position tier.
    Position tier is integer record which can be used for pay
    model, hierarchy model, etc.
    """

    id = models.AutoField(primary_key=True)
    position_title = models.CharField(max_length=100)
    position_description = models.CharField(max_length=250)
    position_tier = models.IntegerField()


class Shifts(models.Model):
    """
    Shifts model is used to record different shift patterns within
    organisation.
    It is then used in record of employee history for
    each individual employee.
    It is also used in ShiftCalendar class which is used for record
    of available working hours for given day, given hour and in
    combination with employee details, it gives position and
    can be used in production planning - labour.
    """

    id = models.AutoField(primary_key=True)
    shift_name = models.CharField(max_length=100)
    shift_description = models.CharField(max_length=250)


class EmploymentHistory(models.Model):
    """
    EmploymentHistory class records history of each individual employee,
    regarding their position and shift. For every position and shift, it
    records start date and optionally end date - only if position or / and
    shift is ended.
    For every change in either shift or position or both, it record new
    line in database.
    """

    employee_ID = models.ForeignKey(Employee, on_delete=models.CASCADE)
    position = models.ForeignKey(Positions, on_delete=models.CASCADE)
    shift = models.ForeignKey(Shifts, on_delete=models.CASCADE, null=True)
    position_start_date = models.DateField()
    position_end_date = models.DateField(null=True)


# class ShiftsCalendar(models.Model):
#     """
#     ShiftCalendar class records by year and date which shift is presented
#     at work place in every given hour.
#     """

#     year = models.IntegerField()
#     date = models.DateField()
#     zero_oclock = models.ForeignKey(Shifts, on_delete=models.DO_NOTHING, null=True)
#     one_oclock = models.ForeignKey(Shifts, on_delete=models.DO_NOTHING, null=True)
#     two_oclock = models.ForeignKey(Shifts, on_delete=models.DO_NOTHING, null=True)
#     three_oclock = models.ForeignKey(Shifts, on_delete=models.DO_NOTHING, null=True)
#     four_oclock = models.ForeignKey(Shifts, on_delete=models.DO_NOTHING, null=True)
#     five_oclock = models.ForeignKey(Shifts, on_delete=models.DO_NOTHING, null=True)
#     six_oclock = models.ForeignKey(Shifts, on_delete=models.DO_NOTHING, null=True)
#     seven_oclock = models.ForeignKey(Shifts, on_delete=models.DO_NOTHING, null=True)
#     eight_oclock = models.ForeignKey(Shifts, on_delete=models.DO_NOTHING, null=True)
#     nine_oclock = models.ForeignKey(Shifts, on_delete=models.DO_NOTHING, null=True)
#     ten_oclock = models.ForeignKey(Shifts, on_delete=models.DO_NOTHING, null=True)
#     eleven_oclock = models.ForeignKey(Shifts, on_delete=models.DO_NOTHING, null=True)
#     twelve_oclock = models.ForeignKey(Shifts, on_delete=models.DO_NOTHING, null=True)
#     thirteen_oclock = models.ForeignKey(Shifts, on_delete=models.DO_NOTHING, null=True)
#     fourteen_oclock = models.ForeignKey(Shifts, on_delete=models.DO_NOTHING, null=True)
#     fifteen_oclock = models.ForeignKey(Shifts, on_delete=models.DO_NOTHING, null=True)
#     sixteen_oclock = models.ForeignKey(Shifts, on_delete=models.DO_NOTHING, null=True)
#     seventeen_oclock = models.ForeignKey(Shifts, on_delete=models.DO_NOTHING, null=True)
#     eighteen_oclock = models.ForeignKey(Shifts, on_delete=models.DO_NOTHING, null=True)
#     nineteen_oclock = models.ForeignKey(Shifts, on_delete=models.DO_NOTHING, null=True)
#     twenty_oclock = models.ForeignKey(Shifts, on_delete=models.DO_NOTHING, null=True)
#     twenty_one_oclock = models.ForeignKey(Shifts, on_delete=models.DO_NOTHING, null=True)
#     twenty_two_oclock = models.ForeignKey(Shifts, on_delete=models.DO_NOTHING, null=True)
#     twenty_three_oclock = models.ForeignKey(Shifts, on_delete=models.DO_NOTHING, null=True)
