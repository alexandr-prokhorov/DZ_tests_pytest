# В одной из прошлых домашних работе вы должны были
# создать базовый класс Teacher и класс наследник
# DisciplineTeacher.
# Вам необходимо будет создать список на уровне класса и
# добавить метод увольнения учителя, как я показал на занятии
# для класса Employer
# Далее для успешного выполнения задания вам создать
# рабочую копию данного проекта с активным виртуальным
# окружением (venv). Установить в каждый проект отдельно
# необходимые библиотеки.
# Для проекта pytest в терминале:
# pip install pytest
# pip install pytest-cov
# pip install coverage (для создания HTML файла данная
# библиотека работает и с pytest и с unittest)
# Для проекта unittest в терминале:
# pip install coverage

class Teacher:
    """
    Класс Teacher в котором описывается характеристика учителей добавленных в список
    """
    # Создаю список для хранения добавленных учителей
    teachers_list = []

    def __init__(self, name, education, experience):
        """
        Функция инициализирует данные об учителе и добавляет его в список

        :param name: Имя учителя
        :param education: Образование учителя
        :param experience: Опыт работы учителя
        """
        self.__name = name
        self.__education = education
        self.__experience = experience
        # Метод добавляет учителя в список
        Teacher.teachers_list.append(self)

    @property
    def name(self):
        """
        Функция возвращает имя учителя

        :return: Возвращает данные
        """
        return self.__name

    @property
    def education(self):
        """
        Функция возвращает образование учителя

        :return: Возвращает данные
        """
        return self.__education

    @property
    def experience(self):
        """
        Функция возвращает опыт учителя

        :return: Возвращает данные
        """
        return self.__experience

    @experience.setter
    def experience(self, years):
        """
        Функция добавляет опыта работы учителя и проверяет на отрицательный ввод

        :param years: Количество лет опыта
        :raise ValueError: ошибка если опыт работы отрицательный
        """
        if years < 0:
            raise ValueError("Опыт не может быть отрицательным.")
        self.__experience = years

    def get_teacher_data(self):
        """
        Функция возвращает данные об учителе в виде таблицы

        :return: возвращает информацию
        """
        return f"Имя: {self.__name},\nОбразование: {self.__education}\nОпыт работы: {self.__experience} года"

    @classmethod
    def dismiss_teacher(cls, teacher_name):
        """
        Функция удаляет учителя из списка или проверяет есть ли такой учитель

        :param teacher_name: имя учителя
        :return: возвращает информацию об увольнении учителя или если учитель не найден
        """
        for teacher in cls.teachers_list:
            if teacher.name == teacher_name:
                cls.teachers_list.remove(teacher)
                return f"Учитель {teacher_name} уволен."
        return f"Учитель с именем {teacher_name} не найден."


class DisciplineTeacher(Teacher):
    """
    Класс DisciplineTeacher описывает должность и предмет учителя
    """

    def __init__(self, name, education, experience, discipline, job_title):
        """
        Функция инициализирует DisciplineTeacher.

        :param name: Имя учителя
        :param education: образование учителя
        :param experience: опыт Работы учителя
        :param discipline: Предмет преподаваемый учителем
        :param job_title: Должность
        """
        super().__init__(name, education, experience)
        self.__discipline = discipline
        self.__job_title = job_title

    @property
    def discipline(self):
        """
        Функция Возвращает предмет, который преподает учитель.

        :return: Возвращает данные
        """
        return self.__discipline

    @property
    def job_title(self):
        """
        Возвращает должность учителя.

        :return: Возвращает данные
        """
        return self.__job_title

    @job_title.setter
    def job_title(self, title):
        """
        Устанавливает должность учителя.

        :param title: Новая должность
        """
        self.__job_title = title

    def get_teacher_data(self):
        """
        Возвращает данные об учителе с учетом дисциплины и должности.

        :return: Возвращает данные
        """
        data = super().get_teacher_data()
        return f"{data}\nПредмет: {self.__discipline}\nДолжность: {self.__job_title}"

    def add_mark(self, student_name, mark):
        """
        Функция добавляет оценку студенту по предмету учителя.

        :param student_name: Имя студента
        :param mark: Оценка
        :return: возвращает информацию
        """
        return f"{self.__job_title} {self.name} по предмету {self.__discipline} поставил оценку {mark} студенту {student_name}"

    def remove_mark(self, student_name, mark):
        """
        Функция удаляет оценку студенту по предмету учителя.

        :param student_name: Имя студента
        :param mark: Оценка
        :return: возвращает информацию
        """
        return f"{self.__job_title} {self.name} по предмету {self.__discipline} удалил оценку {mark} студенту {student_name}"

    def give_a_consultation(self, class_name):
        """
        Функция возвращает информацию о проведенной консультации
        :param class_name: название класса
        :return: возвращает информацию
        """
        return f"{self.__job_title} {self.name} провел консультацию по предмету {self.__discipline} в {class_name} классе"


# Добавляю учителей
teacher1 = DisciplineTeacher(name="Иван Иванов", education="БГПУ", experience=4, discipline="Химия",
                             job_title="Директор")
teacher2 = DisciplineTeacher(name="Сергей Сергеев", education="МГУ", experience=6, discipline="Информатика",
                             job_title="Преподаватель")
teacher3 = DisciplineTeacher(name="Петр Петров", education="СГТУ", experience=3, discipline="История",
                             job_title="Преподаватель")
# # Вывожу информацию
# print(teacher1.get_teacher_data())
# print()
# print(teacher2.get_teacher_data())
# print()
# print(teacher3.get_teacher_data())
# # Увольняю учителя
# print(Teacher.dismiss_teacher("Петр Петров"))
# # Пытаюсь уволить его еще раз, чтобы вернул ошибку
# print(Teacher.dismiss_teacher("Петр Петров"))
# print()
# # Вывожу список оставшихся учителей
# for i in Teacher.teachers_list:
#     print(i.get_teacher_data())
#     print()
