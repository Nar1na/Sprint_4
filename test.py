import pytest
from .main import BooksCollector


class TestBookCollector:

    def test_add_new_book_add_two_books(self, collector):
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.add_new_book('Что делать, если ваш кот хочет вас убить')
        assert len(collector.get_books_genre()) == 2

    @pytest.mark.parametrize("name", ['', 'a' * 41])
    def test_add_new_book_invalid_name_length(self, collector, name):
        collector.add_new_book(name)
        assert len(collector.get_books_genre()) == 0

    def test_set_book_genre(self, collector):
        name = 'Book1'
        collector.add_new_book(name)
        collector.set_book_genre(name, 'Фантастика')
        assert collector.get_book_genre(name) == 'Фантастика'

    def test_set_book_genre_book_not_found(self, collector):
        collector.set_book_genre('NonExistent', 'Фантастика')
        assert collector.get_book_genre('NonExistent') is None

    def test_set_book_genre_invalid_genre(self, collector):
        name = 'Book1'
        collector.add_new_book(name)
        collector.set_book_genre(name, 'UnknownGenre')
        assert collector.get_book_genre(name) == ''

    def test_get_books_with_specific_genre(self, collector):
        collector.add_new_book('Book1')
        collector.add_new_book('Book2')
        collector.set_book_genre('Book1', 'Фантастика')
        collector.set_book_genre('Book2', 'Ужасы')
        assert collector.get_books_with_specific_genre('Фантастика') == ['Book1']

    def test_get_books_for_children(self, collector):
        collector.add_new_book('KidBook')
        collector.add_new_book('AdultBook')
        collector.set_book_genre('KidBook', 'Мультфильмы')
        collector.set_book_genre('AdultBook', 'Ужасы')
        assert collector.get_books_for_children() == ['KidBook']

    def test_add_book_in_favorites(self, collector):
        name = 'Book1'
        collector.add_new_book(name)
        collector.add_book_in_favorites(name)
        assert name in collector.get_list_of_favorites_books()

    def test_add_book_in_favorites_not_in_books(self, collector):
        collector.add_book_in_favorites('Unknown')
        assert 'Unknown' not in collector.get_list_of_favorites_books()

    def test_add_book_in_favorites_duplicate(self, collector):
        name = 'Book1'
        collector.add_new_book(name)
        collector.add_book_in_favorites(name)
        collector.add_book_in_favorites(name)
        assert len(collector.get_list_of_favorites_books()) == 1

    def test_delete_book_from_favorites(self, collector):
        name = 'Book1'
        collector.add_new_book(name)
        collector.add_book_in_favorites(name)
        collector.delete_book_from_favorites(name)
        assert name not in collector.get_list_of_favorites_books()
