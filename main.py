from models import Book
from storage import BookStorage
from stats import calculate_average_rating, display_author_statistics
from datetime import datetime


def print_menu():
    """Выводит главное меню"""
    print("\n" + "="*40)
    print("   ТРЕКЕР ПРОЧИТАННЫХ КНИГ")
    print("="*40)
    print("1. Добавить книгу")
    print("2. Показать все книги")
    print("3. Показать среднюю оценку")
    print("4. Статистика по авторам")
    print("5. Удалить книгу")
    print("6. Выход")
    print("-"*40)


def add_book_interactive(storage):
    """Интерактивное добавление книги"""
    print("\n=== Добавление новой книги ===")
    
    try:
        author = input("Введите автора: ").strip()
        if not author:
            print(" Ошибка: автор не может быть пустым")
            return
        
        title = input("Введите название: ").strip()
        if not title:
            print(" Ошибка: название не может быть пустым")
            return
        
        rating = input("Введите оценку (1-5): ").strip()
        try:
            rating = int(rating)
            if not 1 <= rating <= 5:
                print(" Ошибка: оценка должна быть от 1 до 5")
                return
        except ValueError:
            print(" Ошибка: оценка должна быть целым числом")
            return
        
        date_read = datetime.now().strftime("%Y-%m-%d")
        
        book = Book(author=author, title=title, rating=rating, date_read=date_read)
        
        if storage.add_book(book):
            print(f" Книга '{title}' успешно добавлена!")
        else:
            print(f" Книга '{title}' уже существует в списке!")
            
    except ValueError as e:
        print(f" Ошибка: {e}")


def show_all_books(storage):
    """Показывает все книги"""
    books = storage.get_all_books()
    
    if not books:
        print("\n Список книг пуст. Добавьте первую книгу!")
        return
    
    print("\n=== Список прочитанных книг ===")
    print("-" * 60)
    for i, book in enumerate(books, 1):
        print(f"{i}. {book}")
    print("-" * 60)
    print(f"Всего книг: {len(books)}")


def show_average_rating(storage):
    """Показывает среднюю оценку"""
    books = storage.get_all_books()
    average = calculate_average_rating(books)
    
    print("\n=== Средняя оценка ===")
    if average > 0:
        print(f"Средняя оценка всех книг: {average}/5")
    else:
        print("Нет данных для расчёта средней оценки")


def delete_book_interactive(storage):
    """Интерактивное удаление книги"""
    print("\n=== Удаление книги ===")
    
    author = input("Введите автора книги: ").strip()
    title = input("Введите название книги: ").strip()
    
    if storage.delete_book(author, title):
        print(f" Книга '{title}' успешно удалена!")
    else:
        print(f" Книга '{title}' не найдена!")


def main():
    """Главная функция приложения"""
    storage = BookStorage()
    
    actions = {
        '1': add_book_interactive,
        '2': show_all_books,
        '3': show_average_rating,
        '4': lambda s: display_author_statistics(s.get_all_books()),
        '5': delete_book_interactive,
    }
    
    print("Добро пожаловать в Трекер прочитанных книг!")
    
    while True:
        print_menu()
        choice = input("Выберите действие (1-6): ").strip()
        
        if choice == '6':
            print("\n До свидания! Хорошего дня!")
            break
        
        if choice in actions:
            actions[choice](storage)
            input("\nНажмите Enter, чтобы продолжить...")
        else:
            print("\n Неверный выбор! Пожалуйста, выберите от 1 до 6.")


if __name__ == "__main__":
    main()
