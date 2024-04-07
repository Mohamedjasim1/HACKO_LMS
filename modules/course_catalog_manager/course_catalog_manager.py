
import json


class CourseCatalogManager():
    """
    NOTE: This is a Singleton class
    """

    # Constants
    FILE_PATH    = "./courses/content_list.json"

    # Static Variables
    db_instance = None

    def __init__(self):
        
        with open(CourseCatalogManager.FILE_PATH, 'r') as fp:
            self.db = json.loads(fp.read())
        CourseCatalogManager.db_instance = self
        


    def flush_data(self):
        with open(CourseCatalogManager.FILE_PATH, 'w') as fp:
            json_object = json.dumps(self.db, indent = 4)
            fp.write(json_object)


    def get_complete_course_catalog(self):
        """This is testing"""
        return self.db

    def get_material_count(self,course,week):
        mat_count=self.get_complete_course_catalog()["courses"][f"course{course}"]["weeks"][f"week{week}"]["material_count"]
        return mat_count
    
    def get_course_detail(self,course):
        course_detail=self.get_complete_course_catalog()["courses"][f"course{course}"]
        return course_detail
    def get_week_count(self,course):
        week_count=self.get_complete_course_catalog()["courses"][f"course{course}"]["week_count"]
        return  week_count

    def get_week_count(self, course_num):
        return self.db["courses"][f"course{course_num}"]["week_count"]


    def get_material_count(self, course_num, week_num):
        return self.db["courses"][f"course{course_num}"]["weeks"][f"week{week_num}"]["material_count"]


    def get_quiz_count(self, course_num, week_num):
        return self.db["courses"][f"course{course_num}"]["weeks"][f"week{week_num}"]["quiz_count"]


    # TODO: Add more functions for retrieval of specific info.
    # TODO: Add functions to add content (AND FLUSH DATA) for Faculty Login

    def add_course(self,course_num,name,description,work_in_progress,pec_verified):
            
        self.db["courses"][f"course{course_num}"]={}
        self.db["courses"][f"course{course_num}"]["course_num"]=course_num
        self.db["courses"][f"course{course_num}"]["name"]=name
        self.db["courses"][f"course{course_num}"]["description"]=description
        self.db["courses"][f"course{course_num}"]["work_in_progress"]=work_in_progress
        self.db["courses"][f"course{course_num}"]["pec_verified"]=pec_verified
        self.db["courses"][f"course{course_num}"]["week_count"]=0
        self.db["courses"][f"course{course_num}"]["weeks"]={}
        self.flush_data()
 

    def add_weeks(self,course_num,name):
        week=self.db["courses"][f"course{course_num}"]["week_count"]

        self.db["courses"][f"course{course_num}"]["weeks"][f"week{week+1}"]={}
        self.db["courses"][f"course{course_num}"]["weeks"][f"week{week+1}"]["week_num"]=week+1
        self.db["courses"][f"course{course_num}"]["weeks"][f"week{week+1}"]["name"]=name
        self.db["courses"][f"course{course_num}"]["weeks"][f"week{week+1}"]["material_count"]=0
        self.db["courses"][f"course{course_num}"]["weeks"][f"week{week+1}"]["quiz_count"]=0
        self.db["courses"][f"course{course_num}"]["weeks"][f"week{week+1}"]["materials"]={}
        self.db["courses"][f"course{course_num}"]["weeks"][f"week{week+1}"]["quizzes"]={}
        self.db["courses"][f"course{course_num}"]["week_count"]=week+1
        
        self.flush_data()


    def add_meterials(self,course_num,week,material_name):
        mat_num=self.db["courses"][f"course{course_num}"]["weeks"][f"week{week}"]["material_count"]
        self.db["courses"][f"course{course_num}"]["weeks"][f"week{week}"]["materials"][f"text{mat_num + 1}"]={}
        self.db["courses"][f"course{course_num}"]["weeks"][f"week{week}"]["materials"][f"text{mat_num + 1}"]["material_num"]=mat_num+1
        self.db["courses"][f"course{course_num}"]["weeks"][f"week{week}"]["materials"][f"text{mat_num + 1}"]["name"]=material_name
        self.db["courses"][f"course{course_num}"]["weeks"][f"week{week}"]["material_count"]=mat_num+1
        self.flush_data()

    def add_quizzes(self,course_num,week,quiz_name):
        quiz_num=self.db["courses"][f"course{course_num}"]["weeks"][f"week{week}"]["quiz_count"]
        self.db["courses"][f"course{course_num}"]["weeks"][f"week{week}"]["quizzes"][f"quiz{quiz_num + 1}"]={}
        self.db["courses"][f"course{course_num}"]["weeks"][f"week{week}"]["quizzes"][f"quiz{quiz_num + 1}"]["quiz_num"]=quiz_num+1
        self.db["courses"][f"course{course_num}"]["weeks"][f"week{week}"]["quizzes"][f"quiz{quiz_num + 1}"]["name"]=quiz_name
        self.db["courses"][f"course{course_num}"]["weeks"][f"week{week}"]["quiz_count"]=quiz_num+1
        self.flush_data()


    def current_course(self):
        try:
            course_no=list(self.db["courses"].keys())[-1]
            return self.db["courses"][course_no]["course_num"]+1
        except:
             return 0
    def current_week(self):
        week_no=self.db["courses"][f"course{self.current_course()}"]["week_count"]
        return week_no

    def current_material(self):
        mat_no=self.db["courses"][f"course{self.current_course()}"]["weeks"][f"week{self.current_week()}"]["material_count"]
        return mat_no
 
    def current_quiz(self):
        quiz_no=self.db["courses"][f"course{self.current_course()}"]["weeks"][f"week{self.current_week()}"]["quiz_count"]
        return quiz_no
        



    #def shutdown(self):
    #    self.flush_data()



if __name__ == "__main__":
    pass
