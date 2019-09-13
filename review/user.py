from app.orm import ORM 

class User(ORM):
    tablename = "users"
    fields = ["name", "phone", "email", "credit_card"]

    def __init__(self,**kwargs):
        self.pk = kwargs.get("pk")
        self.name = kwargs.get("name")
        self.phone = kwargs.get("phone")
        self.email = kwargs.get("email")
        self.credit_card = kwargs.get("credit_card")

    def get_computer(self):
        return Computer.all_from_where_clause("WHERE user_pk=?", (self.pk, ))

