from datetime import date
class Task:
    def __init__(self, id, description, status):
        self.id = id
        self.description = description
        self.status = status
        self.created_at = date.today()
        self.updated_at = date.today()

    

    
