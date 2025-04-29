import pytest
from main import BooksCollector

# класс TestBooksCollector объединяет набор тестов, которыми мы покрываем наше приложение BooksCollector
# обязательно указывать префикс Test
class TestBooksCollector:

    # пример теста:
    # обязательно указывать префикс test_
    # дальше идет название метода, который тестируем add_new_book_
    # затем, что тестируем add_two_books - добавление двух книг
    def test_add_new_book_add_two_books(self):
        # создаем экземпляр (объект) класса BooksCollector
        collector = BooksCollector()

        # добавляем две книги
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.add_new_book('Что делать, если ваш кот хочет вас убить')

        # проверяем, что добавилось именно две
        # словарь books_rating, который нам возвращает метод get_books_rating, имеет длину 2
        assert len(collector.get_books_genre()) == 2

    # напиши свои тесты ниже
    # чтобы тесты были независимыми в каждом из них создавай отдельный экземпляр класса BooksCollector()
    
    # тестируем, что книга добавляется без жанра
    def test_add_new_book_book_added_without_genre(self):
        collector = BooksCollector()
        collector.add_new_book('1984')
        assert collector.get_book_genre('1984') == ''

    # тестируем, что нельзя добавить книгу с именем длиннее 40 символов
    def test_add_new_book_book_name_more_than_40_symbols(self):
        collector = BooksCollector()
        long_name = 'Очень длинное название книги, превышающее сорок символов'
        collector.add_new_book(long_name)
        assert long_name not in collector.get_books_genre()

    # тестируем установку жанра книги
    def test_set_book_genre_set_correct_genre(self):
        collector = BooksCollector()
        collector.add_new_book('Гарри Поттер')
        collector.set_book_genre('Гарри Поттер', 'Фантастика')
        assert collector.get_book_genre('Гарри Поттер') == 'Фантастика'

    # тестируем, что невозможно установить жанр книги, если жанр недопустимый
    def test_set_book_genre_set_invalid_genre(self):
        collector = BooksCollector()
        collector.add_new_book('Гарри Поттер')
        collector.set_book_genre('Гарри Поттер', 'Поэзия')
        assert collector.get_book_genre('Гарри Поттер') == ''

    # тестируем получение списка книг по жанру
    def test_get_books_with_specific_genre_return_correct_books(self):
        collector = BooksCollector()
        collector.add_new_book('Гарри Поттер')
        collector.add_new_book('Шрек')
        collector.set_book_genre('Гарри Поттер', 'Фантастика')
        collector.set_book_genre('Шрек', 'Мультфильмы')
        assert collector.get_books_with_specific_genre('Фантастика') == ['Гарри Поттер']

    # тестируем получение списка книг для детей
    def test_get_books_for_children_return_only_child_friendly_books(self):
        collector = BooksCollector()
        collector.add_new_book('Шрек')
        collector.add_new_book('Дракула')
        collector.set_book_genre('Шрек', 'Мультфильмы')
        collector.set_book_genre('Дракула', 'Ужасы')
        assert collector.get_books_for_children() == ['Шрек']

    # тестируем добавление книги в избранное
    def test_add_book_in_favorites_adds_book_correctly(self):
        collector = BooksCollector()
        collector.add_new_book('Гарри Поттер')
        collector.add_book_in_favorites('Гарри Поттер')
        assert 'Гарри Поттер' in collector.get_list_of_favorites_books()

    # тестируем удаление книги из избранного
    def test_delete_book_from_favorites_deletes_book(self):
        collector = BooksCollector()
        collector.add_new_book('Гарри Поттер')
        collector.add_book_in_favorites('Гарри Поттер')
        collector.delete_book_from_favorites('Гарри Поттер')
        assert 'Гарри Поттер' not in collector.get_list_of_favorites_books()

    # тестируем получение списка избранных книг
    def test_get_list_of_favorites_books_returns_correct_list(self):
        collector = BooksCollector()
        collector.add_new_book('Гарри Поттер')
        collector.add_book_in_favorites('Гарри Поттер')
        assert collector.get_list_of_favorites_books() == ['Гарри Поттер']

    # параметризованный тест на добавление книги с валидными именами
    @pytest.mark.parametrize('book_name', ['Гарри Поттер', 'Шрек', '1984'])
    def test_add_new_book_parametrize_valid_names(self, book_name):
        collector = BooksCollector()
        collector.add_new_book(book_name)
        assert book_name in collector.get_books_genre()
        
    # тестируем получение словаря books_genre
    def test_get_books_genre_returns_correct_dictionary(self):
        collector = BooksCollector()
        collector.add_new_book('Гарри Поттер')
        collector.set_book_genre('Гарри Поттер', 'Фантастика')
        assert collector.get_books_genre() == {'Гарри Поттер': 'Фантастика'}

    # тестируем получение жанра конкретной книги
    def test_get_book_genre_returns_correct_genre(self):
        collector = BooksCollector()
        collector.add_new_book('Шрек')
        collector.set_book_genre('Шрек', 'Мультфильмы')
        assert collector.get_book_genre('Шрек') == 'Мультфильмы'

        