"""
URL configuration for elearning project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from . import views, Hod_Views, Staff_Views, Student_Views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('base/', views.Base, name="base"),
    path('', views.LOGIN, name='login'),
    path('doLogin/', views.doLogin, name='doLogin'),
    path('doLogout/', views.doLogout, name='logout'),

    # Profile path
    path('profile/', views.profile, name='profile'),
    path('profile/update/', views.profile_update, name='profile_update'),
    path('join/', Staff_Views.join_room, name='join_room'),

    # Hod path
    path('hod/home/', Hod_Views.Home, name='hod/home/'),
    path('hod/addstudent/', Hod_Views.addStudent, name='addstudent'),
    path('hod/viewstudent/', Hod_Views.viewstudent, name="viewstudent"),
    path('hod/editstudent/<str:id>', Hod_Views.editStudent, name="editstudent"),
    path('hod/updatestudent/', Hod_Views.updatestudent, name='updatestudent'),
    path('hod/deletestudent/<str:admin>',
         Hod_Views.deletestudent, name="deletestudent"),

    path('hod/addstaff/', Hod_Views.addstaff, name="addstaff"),
    path('hod/viewstaff/', Hod_Views.viewstaff, name="viewstaff"),
    path('hod/editstaff/<str:id>', Hod_Views.editstaff, name="editstaff"),
    path('hod/updatestaff/', Hod_Views.updatestaff, name='updatestaff'),
    path('hod/deletestaff/<str:admin>',
         Hod_Views.deletestaff, name="deletestaff"),



    path('hod/addcourse/', Hod_Views.addcourse, name='addcourse'),
    path('hod/viewcourse/', Hod_Views.viewcourse, name='viewcourse'),
    path('hod/editcouse/<str:id>', Hod_Views.editcourse, name="editcourse"),
    path('hod/updatecourse/', Hod_Views.updatecourse, name='updatecourse'),
    path('hod/deletecourse/<str:id>',
         Hod_Views.deletecourse, name="deletecourse"),

    path('hod/addsubject/', Hod_Views.addsubject, name='addsubject'),
    path('hod/viewsubject/', Hod_Views.viewsubject, name='viewsubject'),
    path('hod/editsubject/<str:id>', Hod_Views.editsubject, name="editsubject"),
    path('hod/updatesubject/', Hod_Views.updatesubject, name='updatesubject'),
    path('hod/deletesubject/<str:id>',
         Hod_Views.deletesubject, name="deletesubject"),

    path('hod/addsession/', Hod_Views.addsession, name="addsession"),
    path('hod/viewsession', Hod_Views.viewsession, name="viewsession"),
    path('hod/editsession/<str:id>', Hod_Views.editsession, name="editsession"),
    path('hod/updatesession/', Hod_Views.updatesession, name="updatesession"),
    path('hod/deletesession/<str:id>',
         Hod_Views.deletesession, name="deletesession"),

    path('hod/staff/send_notification/',
         Hod_Views.staff_notification, name="staff_notification"),
    path('hod/staff/save_notificaton/', Hod_Views.save_staff_notification,
         name="save_staff_notification"),

    path('hod/student/send_notification/',
         Hod_Views.student_notification, name="student_notification"),
    path('hod/student/save_notificaton/', Hod_Views.save_student_notification,
         name="save_student_notification"),

    path('Hod/Staff/Leave_View/', Hod_Views.LeaveStaffView, name="staff_leave_view"),
    path('hod/staff/approve_leave/<str:id>', Hod_Views.approveLeave,
         name="approve_staff_leave"),
    path('hod/staff/disapprove_leave/<str:id>', Hod_Views.disapproveLeave,
         name="disapprove_staff_leave"),
    path('Hod/Student/Leave_View/', Hod_Views.LeaveStudentView,
         name="student_leave_view"),
    path('hod/student/approve_leave/<str:id>', Hod_Views.approveLeaveStudent,
         name="approve_student_leave"),
    path('hod/student/disapprove_leave/<str:id>', Hod_Views.disapproveLeaveStudent,
         name="disapprove_student_leave"),

    path('hod/staff/feedback/', Hod_Views.staff_feeadback,
         name="staff_feedback_hod"),
    path('hod/staff/feedback_reply/', Hod_Views.staff_feeadback_reply,
         name="staff_feedback_reply_hod"),
    path('hod/student/feedback/', Hod_Views.student_feedback,
         name="student_feedback_hod"),
    path('hod/student/feedback_reply/', Hod_Views.student_feeadback_reply,
         name="student_feedback_reply_hod"),
    path('Hod/view_attendance/', Hod_Views.ViewAttendance,
         name="hod_view_attendance"),


    # Staff Url
    path('staff/home/', Staff_Views.home, name="staff_home"),
    path('Staff/Notification', Staff_Views.notification, name="notification"),
    path('Staff/MarkAsDone/<str:status>',
         Staff_Views.mark_as_done, name="mark_staff_done"),
    path('Staff/Leave/', Staff_Views.applyLeave, name="staff_apply_leave"),
    path('Staff/leave/Save/', Staff_Views.SaveLeave, name="save_staff_leave"),
    path('Staff/Feedback/', Staff_Views.Feedback, name="staff_feedback"),
    path('Staff/Feedback/save/', Staff_Views.Feedback_Save,
         name="save_staff_feedback"),
    path('Staff/Take_Attendance/',
         Staff_Views.TakeAttendance, name="staff_attendance"),
    path('Staff/Save_Attendance/', Staff_Views.SaveAttendance,
         name="save_staff_attendance"),
    path('Staff/view_attendance/', Staff_Views.View_Attendance,
         name="staff_view_attendance"),
    path('Staff/Add/Result/', Staff_Views.AddResult, name="add_result"),
    path('Staff/Save/Result/', Staff_Views.Save_Result, name="staff_save_result"),
    path('Staff/Class/Live/', Staff_Views.Take_Class, name="staff_live_class"),
    path('meeting/', Staff_Views.meeting, name="meeting"),


    # Student Url

    path('Student/home/', Student_Views.Home, name="student_home"),
    path('Student/Notification/', Student_Views.notification,
         name="notification_student_hod"),
    path('Student/MarkAsDone/<str:status>',
         Student_Views.mark_as_done, name="mark_student_done"),
    path('Student/Feedback/', Student_Views.Feedback, name="student_feedback"),
    path('Student/Feedback/save/', Student_Views.Feedback_Save,
         name="save_student_feedback"),
    path('Student/Leave/', Student_Views.applyLeave, name="student_apply_leave"),
    path('Student/leave/Save/', Student_Views.SaveLeave, name="save_student_leave"),
    path('Student/view_attendance/', Student_Views.View_Attendance,
         name="student_view_attendance"),
    path('Student/Result/View/', Student_Views.ViewResult,
         name="view_student_result"),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
