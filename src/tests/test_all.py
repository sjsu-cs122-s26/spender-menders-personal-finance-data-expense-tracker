from src.service.tests.mockbook import MockBook


def test_all():
    test_book()

def test_book():
    book = MockBook()
    print(book)

test_all()