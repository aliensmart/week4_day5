from app.orm import ORM 

class Computer(ORM):
    
    tablename = "computers"
    fields = ["brand", "model", "year", "ram", "disk", "user_pk"]

    def __init__(self, **kwargs):
        self.pk = kwargs.get("pk")
        self.model = kwargs.get("model")
        self.brand = kwargs.get("brand")
        self.year = kwargs.get("year")
        self.ram = kwargs.get("ram")
        self.disk = kwargs.get("disk")
        self.user_pk = kwargs.get("user_pk")