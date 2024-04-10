from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from api.models import Course, Session_Year, Student, CustomUser, Staff, Subject, Session_Year, Staff_Notification, Staff_Leave, Staff_Feedback, Student_Notification, Student_Feedback, Student_Leave, Attendance, Attendance_Report
from django.contrib import messages


@login_required(login_url='/')
def Home(request):
    student_count = Student.objects.all().count()
    staff_count = Staff.objects.all().count()
    course_count = Course.objects.all().count()
    subject_count = Subject.objects.all().count()
    student_gender_male = Student.objects.filter(gender='Male').count()
    student_gender_female = Student.objects.filter(gender='Female').count()

    context = {
        'student_count': student_count,
        'staff_count': staff_count,
        'course_count': course_count,
        'subject_count': subject_count,
        'student_gender_male': student_gender_male,
        'student_gender_female': student_gender_female,
    }

    return render(request, 'Hod/home.html', context)


@login_required(login_url='/')
def addStudent(request):
    course = Course.objects.all()
    session_year = Session_Year.objects.all()

    if request.method == "POST":
        profile_pic = request.FILES.get('profile_pic')
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        email = request.POST.get('email')
        username = request.POST.get('username')
        password = request.POST.get('password')
        address = request.POST.get('address')
        gender = request.POST.get('gender')
        course_id = request.POST.get('course_id')
        session_year_id = request.POST.get('session_year_id')

        if CustomUser.objects.filter(email=email).exists():
            messages.warning(
                request, 'Email Is Already Taken , Please Enter Another Email Address')
            return redirect('addstudent')
        if CustomUser.objects.filter(username=username).exists():
            messages.warning(
                request, 'Username Is Already Taken , Please Enter Another UserName')
            return redirect('addstudent')
        else:
            user = CustomUser(
                first_name=first_name,
                last_name=last_name,
                username=username,
                email=email,
                profile_pic=profile_pic,
                user_type=3
            )
            user.set_password(password)
            user.save()

            course = Course.objects.get(id=course_id)
            session_year = Session_Year.objects.get(id=session_year_id)

            student = Student(
                admin=user,
                address=address,
                session_year_id=session_year,
                course_id=course,
                gender=gender,
            )
            student.save()
            messages.success(request, user.first_name + "  " +
                             user.last_name + " Are Successfully Added !")
            return redirect('viewstudent')

    context = {
        'course': course,
        'session_year': session_year,
    }

    return render(request, 'Hod/add_student.html', context)


@login_required(login_url='/')
def viewstudent(request):
    student = Student.objects.all()
    context = {
        'student': student,
    }
    return render(request, 'Hod/view_student.html', context)


@login_required(login_url='/')
def editStudent(request, id):
    student = Student.objects.filter(id=id)
    course = Course.objects.all()
    session_year = Session_Year.objects.all()

    context = {
        'student': student,
        'course': course,
        'session_year': session_year,
    }
    return render(request, 'Hod/edit_student.html', context)


@login_required(login_url='/')
def updatestudent(request):
    if request.method == "POST":
        student_id = request.POST.get('student_id')
        profile_pic = request.FILES.get('profile_pic')
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        email = request.POST.get('email')
        username = request.POST.get('username')
        password = request.POST.get('password')
        address = request.POST.get('address')
        gender = request.POST.get('gender')
        course_id = request.POST.get('course_id')
        session_year_id = request.POST.get('session_year_id')

        user = CustomUser.objects.get(id=student_id)

        user.first_name = first_name
        user.last_name = last_name
        user.email = email
        user.username = username

        if password != None and password != "":
            user.set_password(password)
        if profile_pic != None and profile_pic != "":
            user.profile_pic = profile_pic
        user.save()

        student = Student.objects.get(admin=student_id)
        student.address = address
        student.gender = gender

        course = Course.objects.get(id=course_id)
        student.course_id = course

        session_year = Session_Year.objects.get(id=session_year_id)
        student.session_year_id = session_year

        student.save()
        messages.success(request, 'Record Are Successfully Updated !')
        return redirect('viewstudent')

    return render(request, 'Hod/edit_student.html')


