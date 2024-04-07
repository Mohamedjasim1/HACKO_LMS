import markdown2
import os
import json

from modules.course_catalog_manager.course_catalog_manager import CourseCatalogManager

class MarkdownProcessor():
    def __init__(self):
        self.course_catalog_man = CourseCatalogManager.db_instance


    def markdown_to_html(self, markdown_text):
        return markdown2.markdown(markdown_text, extras = ["tables"])


    def fetch_week(self, course_no, week_no, text_material_no):
        with open(f"./courses/course{course_no}/week{week_no}/text{text_material_no}.md", 'r') as fp:
            md_text = fp.read()
        return md_text


    def write_content(self, course_no, week_no, content, text_material_no):
        with open(f"./courses/course{course_no}/week{week_no}/text{text_material_no}.md", 'w') as fw:
            fw.write(content)


    def create_course(self, course_no,name,description,work_in_progress,pec_verified):   # TODO: Not working
        #self.course_catalog_man.get_complete_course_catalog()
        #path=f"\\LMS\\courses\\course{course_no}" 
        #path=f"/sample/course{course_no}"
        
        course_path=f"./courses/course{course_no}"
        if not os.path.exists(course_path):          
            os.makedirs(course_path)
        self.course_catalog_man.add_course(course_no,name,description,work_in_progress,pec_verified)

    ##   OLD CODE   ##
    #def create_week(self,course_no, week_no):   # TODO: Not working
    #    with open(f"./sample/course{course_no}/week{week_no}.md", 'w') as fw:
        #with open(f".\\LMS\\courses\\course{course_no}\\week{week_no}.md", 'w') as fw:
    #       fw.write("")
            
    def create_week(self,course_no,week_no,name):       
        week_path=f"./courses/course{course_no}/week{week_no}"
        if not os.path.exists(week_path):          
            os.makedirs(week_path)
        self.course_catalog_man.add_weeks(course_no,name)
        


    def create_material(self,course_no,week_no,mat_num,material):
        
        with open(f"./courses/course{course_no}/week{week_no}/text{mat_num}.md",'w') as fw:
            fw.write(material)
            
        

    def create_quiz(self,course_no,week_no,quiz_num,quiz):
        
        with open(f"./courses/course{course_no}/week{week_no}/quiz{quiz_num}.json",'w') as fw:
            fw.write(json.dumps(quiz))
        



if __name__ == "__main__":
    obj = MarkdownProcessor()
    print(obj.markdown_to_html("**Bold Text**"))
    obj.create_course(498)
    obj.create_week(498, 7)
