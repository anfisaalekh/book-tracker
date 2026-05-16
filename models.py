from dataclasses import dataclass
from datetime import datetime


@dataclass
class Book:
    """Класс, представляющий книгу"""
    author: str
    title: str
    rating: int
    date_read: str
    
    def __post_init__(self):
        """Валидация данных после инициализации"""
        if not self.author or not self.author.strip():
            raise ValueError("Автор не может быть пустым")
        
        if not self.title or not self.title.strip():
            raise ValueError("Название не может быть пустым")
        
        if not 1 <= self.rating <= 5:
            raise ValueError("Оценка должна быть от 1 до 5")
        
        try:
            datetime.strptime(self.date_read, "%Y-%m-%d")
        except ValueError:
            raise ValueError("Дата должна быть в формате YYYY-MM-DD")
    
    def to_dict(self) -> dict:
        """Преобразует объект книги в словарь для JSON"""
        return {
            "author": self.author,
            "title": self.title,
            "rating": self.rating,
            "date_read": self.date_read
        }
    
    @classmethod
    def from_dict(cls, data: dict) -> 'Book':
        """Создаёт объект книги из словаря"""
        return cls(
            author=data["author"],
            title=data["title"],
            rating=data["rating"],
            date_read=data["date_read"]
        )
    
    def __str__(self) -> str:
        """Строковое представление книги"""
        return f"{self.author} - {self.title} (Оценка: {self.rating}/5, Дата: {self.date_read})"
