import sqlite3 as sq


class DataBase():
    def __init__(self):
        with sq.connect("transactions.db") as con:
            self.cur = con.cursor()

            self.sum = 0
            for x in self.cur.execute('SELECT balance FROM transactions WHERE status = "Расход"'):
                self.sum += (list(x))[0]
            self.cur.execute(f'UPDATE balance SET balance = {self.sum} WHERE id = 3')

            self.sum = 0
            for x in self.cur.execute('SELECT balance FROM transactions WHERE status = "Прибыль"'):
                self.sum += (list(x))[0]
            self.cur.execute(f'UPDATE balance SET balance = {self.sum} WHERE id = 2')

            self.cur.execute('SELECT balance FROM balance WHERE status_id IN(0, 1)')
            self.res = self.cur.fetchall()
            self.cur.execute(f'UPDATE balance SET balance = {self.res[0][0] - self.res[1][0]} WHERE id = 1')

            self.sum = 0
            for x in self.cur.execute('SELECT balance FROM transactions WHERE status = "Расход" AND category = "Сырьё"'):
                self.sum += (list(x))[0]
            self.cur.execute(f'UPDATE outcome SET balance = {self.sum} WHERE id = 1')
            self.sum = 0
            for x in self.cur.execute(
                    'SELECT balance FROM transactions WHERE status = "Расход" AND category = "Зарплата"'):
                self.sum += (list(x))[0]
            self.cur.execute(f'UPDATE outcome SET balance = {self.sum} WHERE id = 2')
            self.sum = 0
            for x in self.cur.execute(
                    'SELECT balance FROM transactions WHERE status = "Расход" AND category = "Электр-во"'):
                self.sum += (list(x))[0]
            self.cur.execute(f'UPDATE outcome SET balance = {self.sum} WHERE id = 3')
            self.sum = 0
            for x in self.cur.execute(
                    'SELECT balance FROM transactions WHERE status = "Расход" AND category = "Прочее"'):
                self.sum += (list(x))[0]
            self.cur.execute(f'UPDATE outcome SET balance = {self.sum} WHERE id = 4')

    def add_row(self, category, date, descriptions, balance, status):
        with sq.connect("transactions.db") as con:
            self.cur = con.cursor()
            self.cur.execute(f"""INSERT INTO transactions (category, date, descriptions, balance, status)
            VALUES ('{category}', '{date}', '{descriptions}', {balance}, '{status}')""")

    def edit_row(self, id, column, new_value):
        with sq.connect("transactions.db") as con:
            self.cur = con.cursor()
            self.cur.execute(f'UPDATE transactions SET {column} = "{new_value}" WHERE id = {id}')

    def delete_row(self, id):
        with sq.connect("transactions.db") as con:
            self.cur = con.cursor()
            self.cur.execute(f'DELETE FROM transactions WHERE id = {id}')

    def select_balance(self, id):
        with sq.connect("transactions.db") as con:
            self.cur = con.cursor()
            self.cur.execute(f'SELECT * FROM balance WHERE id = {id}')

            return str(self.cur.fetchall()[0][1])

    def select_transactions(self):
        with sq.connect("transactions.db") as con:
            self.cur = con.cursor()
            self.cur.execute(f'SELECT * FROM transactions')

            return self.cur.fetchall()

    def select_outcome(self, id):
        with sq.connect("transactions.db") as con:
            self.cur = con.cursor()
            self.cur.execute(f'SELECT * FROM outcome WHERE category = {id}')

            return str(self.cur.fetchall()[0][2])