import sqlite3


class ORM:
    dbpath = ""
    tablename = ""
    fields = []

    def __init__(self, **kwargs):
        raise NotImplementedError

    def save(self):
        if self.pk is None:
            self._insert()
        else:
            self._update()

    def _insert(self):
        with sqlite3.connect(self.dbpath) as conn:
            curs = conn.cursor()
            fields = ", ".join(self.fields)
            qmarks = ", ".join(['?' for _ in self.fields])
            SQL = """ INSERT INTO {} ({}) VALUES ({})""".format(self.tablename, fields, qmarks)
            values = [getattr(self, field) for field in self.fields]
            # [self.field for field in self.fields]
            curs.execute(SQL, values)
            pk = curs.lastrowid
            self.pk = pk

    def _update(self):
        pass

    def delete(self):
        pass

    @classmethod
    def one_from_where_clause(cls, where_clause="", values=tuple()):
        pass

    @classmethod
    def all_from_where_clause(cls, where_clause="", values=tuple()):
        pass

    @classmethod
    def one_from_pk(cls, pk):
        return cls.one_from_where_clause("WHERE pk=?", (pk,))

    def __repr__(self):
        return "<{} ORM: pk={}>".format(self.tablename, self.pk)