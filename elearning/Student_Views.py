from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from api.models import Student, Subject, Student_Notification, Student_Feedback, Student_Leave, Attendance_Report, StudentResult
from django.contrib import messages


@login_required(login_url='/')
def Home(request):
    return render(request, 'Student/home.html', {'name': request.user.first_name})


@login_required(login_url='/')
def notification(request):
    student = Student.objects.filter(admin=request.user.id)
    for i in student:
        student_id = i.id

        notification = Student_Notification.objects.filter(
            student_id=student_id)
        context = {
            'notification': notification,
        }
        return render(request, 'Student/notification.html', context)


@login_required(login_url='/')
def mark_as_done(request, status):
    notification = Student_Notification.objects.get(id=status)
    notification.status = 1
    notification.save()
    return redirect('notification_student_hod')


@login_required(login_url='/')
def Feedback(request):
    student_id = Student.objects.get(admin=request.user.id)
    feedback_history = Student_Feedback.objects.filter(student_id=student_id)

    context = {
        'feedback_history': feedback_history,
    }

    return render(request, 'Student/feedback.html', context)


@login_required(login_url='/')
def Feedback_Save(request):
    if request.method == "POST":
        feedback = request.POST.get('feedback')
        student = Student.objects.get(admin=request.user.id)

        data = Student_Feedback(
            student_id=student,
            feedback=feedback,
            feedback_reply="",
        )
        data.save()
        messages.success(request, "FeedBack Sent Successfully")
        return redirect('student_feedback')


@login_required(login_url='/')
def applyLeave(request):
    student = Student.objects.filter(admin=request.user.id)
    for i in student:
        student_id = i.id

        student_leave_history = Student_Leave.objects.filter(
            student_id=student_id)
        context = {
            'student_leave_history': student_leave_history
        }
    return render(request, 'Student/apply_leave.html', context)


@login_required(login_url='/')
def SaveLeave(request):
    if request.method == "POST":
        leave_date = request.POST.get('leave_date')
        leave_message = request.POST.get('leave_message')
        student = Student.objects.get(admin=request.user.id)

        leave = Student_Leave(
            student_id=student,
            data=leave_date,
            message=leave_message
        )

        leave.save()
        messages.success(request, "Leave Sucessfully Sent")
        return redirect('student_apply_leave')


@login_required(login_url='/')
def View_Attendance(request):
    student = Student.objects.get(admin=request.user.id)
    subjects = Subject.objects.filter(course=student.course_id)
    action = request.GET.get('action')
    get_subject = None
    attendance_report = None

    if action is not None:
        if request.method == "POST":
            subject_id = request.POST.get('subject_id')

            get_subject = Subject.objects.get(id=subject_id)
            attendance_report = Attendance_Report.objects.filter(
                student_id=student, attendance_id__subject_id=subject_id)

    context = {
        'subjects': subjects,
        'action': action,
        'get_subject': get_subject,
        'attendance_report': attendance_report,
    }

    return render(request, 'Student/view_attendance.html', context)


@login_required(login_url='/')
def ViewResult(request):
    student = Student.objects.get(admin=request.user.id)
    results = StudentResult.objects.filter(student_id=student)

    results_with_grades = []

    grade_class_mapping = {
        'A+': 'success',
        'A': 'primary',
        'B': 'info',
        'C': 'warning',
        'D': 'danger',
        'P': 'secondary',
        'BackLog': 'dark'
    }

    for result in results:
        assignment_mark = result.assignment_mark
        exam_mark = result.exam_mark

        total_mark = assignment_mark + exam_mark

        if total_mark >= 90:
            grade = 'A+'
        elif total_mark >= 80:
            grade = 'A'
        elif total_mark >= 70:
            grade = 'B'
        elif total_mark >= 60:
            grade = 'C'
        elif total_mark >= 50:
            grade = 'D'
        elif total_mark >= 33:
            grade = 'P'
        else:
            grade = 'BackLog'

        grade_class = grade_class_mapping.get(grade, 'dark')

        results_with_grades.append((result, grade, grade_class))

    context = {
        'results_with_grades': results_with_grades,
    }

    return render(request, 'Student/view_result.html', context)
