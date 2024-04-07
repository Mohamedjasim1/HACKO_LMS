
import json


from modules.course_catalog_manager.course_catalog_manager import CourseCatalogManager


class ProgressDBProcessor():
    """
    NOTE: This is a Singleton class
    """

    # Constants
    DB_FILE_PATH    = "./user_progress_db/user_progress_db.json"
    FLUSH_THRESHOLD = 25

    # Static Variables
    db_instance = None

    def __init__(self):

        with open(ProgressDBProcessor.DB_FILE_PATH, 'r') as fp:
            self.db = json.loads(fp.read())
        self.flush_count_down = ProgressDBProcessor.FLUSH_THRESHOLD
        ProgressDBProcessor.db_instance = self
        self.progress_db_pro = CourseCatalogManager.db_instance
   


    def flush_data(self):
        with open(ProgressDBProcessor.DB_FILE_PATH, 'w') as fp:
            json_object = json.dumps(self.db, indent = 4)
            fp.write(json_object)


    def get_week_progress(self, course_no, week_no, material_no, email):
        try:
            user = self.db[email]["progress"]
            try:
                course_status = user["course" + str(course_no)]
                try:
                    week_status = course_status["week" + str(week_no)]
                    try:
                        material_status = week_status["text" + str(material_no)]
                        progress = material_status["course_progress"]
                    except KeyError:
                        progress = 0
                except KeyError:
                    progress = 0        # Week Not Yet Started
            except KeyError:
                progress = 0            # Course Not Enrolled by User
        except KeyError:
            progress = 0                # User Not Found
        return progress


    def get_course_progress(self, course_no, email):
        progress = {}
        try:
            user = self.db[email]["progress"]
            try:
                course_status = user["course" + str(course_no)]
                progress = {}
                for i in range(self.progress_db_pro.get_week_count(course_no)):
                #for week in course_status:
                    try:
                        week = f"week{i + 1}"
                        week_status = course_status[week]

                        progress[week] = {}
                        progress[week]["consolidated_marks"] = 0
                        my_sum = 0
                        n = 0
                        progress[week]["materials"] = {}
                        for j in range(self.progress_db_pro.get_material_count(course_no, i + 1)):
                        #for material in week_status:
                            try:
                                material = f"text{j + 1}"
                                material_status = week_status[material]
                                progress[week]["materials"][material] = material_status["course_progress"]
                            except:
                                progress[week]["materials"][material] = 0
                            '''
                            if(material[:4] == "text"):
                                try:
                                    material_status = week_status[material]
                                    progress[week]["materials"][material] = material_status["course_progress"]
                                except KeyError:
                                    progress[week]["materials"][material] = 0
                            if(material[:4] == "quiz"):
                                try:
                                    material_status = week_status[material]
                                    progress[week]["materials"][material] = material_status["quiz_marks"]
                                except KeyError:
                                    progress[week]["materials"][material] = 0
                            '''
                            my_sum += progress[week]["materials"][material]
                            n += 1
                        for j in range(self.progress_db_pro.get_quiz_count(course_no, i + 1)):
                        #for material in week_status:
                            try:
                                material = f"quiz{j + 1}"
                                material_status = week_status[material]
                                progress[week]["materials"][material] = material_status["quiz_marks"]
                                my_sum += 100  # NOTE: PURPOSELY DONE THIS !! NOT A MISTAKE !!!! (Contact Madhav before touching this line)
                            except:
                                progress[week]["materials"][material] = 0
                                my_sum += 0
                            #my_sum += progress[week]["materials"][material]
                            n += 1
                        if n != 0:
                            progress[week]["consolidated_marks"] = round(my_sum / n)
                    except KeyError:
                        progress[week] = {}    # Week Not Yet Started
            except KeyError:
                progress = {}                  # Course Not Enrolled by User
        except KeyError:
            progress = {}                      # User Not Found
        return progress


    def get_week_marks(self, course_no, week_no, material_no, email):
        marks = 0   
        try:
            user = self.db[email]["progress"]
            try:
                course_status = user["course" + str(course_no)]
                try:
                    week_status = course_status["week" + str(week_no)]
                    try:
                        material_status = week_status["quiz" + str(material_no)]
                        marks = material_status["quiz_marks"]
                    except KeyError:
                        marks = 0
                except KeyError:
                    marks = 0           # Week Not Yet Started
            except KeyError:
                marks = 0               # Course Not Enrolled by User
        except KeyError:
            marks = 0                   # User Not Found
        return marks


    def get_course_marks(self, course_no, email):  # TODO: Not Working
        marks = {}
        try:
            user = self.db[email]["progress"]
            try:
                course_status = user["course" + str(course_no)]
                marks = {}
                for week in course_status:
                    try:
                        week_status = course_status[week]
                        for quiz in week_status:
                            if(quiz[:4] == "quiz"):
                                try:
                                    material_status = week_status[quiz]
                                    marks[week][quiz] = material_status["quiz_marks"]
                                except KeyError:
                                    marks[week][quiz] = 0
                    except KeyError:
                        marks[week] = {}    # Week Not Yet Started
            except KeyError:
                marks = {}                  # Course Not Enrolled by User
        except KeyError:
            marks = {}                      # User Not Found
        return marks


    def set_week_progress(self, course_no, week_no, material_no, email, roll_no, progress):
        if(email not in self.db):
            self.db[email] = {}                         # User Not Found (new user)
            self.db[email]["roll_num"] = roll_no
            self.db[email]["progress"] = {}
        user_full = self.db[email]
        user = user_full["progress"]

        if(("course" + str(course_no)) not in user):
            user["course" + str(course_no)] = {}        # Course Not Enrolled by User (so far)
        course_status = user["course" + str(course_no)]

        if(("week" + str(week_no)) not in course_status):
            course_status["week" + str(week_no)] = {}   # Week Not Yet Started (so far)
        week_status = course_status["week" + str(week_no)]

        if(("text" + str(material_no)) not in week_status):
            week_status["text" + str(material_no)] = {}
        material_status = week_status["text" + str(material_no)]

        material_status["course_progress"] = progress
        #material_status["roll_num"] = roll_no

        self.flush_count_down -= 1
        if(self.flush_count_down == 0):
            self.flush_count_down = ProgressDBProcessor.FLUSH_THRESHOLD
            self.flush_data()


    def set_week_marks(self, course_no, week_no, material_no, email, roll_no, marks):
        if(email not in self.db):
            self.db[email] = {}                         # User Not Found (new user)
            self.db[email]["roll_num"] = roll_no
            self.db[email]["progress"] = {}
        user_full = self.db[email]
        user = user_full["progress"]

        if(("course" + str(course_no)) not in user):
            user["course" + str(course_no)] = {}        # Course Not Enrolled by User (so far)
        course_status = user["course" + str(course_no)]

        if(("week" + str(week_no)) not in course_status):
            course_status["week" + str(week_no)] = {}   # Week Not Yet Started (so far)
        week_status = course_status["week" + str(week_no)]

        if(("quiz" + str(material_no)) not in week_status):
            week_status["quiz" + str(material_no)] = {}
        material_status = week_status["quiz" + str(material_no)]

        material_status["quiz_marks"] = marks
        #material_status["roll_num"] = roll_no

        self.flush_count_down -= 1
        if(self.flush_count_down == 0):
            self.flush_count_down = ProgressDBProcessor.FLUSH_THRESHOLD
            self.flush_data()


    def shutdown(self):
        self.flush_data()



if __name__ == "__main__":
    pass
