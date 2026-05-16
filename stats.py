from typing import List
from models import Book
from collections import defaultdict


def calculate_average_rating(books: List[Book]) -> float:
    """Рассчитывает среднюю оценку всех книг"""
    if not books:
        return 0.0
    
    total_rating = sum(book.rating for book in books)
    return round(total_rating / len(books), 2)


def get_author_statistics(books: List[Book]) -> dict:
    """Получает статистику по авторам"""
    stats = defaultdict(int)
    for book in books:
        stats[book.author] += 1
    return dict(stats)


def display_author_statistics(books: List[Book]) -> None:
    """Отображает статистику по авторам в удобном формате"""
    stats = get_author_statistics(books)
    
    if not stats:
        print("\nНет данных о книгах")
        return
    
    print("\n=== Статистика по авторам ===")
    for author, count in sorted(stats.items(), key=lambda x: x[1], reverse=True):
        print(f"{author}: {count} книга(и)")
