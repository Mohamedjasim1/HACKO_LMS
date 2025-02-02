import json
from modules.quiz_pro.quiz_pro import quiz_pro
class leaderboard_pro():
    

    # Constants
    FILE_PATH    = ".\mydb\leaderboard.json"

    # Static Variables
    db_instance = None

    def __init__(self):
        
        with open(leaderboard_pro.FILE_PATH, 'r') as fp:
            self.db = json.loads(fp.read())
             
        leaderboard_pro.db_instance = self
        

    def flush_data(self):
        with open(leaderboard_pro.FILE_PATH, 'w') as fp:
            
            json_object = json.dumps(self.db, indent = 4)
            fp.write(json_object)


    def store_data(self,user,quiz_name,get,total):
        if(user not in self.db):
            self.db[user]=[]
        
        
        quiz={}
        if(quiz_name not in quiz):
            quiz[quiz_name]={}
        quiz[quiz_name]["got"]=get
        quiz[quiz_name]["total"]=total

        self.db[user].append(quiz)

        
        
        self.flush_data()

    
    def update_mark(self,name,quiz_name,current_mark):#
        Flag=False
        store=(list(map(lambda x:list(x.keys())[0],self.db[name][0:])))
        print(store)
        
        if(quiz_name in store):
            ind=store.index(quiz_name)
            pre=self.db[name][ind][quiz_name]["got"]
            print(pre)

            if(current_mark>pre):
                del self.db[name][ind][quiz_name]
                del self.db[name][ind]
                self.flush_data()
              
               
            else:
                del self.db[name][ind][quiz_name]
                del self.db[name][ind]
                self.flush_data()
                
        
        else:
            return Flag
        


    def get_leaderboard(self,quiz_name):
        
        a=[]
      
        for x,v in self.db.items():
            temp={}
            for i in v:
     
                if( quiz_name in i):
                    
                    
                    temp["name"]=x
                    temp["got"]=i[quiz_name]["got"]
                    temp["total"]=i[quiz_name]["total"]
                
                    a.append(temp)
        a.sort(key=lambda x:x["got"],reverse=True)
            
       
        return a
    
    def get_indiduals_mark(self,user):
        c={}
        for x in self.db[user]:
            for k,v in x.items():
                c[k]=v["got"]
        return c

    
                
                



