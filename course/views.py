from django.shortcuts import render

import json


from modules.quiz_processor.quiz_processor import QuizProcessor
from modules.markdown_processor.markdown_processor import MarkdownProcessor
from modules.progress_db_processor.progress_db_processor import ProgressDBProcessor
from modules.course_catalog_manager.course_catalog_manager import CourseCatalogManager
#import signal


md_processor = MarkdownProcessor()
quiz_pro = QuizProcessor()
course_catalog_man = CourseCatalogManager()
progress_db_pro = ProgressDBProcessor()

def show_avl_course(request):
    if request.user.is_authenticated:
        #profile = Studentsinfo.objects.get(Email=email)
        profile =str(request.user)
        course_list = course_catalog_man.get_complete_course_catalog()
        return render(request, "course/avlCourses.html", {
            'profile': profile,
            'catalog': course_list,
            'is_module_view': 0 #,
            #"work_in_progress": [course_list["courses"][key]["work_in_progress"] for key in course_list["courses"]],
            #"pec_verified": [course_list["courses"][key]["pec_verified"] for key in course_list["courses"]]
        })
    else:
        return render(request, 'authError.html')

def view_course(request, course):
    if request.user.is_authenticated:
        uname = request.user.username
        #profile = Studentsinfo.objects.get(Email=email)
        profile = str(request.user)
        
        #all_marks = {
        #    "week1": progress_db_pro.get_week_marks(course, 1, uname),
        #    "week2": progress_db_pro.get_week_marks(course, 2, uname),
        #    "week3": 100  # NOTE: Funny
        #}
        all_marks = progress_db_pro.get_course_marks(course, uname)

        course_details = course_catalog_man.get_course_detail(course)
        
        user_progress = progress_db_pro.get_course_progress(course, request.user.username)

        return render(request, 'studentDashboard/course.html', {
            'profile': profile,
            'marks': all_marks,
            'course_details': course_details,
            'user_progress': user_progress,
            'is_module_view': 1
        })
    else:
        return render(request, 'authError.html')

def module(request, course, week, material):
    if request.user.is_authenticated:
        md_text = md_processor.fetch_week(course, week, material)
        html_content = md_processor.markdown_to_html(md_text)
        #profile = Studentsinfo.objects.get(Email=email)
        #profile = Studentsinfo(name="GUEST USER", email=request.user.username, student_department="-", section="-", roll_no="-")
        profile =str(request.user)
        print("modules")
        last_mat_num = course_catalog_man.get_material_count(course,week)
        flag = 0
        if(material == last_mat_num):
            flag = 1
        
        course_details = course_catalog_man.get_course_detail(course)
        return render(request, 'studentDashboard/module.html', {
            "context": html_content,
            "course": course,
            "week": week,
            "material": material,
            "quiz_no": 1,
            "profile": profile,
            "is_last_material": flag,
            "next_material_num": material + 1,
            "course_name": course_details["name"],
            "course_details": course_details,
            'is_module_view': 1
        })
    else:
        return render(request, 'authError.html')
    


