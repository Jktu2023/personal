# Разработай систему управления учетными записями пользователей для небольшой компании. Компания разделяет сотрудников
# на обычных работников и администраторов. У каждого сотрудника есть уникальный идентификатор (ID), имя и уровень доступа.
# Администраторы, помимо обычных данных пользователей, имеют дополнительный уровень доступа и могут добавлять или удалять пользователя из системы.
# Требования:
# 1.Класс `User*: Этот класс должен инкапсулировать данные о пользователе: ID, имя и уровень доступа ('user' для обычных сотрудников).
# 2.Класс `Admin`: Этот класс должен наследоваться от класса `User`. Добавь дополнительный атрибут уровня доступа, специфичный
# для администраторов ('admin'). Класс должен также содержать методы `add_user` и `remove_user`, которые позволяют добавлять и
# удалять пользователей из списка (представь, что это просто список экземпляров `User`).
# 3.Инкапсуляция данных: Убедись, что атрибуты классов защищены от прямого доступа и модификации снаружи. Предоставь доступ
# к необходимым атрибутам через методы (например, get и set методы).
class User:
    def __init__(self, name, ID, level):
        self._name_protect = name
        self._ID_protect = ID
        self._level_protect = level

    def get_level_privat(self):
        return self._level_protect

    def set_level_privat(self, level):
        self._level_protect = level
    def set_level_protect(self, ID):
        self._ID_protect = ID
    def info(self, ):
        print(f'Имя: {self._name_protect}, ID: {self._ID_protect}, уровень: {self._level_protect}')

class Admin(User):
    def __init__(self, name, ID, level,  level_A):
        super().__init__(name, ID, level)
        self.__level_A_privat = level_A

    def _del_person_privat(self, lst, user):
        lst.remove(user)
    def info(self, ):
        print(f'Имя: {self._name_protect}, ID: {self._ID_protect}, уровень: {self.__level_A_privat}')


user1 = User('Иван', 11223, 'user')
user2 = User('Cергей', 11224, 'user')
user3 = User('Дмитрий', 11225, 'user')
user4 = User('Олег', 11226, 'user')
user5 = User('Алексей', 11227, 'user')

admin1 = Admin('Стас', 10000, 'user','admin')

lst = []
for i in range(5):
    nik = 'user' + str(i+1)
    lst.append(nik)

print(f'список пользователей: {lst}')

user1.info()
user1.ID = 15555
user1.name = 'Рита'
user1.info()
user1.set_level_protect(20000)
user1.info()

print()

admin1.info()
admin1._del_person_privat(lst, 'user1')
# _Admin__del_person_privat(lst, user1)
print(f'список пользователей: {lst}')