@login_required(login_url='/')
def deletestudent(request, admin):
    student = CustomUser.objects.get(id=admin)
    student.delete()
    messages.success(request, 'Record Are Successfully Deleted !')
    return redirect('viewstudent')


@login_required(login_url='/')
def addcourse(request):

    if request.method == "POST":
        course_name = request.POST.get('course_name')

        course = Course(
            name=course_name,
        )
        course.save()
        messages.success(request, 'Course Are Successfully Created ')

        # engine.say("course are successfully added")

        # engine.runAndWait()
        # engine.endLoop()
        # return redirect('view_course')
        return redirect(viewcourse)

    return render(request, 'Hod/add_course.html')


@login_required(login_url='/')
def viewcourse(request):
    course = Course.objects.all()
    context = {
        'course': course,
    }
    return render(request, 'Hod/view_course.html', context)


@login_required(login_url='/')
def editcourse(request, id):
    course = Course.objects.get(id=id)
    context = {
        'course': course,
    }
    return render(request, 'Hod/edit_course.html', context)


@login_required(login_url='/')
def updatecourse(request):
    if request.method == "POST":
        name = request.POST.get('name')
        course_id = request.POST.get('course_id')

        course = Course.objects.get(id=course_id)
        course.name = name
        course.save()
        messages.success(request, "Course Are Sucessfully Updated")
        return redirect('viewcourse')

    return render(request, 'Hod/edit_course.html')


@login_required(login_url='/')
def deletecourse(request, id):
    course = Course.objects.get(id=id)
    course.delete()
    messages.success(request, 'Course are Successfully Deleted')

    return redirect('viewcourse')


@login_required(login_url='/')
def addstaff(request):
    if request.method == "POST":
        profile_pic = request.FILES.get('profile_pic')
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        email = request.POST.get('email')
        username = request.POST.get('username')
        password = request.POST.get('password')
        address = request.POST.get('address')
        gender = request.POST.get('gender')

        if CustomUser.objects.filter(email=email).exists():
            messages.warning(
                request, 'Email Is Already Taken , Please Enter Another Email Address')
            return redirect('addstaff')
        if CustomUser.objects.filter(username=username).exists():
            messages.warning(
                request, 'Username Is Already Taken , Please Enter Another UserName')
            return redirect('addstaff')

        else:
            user = CustomUser(
                first_name=first_name,
                last_name=last_name,
                username=username,
                email=email,
                profile_pic=profile_pic,
                user_type=2
            )
            user.set_password(password)
            user.save()

            staff = Staff(
                admin=user,
                address=address,
                gender=gender
            )

            staff.save()
            messages.success(request, "Staff Are Added Sucessfully")
            return redirect('viewstaff')
    return render(request, 'Hod/add_staff.html')


@login_required(login_url='/')
def viewstaff(request):
    staff = Staff.objects.all()
    context = {
        'staff': staff,
    }
    return render(request, 'Hod/view_staff.html', context)


@login_required(login_url='/')
def editstaff(request, id):
    staff = Staff.objects.get(id=id)
    context = {
        'staff': staff,
    }
    return render(request, 'Hod/edit_staff.html', context)


@login_required(login_url='/')
def updatestaff(request):
    if request.method == "POST":
        staff_id = request.POST.get('staff_id')
        profile_pic = request.FILES.get('profile_pic')
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        email = request.POST.get('email')
        username = request.POST.get('username')
        password = request.POST.get('password')
        address = request.POST.get('address')
        gender = request.POST.get('gender')

        user = CustomUser.objects.get(id=staff_id)

        user.first_name = first_name
        user.last_name = last_name
        user.email = email
        user.username = username

        if password != None and password != "":
            user.set_password(password)
        if profile_pic != None and profile_pic != "":
            user.profile_pic = profile_pic

        user.save()

        staff = Staff.objects.get(admin=staff_id)
        staff.gender = gender
        staff.address = address

        staff.save()

        messages.success(request, 'Record Are Successfully Updated !')
        return redirect('viewstaff')

    return render(request, 'Hod/edit_staff.html')


