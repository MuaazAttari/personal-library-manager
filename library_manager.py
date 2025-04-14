import json
import uuid
import os


class BookCollection:
    """A class to manage a collection of books, allowing users to store and organize their reading materials."""

    def __init__(self):
        """This sets up our book collection. If a file with books exists, we load it, otherwise we start fresh."""
        self.book_list = []
        self.storage_file = "books_data.json"
        self.read_from_file()

    def read_from_file(self):
        """This loads saved books from the JSON file so we don’t lose data between uses."""
        if os.path.exists(self.storage_file):
            try:
                with open(self.storage_file, "r") as file:
                    self.book_list = json.load(file)
            except json.JSONDecodeError:
                # If there's an error in reading, we start with an empty list
                print("⚠️ Warning: Could not read from file, starting with an empty collection.\n")
                self.book_list = []
        else:
            self.book_list = []

    def save_to_file(self):
        """Saves the current book list to a JSON file so it's not lost after closing the app."""
        with open(self.storage_file, "w") as file:
            json.dump(self.book_list, file, indent=4)

    def create_new_book(self):
        """Lets the user add a new book by typing in details."""
        print("\n📘 Add a New Book")
        book_title = input("Enter book title: ").strip()
        book_author = input("Enter author: ").strip()
        publication_year = input("Enter publication year: ").strip()
        book_genre = input("Enter genre: ").strip()
        is_book_read = input("Have you read this book? (yes/no): ").strip().lower() == "yes"

        # Create a dictionary for the book with a unique ID
        new_book = {
            "id": str(uuid.uuid4()),
            "title": book_title,
            "author": book_author,
            "year": publication_year,
            "genre": book_genre,
            "read": is_book_read,
        }

        # Add the new book to the list and save it
        self.book_list.append(new_book)
        self.save_to_file()
        print("✅ Book added successfully!\n")

    def delete_book(self):
        """Removes a book from the list by title."""
        book_title = input("Enter the title of the book to remove: ").strip()

        for book in self.book_list:
            if book["title"].lower() == book_title.lower():
                self.book_list.remove(book)
                self.save_to_file()
                print("🗑️ Book removed successfully!\n")
                return
        print("❌ Book not found!\n")

    def find_book(self):
        """Searches for books by title or author name."""
        search_text = input("Enter search term (title or author): ").strip().lower()
        found_books = [
            book for book in self.book_list
            if search_text in book["title"].lower() or search_text in book["author"].lower()
        ]

        if found_books:
            print("\n🔍 Matching Books:")
            for index, book in enumerate(found_books, 1):
                reading_status = "Read" if book["read"] else "Unread"
                print(
                    f"{index}. {book['title']} by {book['author']} ({book['year']}) - {book['genre']} - {reading_status}"
                )
        else:
            print("😕 No matching books found.\n")

    def update_book(self):
        """Edits details of an existing book."""
        book_title = input("Enter the title of the book you want to edit: ").strip()

        for book in self.book_list:
            if book["title"].lower() == book_title.lower():
                print("\n✏️ Leave blank to keep the current value.")
                book["title"] = input(f"New title ({book['title']}): ") or book["title"]
                book["author"] = input(f"New author ({book['author']}): ") or book["author"]
                book["year"] = input(f"New year ({book['year']}): ") or book["year"]
                book["genre"] = input(f"New genre ({book['genre']}): ") or book["genre"]

                read_input = input("Have you read this book? (yes/no): ").strip().lower()
                if read_input in ["yes", "no"]:
                    book["read"] = (read_input == "yes")

                self.save_to_file()
                print("✅ Book updated successfully!\n")
                return
        print("❌ Book not found!\n")

    def toggle_read_status(self):
        """Changes the read/unread status of a book."""
        book_title = input("Enter the title of the book to mark as read/unread: ").strip()

        for book in self.book_list:
            if book["title"].lower() == book_title.lower():
                book["read"] = not book["read"]
                self.save_to_file()
                status = "Read" if book["read"] else "Unread"
                print(f"📖 Book marked as '{status}'.\n")
                return
        print("❌ Book not found!\n")

    def show_all_books(self):
        """Displays every book in the list with all their info."""
        if not self.book_list:
            print("📭 Your collection is empty.\n")
            return

        print("\n📚 Your Book Collection:")
        for index, book in enumerate(self.book_list, 1):
            reading_status = "Read" if book["read"] else "Unread"
            print(
                f"{index}. {book['title']} by {book['author']} ({book['year']}) - {book['genre']} - {reading_status}"
            )
        print()

    def show_reading_progress(self):
        """Shows how many books you've read out of the total collection."""
        total_books = len(self.book_list)
        completed_books = sum(1 for book in self.book_list if book["read"])
        completion_rate = (completed_books / total_books * 100) if total_books > 0 else 0

        print(f"\n📊 Total books in collection: {total_books}")
        print(f"📈 Books read: {completed_books}")
        print(f"📘 Reading progress: {completion_rate:.2f}%\n")

    def start_application(self):
        """Starts the main menu loop where users choose what they want to do."""
        while True:
            print("\n📚📖 ===== Book Collection Manager Menu ===== 📖📚")
            print("1️⃣  Add a new book")
            print("2️⃣  Remove a book")
            print("3️⃣  Search for books")
            print("4️⃣  Update book details")
            print("5️⃣  Mark book as read/unread")
            print("6️⃣  View all books")
            print("7️⃣  View reading progress")
            print("8️⃣  Exit the program")

            user_choice = input("👉 Please choose an option (1-8): ")

            match user_choice:
                case "1":
                    self.create_new_book()
                case "2":
                    self.delete_book()
                case "3":
                    self.find_book()
                case "4":
                    self.update_book()
                case "5":
                    self.toggle_read_status()
                case "6":
                    self.show_all_books()
                case "7":
                    self.show_reading_progress()
                case "8":
                    self.save_to_file()
                    print("👋 Thanks for using Book Collection Manager! Goodbye!\n")
                    break
                case _:
                    print("⚠️ Oops! Invalid choice. Please try again.\n")


# This part runs the program when you launch the file directly
if __name__ == "__main__":
    book_manager = BookCollection()
    book_manager.start_application()
