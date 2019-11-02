from django.db import models


# Create your models here.
class Professor(models.Model):
    first_name = models.CharField(max_length=64, null=True, blank=True)
    last_name = models.CharField(max_length=64, null=True, blank=True)
    webpage = models.CharField(max_length=64, null=True, blank=True)
    username = models.CharField(max_length=64, null=True, blank=True)
    password = models.CharField(max_length=255, null=True, blank=True)


class Department(models.Model):
    name = models.CharField(max_length=64, null=True, blank=True)
    abbreviation = models.CharField(max_length=8, null=True, blank=True)


class Student(models.Model):
    username = models.CharField(max_length=64, null=True, blank=True)
    password = models.CharField(max_length=255, null=True, blank=True)
    first_name = models.CharField(max_length=64, null=True, blank=True)
    last_name = models.CharField(max_length=64, null=True, blank=True)
    department = models.ForeignKey(Department, null=True, on_delete=models.SET_NULL)
    year = models.SmallIntegerField()
    group = models.SmallIntegerField()
    semigroup = models.SmallIntegerField()


class Subject(models.Model):
    MANDATORY = "MANDATORY"
    OPTIONAL = "OPTIONAL"
    TYPES = (
        (MANDATORY, "MANDATORY"),
        (OPTIONAL, "OPTIONAL"),
    )
    name = models.CharField(max_length=128, null=True, blank=True)
    type = models.CharField(choices=TYPES, default="OPTIONAL", max_length=15)
    professor = models.ForeignKey(Professor, on_delete=models.SET_NULL, null=True)
    description = models.TextField(null=True, blank=True)
    credits_number = models.IntegerField()
    semester = models.IntegerField()


class Enrollment(models.Model):
    subject = models.ForeignKey(Subject, models.DO_NOTHING)
    student = models.ForeignKey(Student, models.DO_NOTHING)

    class Meta:
        unique_together = (('subject', 'student'),)


class News(models.Model):
    subject = models.ForeignKey(Subject, models.DO_NOTHING)
    content = models.TextField(null=True, blank=True)
    date_time = models.DateTimeField()


class Location(models.Model):
    name = models.CharField(max_length=64)
    address = models.CharField(max_length=128)
    latitude = models.FloatField()
    longitude = models.FloatField()


class Room(models.Model):
    number = models.CharField(max_length=32)
    indoor_directions = models.CharField(max_length=128)
    location = models.ForeignKey(Location, models.DO_NOTHING)


class TimeTable(models.Model):
    COURSE = "COURSE"
    LABORATORY = "LABORATORY"
    SEMINARY = "SEMINARY"
    TYPES = (
        (COURSE, "COURSE"),
        (SEMINARY, "SEMINARY"),
        (LABORATORY, "LABORATORY"),
    )
    days_of_week = models.SmallIntegerField()
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    frequency = models.SmallIntegerField()
    type = models.CharField(choices=TYPES, default="COURSE", max_length=15)
    room = models.ForeignKey(Room, models.DO_NOTHING)
    subject = models.ForeignKey(Subject, models.DO_NOTHING)
    formation = models.CharField(max_length=8)


class SubjectActivity(models.Model):
    subject = models.ForeignKey(Subject, models.DO_NOTHING)


class Assignemnt(models.Model):
    subject_activity = models.ForeignKey(SubjectActivity, models.DO_NOTHING)


class Attendance(models.Model):
    student = models.ForeignKey(Student, models.CASCADE)
    subject_activity = models.ForeignKey(SubjectActivity, models.DO_NOTHING)


class Leave(models.Model):
    attendance = models.ForeignKey(Attendance, models.DO_NOTHING)
    # image = models.ImageField() mai specific ?


class StudentAssignments(models.Model):
    student = models.ForeignKey(Student, models.DO_NOTHING)
    assignemnt = models.ForeignKey(Assignemnt, models.DO_NOTHING)
