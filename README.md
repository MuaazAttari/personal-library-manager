# Personal Library Manager

## Overview

This is a command-line application that helps you manage your book collection. You can add books, remove books, search for books, display all your books, and view statistics about your reading progress. With the optional file handling feature, you can also save and load your library data.

## Features

* **Add a book:** Add new books to your library, including details like title, author, publication year, genre, and read status (read or unread).
* **Remove a book:** Remove any book from your library by its title.
* **Search for a book:** Search for books in your library by title or author. Matching books will be displayed.
* **Display all books:** View a formatted list of all the books currently in your library.
* **Display statistics:** See basic statistics about your library, such as the total number of books and the percentage of books you have read.
* **Save and Load Library (Optional):** Save your library data to a file when the program exits and load it from the file when the program starts.

## Getting Started

1.  **Prerequisites:** You need to have Python installed on your system.
2.  **Download the script:** Download the `library_manager.py` file.
3.  **Run the application:** Open your command line or terminal, navigate to the directory where you downloaded the file, and run this command:
    ```bash
    python library_manager.py
    ```
4.  **Follow the menu:** Once the application starts, follow the menu options to manage your book collection.

## Usage

After running the application, you will see a menu with available options. Enter your choice (1-8) and follow the instructions.

* **1. Add a new book:** Follow the prompts to enter the book's details.
* **2. Remove a book:** Enter the title of the book you want to remove.
* **3. Search for books:** Enter the search term (title or author).
* **4. Update book details:** Enter the title of the book you want to edit, and then enter the new details. Leave a field blank to keep the current value.
* **5. Mark book as read/unread:** Enter the title of the book to toggle its read status.
* **6. View all books:** See a list of all books in your library.
* **7. View reading progress:** View statistics about your library.
* **8. Exit the program:** Close the application. If file handling is enabled, your library will be saved.

## Optional File Handling

This application saves and loads your library data in a file named `books_data.json`. This file will be created in the same directory as the script when you exit the program (if you have added any books). The next time you run the application, this file will be loaded automatically.

## Contributing

If you'd like to contribute to this project, please feel free to submit pull requests or raise issues.

## License

[You can add your license information here, if you have one.]

## Author

[You can add your name or username here.]
