# qa_python
Tests for BooksCollector class 
Contains:
- test_add_new_book_name_less_than_40_symbols_book_is_added
Tests that add_new_book() method adds a book with a name shorter than 40 characters.

- test_add_new_book_name_more_than_40_or_less_then_1_symbols_book_is_not_added
Tests that add_new_book() method does not add a book if the name is more than 40 or less than 1 symbol

- test_set_book_genre_genre_in_genre_list_genre_is_set
Tests that set_book_genre() method correctly assigns a genre from the allowed list to a book

- test_set_book_genre_genre_not_in_genre_list_genre_is_not_set
Tests that set_book_genre() method does not assign not allowed genre to a book

- test_get_books_with_specific_genre_genre_in_genre_list_returns_books_with_genre
Tests that get_books_with_specific_genre() method returns all books with the given genre

- test_get_book_genre_book_with_genre_returns_book_genre
Tests that get_book_genre() method returns the correct genre for a given book

- test_get_books_for_children_returns_books_without_age_rating
Tests that get_books_for_children() method returns only books without age rating

- test_add_book_in_favorites_book_in_books_genre_book_is_added
Tests that add_book_in_favorites() method adds a book to favorites if it exists in the collection

- test_add_book_in_favorites_book_not_in_books_genre_book_is_not_added
Tests that add_book_in_favorites() method does not add a book that wasn't added to the collection

- test_delete_book_from_favorites_book_in_favorites_book_is_deleted
Tests that delete_book_from_favorites() method removes a book from the favorites list

- test_get_list_of_favorites_books_2_books_in_favorites_returns_2_books
Tests that get_list_of_favorites_books() method returns all favorite books that were added