import pytest
from task_1 import Teacher, DisciplineTeacher


@pytest.fixture
def teachers():
    """
    Фикстура для инициализации объектов Teacher и DisciplineTeacher.
    """
    teacher1 = Teacher(name="Иван Иванов", education="БГПУ", experience=4)
    teacher2 = DisciplineTeacher(name="Сергей Сергеев", education="МГУ", experience=6,
                                 discipline="Информатика", job_title="Преподаватель")
    return teacher1, teacher2


def test_teacher_initialization(teachers):
    """
    Функция тестирует инициализации объекта Teacher.
    """
    teacher1, teacher2 = teachers
    assert teacher1.name == "Иван Иванов"
    assert teacher1.education == "БГПУ"
    assert teacher1.experience == 4


def test_discipline_teacher_initialization(teachers):
    """
    Функция тестирует инициализации объекта DisciplineTeacher.
    """
    teacher1, teacher2 = teachers
    assert teacher2.name == "Сергей Сергеев"
    assert teacher2.education == "МГУ"
    assert teacher2.experience == 6
    assert teacher2.discipline == "Информатика"
    assert teacher2.job_title == "Преподаватель"


def test_experience_setter(teachers):
    """
    Функция тестирует значение опыта работы.
    """
    teacher1, teacher2 = teachers
    teacher1.experience = 5
    assert teacher1.experience == 5
    with pytest.raises(ValueError):
        teacher1.experience = -1


def test_get_teacher_data(teachers):
    """
    Функция тестирует метода get_teacher_data вывод информации об учителе.
    """
    teacher1, teacher2 = teachers
    teacher_data = teacher1.get_teacher_data()
    assert "Иван Иванов" in teacher_data
    assert "БГПУ" in teacher_data
    assert "4" in teacher_data

    discipline_teacher_data = teacher2.get_teacher_data()
    assert "Сергей Сергеев" in discipline_teacher_data
    assert "Информатика" in discipline_teacher_data
    assert "Преподаватель" in discipline_teacher_data


def test_add_mark(teachers):
    """
    Функция тестирует метод add_mark добавление оценки.
    """
    teacher1, teacher2 = teachers
    result = teacher2.add_mark("Анна", 5)
    assert result == "Преподаватель Сергей Сергеев по предмету Информатика поставил оценку 5 студенту Анна"


def test_remove_mark(teachers):
    """
    Функция тестирует метод remove_mark удаление оценки..
    """
    teacher1, teacher2 = teachers
    result = teacher2.remove_mark("Анна", 4)
    assert result == "Преподаватель Сергей Сергеев по предмету Информатика удалил оценку 4 студенту Анна"


def test_give_a_consultation(teachers):
    """
    Функция тестирует метод give_a_consultation о проведенной консультации преподавателем.
    """
    teacher1, teacher2 = teachers
    result = teacher2.give_a_consultation("10А")
    assert result == "Преподаватель Сергей Сергеев провел консультацию по предмету Информатика в 10А классе"


def test_dismiss_teacher(teachers):
    """
    Функция тестирует метода dismiss_teacher удаление учителя или его наличие.
    """
    teacher1, teacher2 = teachers
    Teacher.teachers_list = [teacher1, teacher2]
    result = Teacher.dismiss_teacher("Иван Иванов")
    assert result == "Учитель Иван Иванов уволен."
    assert len(Teacher.teachers_list) == 1
    assert Teacher.teachers_list[0].name == "Сергей Сергеев"

    result = Teacher.dismiss_teacher("Иван Иванов")
    assert result == "Учитель с именем Иван Иванов не найден."


def test_job_title_setter(teachers):
    """
    Функция проверяет сеттер job_title изменение в должности.
    """
    teacher1, teacher2 = teachers
    teacher2.job_title = "Директор"
    assert teacher2.job_title == "Директор"
