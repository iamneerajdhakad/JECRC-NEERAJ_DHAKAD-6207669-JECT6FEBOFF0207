import time

class TODO:
    todos = []
    
    def add_todo(self, desc):
        ##1. Take desc from the user
        if(len(desc.strip())==0):
            print('Task cannot be empty.')
            return
        ##2. we have to create a dictionary in which we will add the todo desc
        d = {
            'id': int(time.time()),
            'desc': desc,
            'is_completed':False
        }
        ##3. we have to append that dictionay inside todo
        self.todos.append(d)
        print(f'--> {desc}; Added Successfully :)')
    
    def remove_todo(self, id):

        if len(self.todos) == 0:
            print('NO TODOS EXISTS!')
            return

        i = 0
        while(i < len(self.todos)):
            if(self.todos[i]['id']==id):
                print(f'Removed TO-DO id {self.todos[i]['id']}')
                self.todos.pop(i)
            i+=1


    def display_todos(self):
        
        if len(self.todos) == 0:
            print('NO TODOS EXISTS!')
            return
        
        for i in self.todos:

            if i['is_completed']:
                print(f'{i['desc']} {i['id']} (completed)')
            else:
                print(f'{i['desc']} {i['id']} (Pending)')
            
    
    def update_todo(self, id, new_desc):
        i = 0

        while(i < len(self.todos)):
            if(self.todos[i]['id']==id):
                print(f'Description Updated for {self.todos[i]['id']}')
                self.todos[i]['desc']=new_desc
            i+=1
    
    def toggle_mark_as_completed(self, id):

        for i in self.todos:
            if(id == i['id']):
                i['is_completed'] = ~i['is_completed']
    
    def completed_todos(self):

        for i in self.todos:
            if(i['is_completed']):
                print(f'{i['desc']} {i['id']} (completed)')
    
    def incompleted_todos(self):

        for i in self.todos:
            if(i['is_completed']):
                continue
            else:
                print(f'{i['desc']} {i['id']} (Pending)')
    