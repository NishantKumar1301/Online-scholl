from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from api.models import Session_Year, Student, Staff, Subject, Session_Year, Staff_Notification, Staff_Leave, Staff_Feedback, Attendance, Attendance_Report, StudentResult
from django.contrib import messages


def home(request):
    return render(request, 'Staff/home.html')


@login_required(login_url='/')
def notification(request):
    staff = Staff.objects.filter(admin=request.user.id)
    for i in staff:
        staff_id = i.id

        notification = Staff_Notification.objects.filter(staff_id=staff_id)
        context = {
            'notification': notification,
        }
        return render(request, 'Staff/notification.html', context)


@login_required(login_url='/')
def mark_as_done(request, status):
    notification = Staff_Notification.objects.get(id=status)
    notification.status = 1
    notification.save()
    return redirect('notification')


@login_required(login_url='/')
def applyLeave(request):
    staff = Staff.objects.filter(admin=request.user.id)
    for i in staff:
        staff_id = i.id

        staff_leave_history = Staff_Leave.objects.filter(staff_id=staff_id)
        context = {
            'staff_leave_history': staff_leave_history
        }
        return render(request, 'Staff/apply_leave.html', context)


@login_required(login_url='/')
def SaveLeave(request):
    if request.method == "POST":
        leave_date = request.POST.get('leave_date')
        leave_message = request.POST.get('leave_message')
        staff = Staff.objects.get(admin=request.user.id)

        leave = Staff_Leave(
            staff_id=staff,
            data=leave_date,
            message=leave_message
        )

        leave.save()
        messages.success(request, "Leave Sucessfully Sent")
        return redirect('staff_apply_leave')


@login_required(login_url='/')
def Feedback(request):
    staff_id = Staff.objects.get(admin=request.user.id)
    feedback_history = Staff_Feedback.objects.filter(staff_id=staff_id)

    context = {
        'feedback_history': feedback_history,
    }

    return render(request, 'Staff/feedback.html', context)


@login_required(login_url='/')
def Feedback_Save(request):
    if request.method == "POST":
        feedback = request.POST.get('feedback')
        staff = Staff.objects.get(admin=request.user.id)

        data = Staff_Feedback(
            staff_id=staff,
            feedback=feedback,
            feedback_reply="",
        )
        data.save()
        messages.success(request, "FeedBack Sent Successfully")
        return redirect('staff_feedback')


@login_required(login_url='/')
def TakeAttendance(request):
    staff_id = Staff.objects.get(admin=request.user.id)
    subject = Subject.objects.filter(staff=staff_id)
    session_year = Session_Year.objects.all()
    action = request.GET.get('action')
    get_session_year = None
    get_subject = None
    students = None

    if action is not None:
        if request.method == "POST":
            session_year_id = request.POST.get('session_year_id')
            subject_id = request.POST.get('subject_id')

            get_subject = Subject.objects.get(id=subject_id)
            get_session_year = Session_Year.objects.get(id=session_year_id)

            subject = Subject.objects.filter(id=subject_id)
            for i in subject:
                student_id = i.course.id
                students = Student.objects.filter(course_id=student_id)

    context = {
        'subject': subject,
        'session_year': session_year,
        'get_subject': get_subject,
        'get_session_year': get_session_year,
        'action': action,
        'students': students,
    }

    return render(request, 'Staff/attendance.html', context)


@login_required(login_url='/')
def SaveAttendance(request):
    if request.method == "POST":
        session_year_id = request.POST.get('session_year_id')
        subject_id = request.POST.get('subject_id')
        attendance_date = request.POST.get('attendance_date')
        student_id = request.POST.getlist('student_id')
        get_subject = Subject.objects.get(id=subject_id)
        get_session_year = Session_Year.objects.get(id=session_year_id)

        attendance = Attendance(
            subject_id=get_subject,
            attendance_data=attendance_date,
            session_year_id=get_session_year,
        )
        attendance.save()
        for i in student_id:
            stud_id = i
            int_stud = int(stud_id)

            p_student = Student.objects.get(id=int_stud)

            attendance_report = Attendance_Report(
                student_id=p_student,
                attendance_id=attendance,
            )

            attendance_report.save()
            messages.success(request, "Attendance Taken Successfully")

    return redirect('staff_view_attendance')


