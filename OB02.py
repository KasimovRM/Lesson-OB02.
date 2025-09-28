class User:
    def __init__(self, user_id, name):
        self.__id = user_id  # Приватный атрибут
        self.__name = name  # Приватный атрибут
        self.__access_level = 'user'  # Приватный атрибут

    # Геттеры для получения данных
    def get_id(self):
        return self.__id

    def get_name(self):
        return self.__name

    def get_access_level(self):
        return self.__access_level

    # Сеттеры для изменения данных
    def set_name(self, new_name):
        self.__name = new_name

    def __str__(self):
        return f"ID: {self.__id}, Имя: {self.__name}, Уровень доступа: {self.__access_level}"


class Admin(User):
    def __init__(self, user_id, name):
        super().__init__(user_id, name)
        self.__access_level = 'admin'  # Переопределяем уровень доступа
        self.__users_list = []  # Приватный список пользователей

    # Переопределяем геттер для уровня доступа
    def get_access_level(self):
        return self.__access_level

    def add_user(self, user):
        """Добавить пользователя в систему"""
        if isinstance(user, User):
            self.__users_list.append(user)
            print(f"Пользователь {user.get_name()} добавлен в систему")
        else:
            print("Ошибка: можно добавлять только объекты класса User")

    def remove_user(self, user_id):
        """Удалить пользователя из системы по ID"""
        for user in self.__users_list:
            if user.get_id() == user_id:
                self.__users_list.remove(user)
                print(f"Пользователь с ID {user_id} удален из системы")
                return
        print(f"Пользователь с ID {user_id} не найден")

    def show_all_users(self):
        """Показать всех пользователей в системе"""
        print("\nСписок всех пользователей:")
        if not self.__users_list:
            print("Система пуста")
        else:
            for user in self.__users_list:
                print(user)


# Демонстрация работы системы
if __name__ == "__main__":
    # Создаем обычных пользователей
    user1 = User(1, "Иван Петров")
    user2 = User(2, "Мария Сидорова")
    user3 = User(3, "Алексей Козлов")

    # Создаем администратора
    admin = Admin(100, "Администратор Системы")

    print("=== ТЕСТИРОВАНИЕ СИСТЕМЫ ===")

    # Показываем информацию о пользователях через геттеры
    print(f"\nИнформация о пользователях:")
    print(f"User1: {user1.get_name()} (ID: {user1.get_id()}), Уровень: {user1.get_access_level()}")
    print(f"Admin: {admin.get_name()} (ID: {admin.get_id()}), Уровень: {admin.get_access_level()}")

    # Администратор добавляет пользователей
    print(f"\nДействия администратора:")
    admin.add_user(user1)
    admin.add_user(user2)
    admin.add_user(user3)

    # Показываем всех пользователей
    admin.show_all_users()

    # Изменяем имя пользователя через сеттер
    print(f"\nИзменение данных:")
    user1.set_name("Иван Иванов")
    print(f"Новое имя user1: {user1.get_name()}")

    # Администратор удаляет пользователя
    print(f"\nУдаление пользователя:")
    admin.remove_user(2)

    # Показываем обновленный список
    admin.show_all_users()

    # Попытка прямого доступа к приватным атрибутам (вызовет ошибку)
    print(f"\nПопытка прямого доступа к приватным атрибутам:")
    try:
        print(user1.__id)  # Это вызовет ошибку
    except AttributeError as e:
        print(f"Ошибка: {e}")
        print("Доступ к приватным атрибутам возможен только через геттеры!")