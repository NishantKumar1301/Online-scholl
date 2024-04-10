from django.contrib import admin
from .models import CustomUser, Session_Year, Course, Student, Staff, Subject, Staff_Notification, Staff_Leave, Staff_Feedback, Student_Notification, Student_Feedback, Student_Leave, Attendance, Attendance_Report, StudentResult
from django.contrib.auth.admin import UserAdmin
# Register your models here.


class UserModel(UserAdmin):
    list_display = ['id', 'username', 'user_type']


admin.site.register(CustomUser, UserAdmin)


@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'created_at', 'updated_at']


@admin.register(Session_Year)
class SesssionAdmin(admin.ModelAdmin):
    list_display = ['id', 'session_start', 'session_end']


@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ['id', 'admin', 'gender']


@admin.register(Staff)
class StaffAdmin(admin.ModelAdmin):
    list_display = ['id', 'admin', 'address', 'gender']


@admin.register(Subject)
class SubjectAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'course', 'staff']


@admin.register(Staff_Notification)
class StaffNotificationAdmin(admin.ModelAdmin):
    list_display = ['id', 'staff_id', 'message', 'status']


@admin.register(Student_Notification)
class StudentNotificationAdmin(admin.ModelAdmin):
    list_display = ['id', 'student_id', 'message', 'status']


@admin.register(Staff_Leave)
class StaffLeaveAdmin(admin.ModelAdmin):
    list_display = ['id', 'data', 'message', 'status', 'created_at']


@admin.register(Student_Leave)
class StudentLeaveAdmin(admin.ModelAdmin):
    list_display = ['id', 'data', 'message', 'status', 'created_at']


@admin.register(Staff_Feedback)
class StaffFeedbackAdmin(admin.ModelAdmin):
    list_display = ['id', 'staff_id', 'feedback', 'created_at']


@admin.register(Student_Feedback)
class StudentFeedbackAdmin(admin.ModelAdmin):
    list_display = ['id', 'student_id', 'feedback', 'created_at']


@admin.register(Attendance)
class AttendanceAdmin(admin.ModelAdmin):
    list_display = ['id', 'subject_id', 'attendance_data', 'created_at']


@admin.register(Attendance_Report)
class AttendanceReportAdmin(admin.ModelAdmin):
    list_display = ['id', 'student_id', 'attendance_id']


@admin.register(StudentResult)
class ResultAdmin(admin.ModelAdmin):
    list_display = ['id', 'student_id', 'assignment_mark', 'exam_mark']