@login_required(login_url='/')
def View_Attendance(request):
    staff_id = Staff.objects.get(admin=request.user.id)
    session_year = Session_Year.objects.all()
    subject = Subject.objects.filter(staff_id=staff_id)
    action = request.GET.get('action')
    get_subject = None
    get_session_year = None
    attendance_date = None
    attendance_report = None

    if action is not None:
        if request.method == "POST":
            subject_id = request.POST.get('subject_id')
            session_year_id = request.POST.get('session_year_id')
            attendance_date = request.POST.get('attendance_date')

            get_subject = Subject.objects.get(id=subject_id)
            get_session_year = Session_Year.objects.get(id=session_year_id)
            attendance = Attendance.objects.filter(
                subject_id=get_subject, attendance_data=attendance_date)
            for i in attendance:
                attendance_id = i.id
                attendance_report = Attendance_Report.objects.filter(
                    attendance_id=attendance_id)

    context = {
        'subject': subject,
        'session_year': session_year,
        'action': action,
        'get_subject': get_subject,
        'get_session_year': get_session_year,
        'attendance_date': attendance_date,
        'attendance_report': attendance_report,
    }

    return render(request, 'Staff/view_attendance.html', context)


@login_required(login_url='/')
def AddResult(request):
    staff = Staff.objects.get(admin=request.user.id)

    subjects = Subject.objects.filter(staff_id=staff)
    session_year = Session_Year.objects.all()
    action = request.GET.get('action')
    get_subject = None
    get_session = None
    students = None
    if action is not None:
        if request.method == "POST":
            subject_id = request.POST.get('subject_id')
            session_year_id = request.POST.get('session_year_id')

            get_subject = Subject.objects.get(id=subject_id)
            get_session = Session_Year.objects.get(id=session_year_id)

            subjects = Subject.objects.filter(id=subject_id)
            for i in subjects:
                student_id = i.course.id
                students = Student.objects.filter(course_id=student_id)

    context = {
        'subjects': subjects,
        'session_year': session_year,
        'action': action,
        'get_subject': get_subject,
        'get_session': get_session,
        'students': students,
    }
    return render(request, 'Staff/add_result.html', context)


@login_required(login_url='/')
def Save_Result(request):
    if request.method == "POST":
        subject_id = request.POST.get('subject_id')
        session_year_id = request.POST.get('session_year_id')
        student_id = request.POST.get('student_id')
        assignment_mark = request.POST.get('assignment_mark')
        Exam_mark = request.POST.get('Exam_mark')

        get_student = Student.objects.get(admin=student_id)
        get_subject = Subject.objects.get(id=subject_id)

        check_exist = StudentResult.objects.filter(
            subject_id=get_subject, student_id=get_student).exists()
        if check_exist:
            result = StudentResult.objects.get(
                subject_id=get_subject, student_id=get_student)
            result.assignment_mark = assignment_mark
            result.exam_mark = Exam_mark
            result.save()
            messages.success(request, "Result Is Successfully Updated")
            return redirect('add_result')
        else:
            result = StudentResult(student_id=get_student, subject_id=get_subject, exam_mark=Exam_mark,
                                   assignment_mark=assignment_mark)
            result.save()
            messages.success(request, "Result Is Successfully Added")
            return redirect('add_result')


@login_required(login_url='/')
def Take_Class(request):
    return render(request, 'Staff/take_class.html', {'name': request.user.first_name})


@login_required(login_url='/')
def meeting(request):
    return render(request, 'Staff/videocall.html', {'name': request.user.first_name})


@login_required
def join_room(request):
    if request.method == 'POST':
        roomID = request.POST['roomID']
        return redirect("/meeting/?roomID=" + roomID)
    return render(request, 'joinroom.html')
