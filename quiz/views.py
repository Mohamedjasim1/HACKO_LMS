from django.shortcuts import render, redirect
from django.views import View
from .models import Question, Mark
from django.conf import settings
from django.contrib import messages
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from modules.quiz_pro.quiz_pro import quiz_pro
from modules.leaderboard_pro.leaderboard_pro import leaderboard_pro
quiz_p=quiz_pro()
LBoard=leaderboard_pro()
import json


from modules.quiz_processor.quiz_processor import QuizProcessor
from modules.markdown_processor.markdown_processor import MarkdownProcessor
from modules.progress_db_processor.progress_db_processor import ProgressDBProcessor
from modules.course_catalog_manager.course_catalog_manager import CourseCatalogManager
#import signal


md_processor = MarkdownProcessor()
quiz_pros = QuizProcessor()
course_catalog_man = CourseCatalogManager()
progress_db_pro = ProgressDBProcessor()
# Create your views here.
# @method_decorator(login_required, name="dispatch")


class Quiz_module(View):
    def get(self,request):
        
        context=quiz_p.all_quiz_data()
        return render(request,"quiz/quiz_module.html",{"context":context})

class Quiz(View):
    def get(self, request,quiz_id):
      
        questions =quiz_p.creator_quiz(str(quiz_id))
        seconds=quiz_p.get_seconds(str(quiz_id))
      
        return render(
            request,
            "quiz/quiz.html",
            {"questions": questions,"quiz_id":str(quiz_id),"seconds":seconds}
        )

    def post(self, request,quiz_id):

        print("yes...its working !!!!!!")
        # mark = Mark(user=request.user, total=Question.objects.filter(verified=True).count())
        mark=0
        b=quiz_p.correct_options(str(quiz_id))
        data=quiz_p.quiz_data(str(quiz_id))
       
        name=str(request.user)
        quiz_name=data["name"]
        
        for i,v in enumerate(b):
           
            #print(request.POST.get(f"q{i+1}o", ""),v)
            if(request.POST.get(f"q{i+1}o", "")==v):
                mark+=1
        
        total=len(b)
        try:
            LBoard.update_mark(name,quiz_name,mark)
        except:
            pass
        LBoard.store_data(name,quiz_name,mark,total)
            
        
        
        
        
        

        return render(request,"quiz/result.html",{"content":mark,"quiz_id":str(quiz_id)})


class AddCourse(View):

    def get(self, request):
        return render(
            request, 
            "quiz/add_course.html"
        )
    
    def post(self,request):
        data = request.POST
        x=course_catalog_man.current_course()
        course_name=data.get("c_name")
        description=data.get("des")
        w_name=data.get("w_name")
        topic=data.get("topic").split(",")
        print(course_name   )
        course_catalog_man.add_course(x,course_name,description,0,1)
        course_catalog_man.add_weeks(x,w_name)


        for i in topic:
            course_catalog_man.add_meterials(x,1,i)
        return redirect('show_courses')




class AddQuestion(View):
    db={"qtns":{}}
    def get(self, request):
        return render(
            request, 
            "quiz/add_questions.html",{"questions":range(1,6)}
        )
    
    
    def post(self, request):

        

        already_exists=0
        
        for i in range(1, 6):
            data = request.POST
            q = data.get(f"q{i}", "")
            o1 = data.get(f"q{i}o1", "")
            o2 = data.get(f"q{i}o2", "")
            o3 = data.get(f"q{i}o3", "")
            o4 = data.get(f"q{i}o4", "")
            co = data.get(f"q{i}c", "")
            quiz_name=data.get("quiz_name")
            seconds=data.get("seconds")
            # self.db["creator"]=request.user
            # self.db["qtns"][q]=list([o1,o2,o3,o4])
            quiz_p.get_quiz_detail(quiz_name,str(request.user),q,list([o1,o2,o3,o4]),co,quiz_p.current_quiz(quiz_name),seconds)


            

            
            if Question.objects.filter(question=q).first():
                already_exists += 1
                continue



            question = Question(
                question=q,
                option1=o1,
                option2=o2,
                option3=o3,
                option4=o4,
                correct_option=co,
                quiz_name=quiz_name,
                creator=request.user
            )
            question.save()
           
        
        return redirect("add_question")

# @method_decorator(login_required, name="dispatch")
class Result(View):
    def get(self, request):
        results = Mark.objects.filter(user=request.user)
        return render(request, "quiz/result.html", {"results": results})

class Leaderboard(View):
    def get(self, request,quiz_id):
        q_name=quiz_p.quiz_name_by_id(str(quiz_id))
        result=(LBoard.get_leaderboard(q_name))
        return render(
            request, 
            "quiz/leaderboard.html", 
            {"results":result})
    
class Leaderboards(View):
    def get(self,request):
        leaderboard=quiz_p.get_quiznames()

        return render(
            request, 
            "quiz/leaderboards.html", 
            {"leaderboard":leaderboard})
    



def show_avl_course(request):
    if request.user.is_authenticated:
        #profile = Studentsinfo.objects.get(Email=email)
        profile =str(request.user)
        course_list = course_catalog_man.get_complete_course_catalog()
        return render(request, "quiz/avlCourses.html", {
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

        return render(request, 'quiz/course.html', {
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
        return render(request, 'quiz/module.html', {
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
    
