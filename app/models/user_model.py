class User:
    def __init__(self, id, name, email, user_type):
        self.id = id
        self.name = name
        self.email = email
        self.user_type = user_type

    @staticmethod
    def get_by_id(user_id, mysql):
        cur = mysql.connection.cursor()
        cur.execute("SELECT * FROM users WHERE id=%s", (user_id,))
        user_data = cur.fetchone()
        cur.close()
        if user_data:
            return User(user_data['id'], user_data['name'], user_data['email'], user_data['user_type'])
        return None