@login_required(login_url='/')
def deletestaff(request, admin):
    staff = CustomUser.objects.get(id=admin)
    staff.delete()
    messages.success(request, 'Record Are Successfully Deleted !')
    return redirect('viewstaff')


@login_required(login_url='/')
def addsubject(request):

    course = Course.objects.all()
    staff = Staff.objects.all()

    if request.method == "POST":
        subject_name = request.POST.get('subject_name')
        course_id = request.POST.get('course_id')
        staff_id = request.POST.get('staff_id')

        course = Course.objects.get(id=course_id)
        staff = Staff.objects.get(id=staff_id)

        subject = Subject(
            name=subject_name,
            course=course,
            staff=staff
        )

        subject.save()
        messages.success(request, "Subject Is Added Sucessfully ")
        return redirect('viewsubject')

    context = {
        'course': course,
        'staff': staff,
    }

    return render(request, 'Hod/add_subject.html', context)


@login_required(login_url='/')
def viewsubject(request):
    subject = Subject.objects.all()
    context = {
        'subject': subject,
    }
    return render(request, 'Hod/view_subject.html', context)


@login_required(login_url='/')
def editsubject(request, id):
    subject = Subject.objects.get(id=id)
    course = Course.objects.all()
    staff = Staff.objects.all()
    context = {
        'subject': subject,
        'course': course,
        'staff': staff
    }
    return render(request, 'Hod/edit_subject.html', context)


@login_required(login_url='/')
def updatesubject(request):
    if request.method == "POST":
        subject_id = request.POST.get('subject_id')
        subject_name = request.POST.get('subject_name')
        course_id = request.POST.get('course_id')
        staff_id = request.POST.get('staff_id')

        try:
            subject = Subject.objects.get(id=subject_id)
        except Subject.DoesNotExist:
            messages.error(request, "Subject does not exist.")
            return redirect('viewsubject')

        course = Course.objects.get(id=course_id)
        staff = Staff.objects.get(id=staff_id)

        subject.id = subject_id
        subject.name = subject_name
        subject.course = course
        subject.staff = staff

        subject.save()

        messages.success(request, "Subject is updated successfully")
        return redirect('viewsubject')

    return render(request, 'Hod/edit_subject.html')


@login_required(login_url='/')
def deletesubject(request, id):
    subject = Subject.objects.filter(id=id)
    subject.delete()
    messages.success(request, 'Subject Is Successfully Deleted !')
    return redirect('viewsubject')


@login_required(login_url='/')
def addsession(request):
    if request.method == "POST":
        session_year_start = request.POST.get('session_year_start')
        session_year_end = request.POST.get('session_year_end')

        session = Session_Year(
            session_start=session_year_start,
            session_end=session_year_end
        )

        session.save()

        messages.success(request, "Session Is Sucessfully Added ")
        return redirect('viewsession')

    return render(request, 'Hod/add_session.html')


@login_required(login_url='/')
def viewsession(request):
    session = Session_Year.objects.all()
    context = {
        'session': session
    }
    return render(request, 'Hod/view_session.html', context)


@login_required(login_url='/')
def editsession(request, id):
    session = Session_Year.objects.filter(id=id)
    context = {
        'session': session
    }
    return render(request, 'Hod/edit_session.html', context)


@login_required(login_url='/')
def updatesession(request):
    if (request.method == "POST"):
        session_id = request.POST.get('session_id')
        session_year_start = request.POST.get('session_year_start')
        session_year_end = request.POST.get('session_year_end')

        session = Session_Year(
            id=session_id,
            session_start=session_year_start,
            session_end=session_year_end
        )
        session.save()
        messages.success(request, "Session Updated Sucessfully")
        return redirect('viewsession')

    return render(request, "Hod/view_session.html")


@login_required(login_url='/')
def deletesession(request, id):
    session = Session_Year.objects.get(id=id)
    session.delete()
    messages.success(request, "Session Deleted Sucessfully")
    return redirect('viewsession')


@login_required(login_url='/')
def staff_notification(request):
    staff = Staff.objects.all()
    see_notification = Staff_Notification.objects.all().order_by('-id')[0:5]
    context = {
        'staff': staff,
        'see_notification': see_notification,
    }
    return render(request, 'Hod/send_staff_notification.html', context)


