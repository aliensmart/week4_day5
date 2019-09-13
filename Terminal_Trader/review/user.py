from orm import ORM
from computer import Computer


class User(ORM):

    tablename = "users"
    fields = ["name", "phone", "email", "credit_card"]

    def __init__(self, **kwargs):
        self.pk = kwargs.get('pk')
        self.name = kwargs.get('name')
        self.phone = kwargs.get('phone')
        self.email = kwargs.get('email')
        self.credit_card = kwargs.get('credit_card')

    def computers_for(self):
        return Computer.all_from_where_clause("WHERE user_pk=?", (self.pk,))


if __name__=="__main__":
    test = User(name="Greg", pk=1)
    print(test.computers_for())
