# FEATURE/NEW-STORAGE BRANCH
# Добавлена проверка дубликатов книг

import json
import os
from models import Book


class BookStorage:
    def __init__(self, filename: str = "books.json"):
        self.filename = filename
        self._ensure_file_exists()
    
    def _ensure_file_exists(self):
        if not os.path.exists(self.filename):
            self._save_books([])
    
    def _load_books(self):
        try:
            with open(self.filename, 'r', encoding='utf-8') as f:
                return json.load(f)
        except:
            return []
    
    def _save_books(self, books_data):
        with open(self.filename, 'w', encoding='utf-8') as f:
            json.dump(books_data, f, ensure_ascii=False, indent=2)
    
    def get_all_books(self):
        books_data = self._load_books()
        return [Book.from_dict(book) for book in books_data]
    
    def add_book(self, book):
        books = self.get_all_books()
        
        # ПРОВЕРКА НА ДУБЛИКАТЫ (новая функциональность)
        for existing_book in books:
            if existing_book.author.lower() == book.author.lower() and existing_book.title.lower() == book.title.lower():
                return False  # Книга уже существует
        
        books.append(book)
        self._save_books([b.to_dict() for b in books])
        return True
    
    def delete_book(self, author, title):
        books = self.get_all_books()
        books = [b for b in books if not (b.author.lower() == author.lower() and b.title.lower() == title.lower())]
        self._save_books([b.to_dict() for b in books])
        return True
        
