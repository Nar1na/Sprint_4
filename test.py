import pytest
from .main import BooksCollector


class TestBookCollector:

    @pytest.fixture(autouse=True)
    def collector(self):
        self.collector = BooksCollector()
        return self.collector

    def test_add_new_book_add_two_books(self):
        self.collector.add_new_book('Гордость и предубеждение и зомби')
        self.collector.add_new_book('Что делать, если ваш кот хочет вас убить')
        assert len(self.collector.get_books_genre()) == 2

    @pytest.mark.parametrize("name", ['', 'a' * 41])
    def test_add_new_book_invalid_name_length(self, name):
        self.collector.add_new_book(name)
        assert len(self.collector.get_books_genre()) == 0

    def test_set_book_genre(self):
        name = 'Book1'
        self.collector.add_new_book(name)
        self.collector.set_book_genre(name, 'Фантастика')
        assert self.collector.get_book_genre(name) == 'Фантастика'

    def test_set_book_genre_book_not_found(self):
        self.collector.set_book_genre('NonExistent', 'Фантастика')
        assert self.collector.get_book_genre('NonExistent') is None

    def test_set_book_genre_invalid_genre(self):
        name = 'Book1'
        self.collector.add_new_book(name)
        self.collector.set_book_genre(name, 'UnknownGenre')
        assert self.collector.get_book_genre(name) == ''

    def test_get_books_with_specific_genre(self):
        self.collector.add_new_book('Book1')
        self.collector.add_new_book('Book2')
        self.collector.set_book_genre('Book1', 'Фантастика')
        self.collector.set_book_genre('Book2', 'Ужасы')
        assert self.collector.get_books_with_specific_genre('Фантастика') == ['Book1']

    def test_get_books_for_children(self):
        self.collector.add_new_book('KidBook')
        self.collector.add_new_book('AdultBook')
        self.collector.set_book_genre('KidBook', 'Мультфильмы')
        self.collector.set_book_genre('AdultBook', 'Ужасы')
        assert self.collector.get_books_for_children() == ['KidBook']

    def test_add_book_in_favorites(self):
        name = 'Book1'
        self.collector.add_new_book(name)
        self.collector.add_book_in_favorites(name)
        assert name in self.collector.get_list_of_favorites_books()

    def test_add_book_in_favorites_not_in_books(self):
        self.collector.add_book_in_favorites('Unknown')
        assert 'Unknown' not in self.collector.get_list_of_favorites_books()

    def test_add_book_in_favorites_duplicate(self):
        name = 'Book1'
        self.collector.add_new_book(name)
        self.collector.add_book_in_favorites(name)
        self.collector.add_book_in_favorites(name)
        assert len(self.collector.get_list_of_favorites_books()) == 1

    def test_delete_book_from_favorites(self):
        name = 'Book1'
        self.collector.add_new_book(name)
        self.collector.add_book_in_favorites(name)
        self.collector.delete_book_from_favorites(name)
        assert name not in self.collector.get_list_of_favorites_books()