@login_required(login_url='/')
def student_notification(request):
    student = Student.objects.all()
    notification = Student_Notification.objects.all()
    context = {
        'student': student,
        'notification': notification,
    }
    return render(request, 'Hod/send_student_notification.html', context)


@login_required(login_url='/')
def save_staff_notification(request):
    if request.method == "POST":
        message = request.POST.get('message')
        staff_id = request.POST.get('staff_id')

    staff = Staff.objects.get(admin=staff_id)
    notification = Staff_Notification(
        staff_id=staff,
        message=message,
    )
    notification.save()
    messages.success(request, "Notification Sent Sucessfully")
    return redirect('staff_notification')


@login_required(login_url='/')
def save_student_notification(request):
    if request.method == "POST":
        message = request.POST.get('message')
        student_id = request.POST.get('student_id')

        student = Student.objects.get(admin=student_id)
        notification = Student_Notification(
            student_id=student,
            message=message
        )
        notification.save()
        messages.success(request, "Notification Sent Successfully")
        return redirect('student_notification')


@login_required(login_url='/')
def LeaveStaffView(request):
    staff_leave = Staff_Leave.objects.all()
    context = {
        'staff_leave': staff_leave,
    }
    return render(request, 'Hod/staff_leave.html', context)


@login_required(login_url='/')
def LeaveStudentView(request):
    student_leave = Student_Leave.objects.all()
    context = {
        'student_leave': student_leave,
    }
    return render(request, 'Hod/student_leave.html', context)


@login_required(login_url='/')
def approveLeave(request, id):
    leave = Staff_Leave.objects.get(id=id)
    leave.status = 1
    leave.save()
    return redirect('staff_leave_view')


@login_required(login_url='/')
def approveLeaveStudent(request, id):
    leave = Student_Leave.objects.get(id=id)
    leave.status = 1
    leave.save()
    return redirect('student_leave_view')


@login_required(login_url='/')
def disapproveLeave(request, id):
    leave = Staff_Leave.objects.get(id=id)
    leave.status = 2
    leave.save()
    return redirect('staff_leave_view')


@login_required(login_url='/')
def disapproveLeaveStudent(request, id):
    leave = Student_Leave.objects.get(id=id)
    leave.status = 2
    leave.save()
    return redirect('student_leave_view')


@login_required(login_url='/')
def staff_feeadback(request):
    feedback = Staff_Feedback.objects.all()
    feedback_history = Staff_Feedback.objects.all().order_by('-id')[0:5]
    context = {
        'feedback': feedback,
        'feedback_history': feedback_history
    }
    return render(request, 'Hod/staff_feedback.html', context)


@login_required(login_url='/')
def student_feedback(request):
    feedback = Student_Feedback.objects.all()
    feedback_history = Student_Feedback.objects.all().order_by('-id')[0:5]
    context = {
        'feedback': feedback,
        'feedback_history': feedback_history
    }
    return render(request, 'Hod/student_feedback.html', context)


@login_required(login_url='/')
def staff_feeadback_reply(request):
    if request.method == "POST":
        feedback_id = request.POST.get('feedback_id')
        feedback_reply = request.POST.get('feedback_reply')
        feedback = Staff_Feedback.objects.get(id=feedback_id)
        feedback.feedback_reply = feedback_reply
        feedback.status = 1
        feedback.save()
        messages.success(request, "FeedBack Sent Successfully ")
        return redirect('staff_feedback_hod')


@login_required(login_url='/')
def student_feeadback_reply(request):
    if request.method == "POST":
        feedback_id = request.POST.get('feedback_id')
        feedback_reply = request.POST.get('feedback_reply')
        feedback = Student_Feedback.objects.get(id=feedback_id)
        feedback.feedback_reply = feedback_reply
        feedback.status = 1
        feedback.save()
        messages.success(request, "FeedBack Sent Successfully ")
        return redirect('student_feedback_hod')


@login_required(login_url='/')
def ViewAttendance(request):
    session_year = Session_Year.objects.all()
    subject = Subject.objects.all()
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

    return render(request, 'Hod/view_attendance.html', context)
