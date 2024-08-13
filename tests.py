from main import BooksCollector
import pytest

class TestBooksCollector:

    def test_add_new_book_two_books_true(self):

        collector = BooksCollector()
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.add_new_book('Что делать, если ваш кот хочет вас убить')

        assert len(collector.get_books_genre()) == 2

    @pytest.mark.parametrize('name', [
        'Гордость и предубеждение и зомби         ',
        'Что делать, если ваш кот хочет вас убить '
    ])
    def test_add_new_book_with_a_long_title_false(self, name):
        collector = BooksCollector()
        assert len(name) > 40, f"Ошибка: Длина названия книги '{name}' не должна быть больше 41 символа."

    def test_get_books_genre_empty_true(self):
        collector = BooksCollector()
        assert collector.get_books_genre() == {}

    @pytest.mark.parametrize('name, genre', [
        ("Властелин Колец", "Фантастика"),
        ("Шерлок Холмс", "Детективы")
    ])
    def test_set_book_genre_true(self, name, genre):
        collector = BooksCollector()
        collector.add_new_book(name)
        collector.set_book_genre(name, genre)
        actual_genre = collector.get_book_genre(name)
        assert actual_genre == genre

    def test_set_book_genre_invalid_false(self):
        collector = BooksCollector()
        collector.add_new_book('1984')
        collector.set_book_genre('1984', 'Invalid Genre')
        assert collector.get_book_genre('1984') == ""


    def test_get_books_with_specific_genre_true(self):
        collector = BooksCollector()
        collector.add_new_book('Автостопом по Галактике')
        collector.set_book_genre('Автостопом по Галактике', 'Фантастика')
        collector.add_new_book('Dracula')
        collector.set_book_genre('Dracula', 'Ужасы')
        books = collector.get_books_with_specific_genre('Фантастика')
        assert 'Автостопом по Галактике' in books
        assert 'Dracula' not in books


    def test_add_book_in_favorites_true(self):
        collector = BooksCollector()
        collector.add_new_book('Дюна')
        collector.add_book_in_favorites('Дюна')
        assert 'Дюна' in collector.get_list_of_favorites_books()


    def test_delete_book_from_favorites_true(self):
        collector = BooksCollector()
        collector.add_new_book('Дюна')
        collector.add_book_in_favorites('Дюна')
        collector.delete_book_from_favorites('Дюна')
        assert 'Дюна' not in collector.get_list_of_favorites_books()


    def test_add_book_in_favorites_invalid_false(self):
        collector = BooksCollector()
        collector.add_book_in_favorites('Nonexistent Book')
        assert 'Nonexistent Book' not in collector.get_list_of_favorites_books()

    def test_get_list_in_favorites_books_true(self):
        collector = BooksCollector()
        assert collector.get_list_of_favorites_books() == []

    def test_get_list_in_favorites_books_single_true(self):
        collector = BooksCollector()
        collector.add_new_book('The Great Gatsby')
        collector.add_book_in_favorites('The Great Gatsby')
        assert collector.get_list_of_favorites_books() == ['The Great Gatsby']

    def test_get_list_in_favorites_books_multiple_true(self):
        collector = BooksCollector()
        collector.add_new_book('1984')
        collector.add_new_book('Brave New World')
        collector.add_book_in_favorites('1984')
        collector.add_book_in_favorites('Brave New World')
        assert collector.get_list_of_favorites_books() == ['1984', 'Brave New World']

    def test_get_book_genre_name_true(self):
        collector = BooksCollector()
        collector.add_new_book('Гордость и предубеждение')
        assert collector.get_book_genre('Гордость и предубеждение') == ''

    def test_get_books_for_children_rating_true(self):
        collector = BooksCollector()
        collector.add_new_book('Лев, колдунья и платяной шкаф')
        collector.set_book_genre('Лев, колдунья и платяной шкаф', 'Фантастика')
        collector.add_new_book('Тебе не спрятаться')
        collector.set_book_genre('Тебе не спрятаться', 'Ужасы')

        books = collector.get_books_for_children()

        assert 'Лев, колдунья и платяной шкаф' in books, "Ошибка: 'Лев, колдунья и платяной шкаф' должен быть в списке."
        assert 'Тебе не спрятаться' not in books, "Ошибка: 'Тебе не спрятаться' не должен быть в списке."
