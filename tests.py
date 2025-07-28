import pytest


class TestBooksCollector:

    def test_add_new_book_name_less_then_40_symbols_book_is_added(self, collector_without_books):

        book_name = 'Момент истины'
        collector_without_books.add_new_book(book_name)
        assert book_name in collector_without_books.books_genre

    @pytest.mark.parametrize('book_name', ['Похождения бравого солдата Швейка во время мировой войны', ''])
    def test_add_new_book_name_more_then_40_or_less_then_1_symbols_book_is_not_added(self, collector_without_books, book_name):

        collector_without_books.add_new_book(book_name)
        assert book_name not in collector_without_books.books_genre

    @pytest.mark.parametrize('book_genre', ['Фантастика', 'Ужасы', 'Детективы', 'Мультфильмы', 'Комедии'])
    def test_set_book_genre_genre_in_genre_list_genre_is_set(self, collector_without_books, book_genre):

        book_name = 'Момент истины'
        collector_without_books.add_new_book(book_name)
        collector_without_books.set_book_genre(book_name, book_genre)
        assert collector_without_books.books_genre.get(book_name) == book_genre

    def test_set_book_genre_genre_not_in_genre_list_genre_is_not_set(self, collector_without_books):

        book_name = 'Кортик'
        book_genre = 'Приключения'
        collector_without_books.add_new_book(book_name)
        collector_without_books.set_book_genre(book_name, book_genre)
        assert collector_without_books.books_genre.get(book_name) == ''

    @pytest.mark.parametrize(
        'books_name,books_genre',
        [
            ['Черновик', 'Фантастика'],
            ['Сияние', 'Ужасы'],
            ['Момент истины', 'Детективы'],
            ['Незнайка на луне', 'Мультфильмы'],
            ['Двенадцать стульев', 'Комедии']
        ]
    )
    def test_get_books_with_specific_genre_genre_in_genre_list_returns_books_with_genre(self, collector_with_books_of_all_genres, books_name, books_genre):

        books_with_genre = collector_with_books_of_all_genres.get_books_with_specific_genre(books_genre)
        assert books_with_genre == [books_name]

    @pytest.mark.parametrize(
        'books_name,books_genre',
        [
            ['Черновик', 'Фантастика'],
            ['Сияние', 'Ужасы'],
            ['Момент истины', 'Детективы'],
            ['Незнайка на луне', 'Мультфильмы'],
            ['Двенадцать стульев', 'Комедии']
        ]
    )
    def test_get_book_genre_book_with_genre_returns_book_genre(self, collector_with_books_of_all_genres, books_name, books_genre):

        result_book_genre = collector_with_books_of_all_genres.get_book_genre(books_name)
        assert result_book_genre == books_genre

    def test_get_books_for_children_returns_books_without_age_rating(self, collector_with_books_with_age_rating):

        target_books_for_child = ['Черновик']
        books_for_child = collector_with_books_with_age_rating.get_books_for_children()
        assert books_for_child == target_books_for_child

    def test_add_book_in_favorites_book_in_books_genre_book_is_added(self, collector_without_books):

        book_name = 'Момент истины'
        collector_without_books.add_new_book(book_name)
        collector_without_books.add_book_in_favorites(book_name)
        assert collector_without_books.favorites == ['Момент истины']

    def test_add_book_in_favorites_book_not_in_books_genre_book_is_not_added(self, collector_without_books):

        book_name = 'Момент истины'
        collector_without_books.add_book_in_favorites(book_name)
        assert collector_without_books.favorites == []

    def test_delete_book_from_favorites_book_in_favorites_book_is_deleted(self, collector_without_books):

        book_name = 'Момент истины'
        collector_without_books.add_new_book(book_name)
        collector_without_books.add_book_in_favorites(book_name)
        collector_without_books.delete_book_from_favorites(book_name)
        assert collector_without_books.favorites == []

    def test_get_list_of_favorites_books_2_books_in_favorites_returns_2_books(self, collector_without_books):

        books = ['Черновик', 'Момент истины']
        for book_name in books:
            collector_without_books.add_new_book(book_name)
            collector_without_books.add_book_in_favorites(book_name)

        favorite_books = collector_without_books.get_list_of_favorites_books()
        assert favorite_books == ['Черновик', 'Момент истины']