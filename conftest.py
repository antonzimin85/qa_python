import pytest

from main import BooksCollector


@pytest.fixture(scope='function')
def collector_without_books():
    collector_without_books = BooksCollector()

    return collector_without_books

@pytest.fixture(scope='function')
def collector_with_books_of_all_genres():
    collector_with_books_of_all_genres = BooksCollector()
    books_with_all_genres = {'Черновик': 'Фантастика', 'Сияние': 'Ужасы','Момент истины': 'Детективы','Незнайка на луне': 'Мультфильмы','Двенадцать стульев': 'Комедии'}
    for book_name, book_genre in books_with_all_genres.items():
        collector_with_books_of_all_genres.add_new_book(book_name)
        collector_with_books_of_all_genres.set_book_genre(book_name, book_genre)

    return collector_with_books_of_all_genres

@pytest.fixture(scope='function')
def collector_with_books_with_age_rating():
    collector_with_books_with_age_rating = BooksCollector()
    books_with_book_with_age_rating = {'Черновик': 'Фантастика', 'Момент истины': 'Детективы'}
    for book_name, book_genre in books_with_book_with_age_rating.items():
        collector_with_books_with_age_rating.add_new_book(book_name)
        collector_with_books_with_age_rating.set_book_genre(book_name, book_genre)

    return collector_with_books_with_age_rating