# Feature: Добавлена проверка дубликатов книг
# BRANCH: feature/storage
import json
import os
from typing import List, Optional
from models import Book


class BookStorage:
    """Класс для работы с хранилищем книг"""
    
    def __init__(self, filename: str = "books.json"):
        self.filename = filename
        self._ensure_file_exists()
    
    def _ensure_file_exists(self) -> None:
        """Создаёт файл JSON, если он не существует"""
        if not os.path.exists(self.filename):
            self._save_books([])
    
    def _load_books(self) -> List[dict]:
        """Загружает книги из JSON файла"""
        try:
            with open(self.filename, 'r', encoding='utf-8') as f:
                return json.load(f)
        except (json.JSONDecodeError, FileNotFoundError):
            return []
    
    def _save_books(self, books_data: List[dict]) -> None:
        """Сохраняет книги в JSON файл"""
        with open(self.filename, 'w', encoding='utf-8') as f:
            json.dump(books_data, f, ensure_ascii=False, indent=2)
    
    def get_all_books(self) -> List[Book]:
        """Возвращает список всех книг"""
        books_data = self._load_books()
        return [Book.from_dict(book) for book in books_data]
    
    def add_book(self, book: Book) -> bool:
        """
        Добавляет книгу в хранилище
        Returns True если книга добавлена, False если дубликат
        """
        books = self.get_all_books()
        
        # Проверка на дубликаты
        for existing_book in books:
            if (existing_book.author.lower() == book.author.lower() and 
                existing_book.title.lower() == book.title.lower()):
                return False
        
        books.append(book)
        books_data = [b.to_dict() for b in books]
        self._save_books(books_data)
        return True
    
    def delete_book(self, author: str, title: str) -> bool:
        """Удаляет книгу по автору и названию"""
        books = self.get_all_books()
        initial_count = len(books)
        
        books = [book for book in books 
                if not (book.author.lower() == author.lower() and 
                       book.title.lower() == title.lower())]
        
        if len(books) < initial_count:
            books_data = [b.to_dict() for b in books]
            self._save_books(books_data)
            return True
        return False
    
    def find_book(self, author: str, title: str) -> Optional[Book]:
        """Ищет книгу по автору и названию"""
        books = self.get_all_books()
        for book in books:
            if (book.author.lower() == author.lower() and 
                book.title.lower() == title.lower()):
                return book
        return None
