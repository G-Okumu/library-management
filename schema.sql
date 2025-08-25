-- teachers table
-- students table
-- libraries table
-- members table
-- books table
-- librarians table
-- users table

create table IF NOT EXISTS users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    username TEXT UNIQUE NOT NULL,
    password TEXT NOT NULL,
    role TEXT NOT NULL
);

create table libraries (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL
);

create table librarians (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    library_id INTEGER UNIQUE, -- we are associating a librarian with a library
    user_id INTEGER UNIQUE, -- linking this to the user in the system
    FOREIGN KEY (library_id) REFERENCES libraries(id),
    FOREIGN KEY (user_id) REFERENCES users(id)
);

create table books (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    title TEXT NOT NULL,
    library_id INTEGER,
    is_borrowed INTEGER DEFAULT 0, -- 0 means not borrows, NO, 1 will mean borrowed, YES
    FOREIGN KEY (library_id) REFERENCES libraries(id)
);

create table students (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    user_id INTEGER UNIQUE,
    FOREIGN KEY (user_id) REFERENCES users(id)
);


-- A table that will associate borrowed books with the student. Joint table in many to many book student relationship.ABORT

create table borrowed_books(
    student_id INTEGER UNIQUE,
    book_id INTEGER UNIQUE,
    borrowed_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    PRIMARY KEY (student_id, book_id),
    FOREIGN KEY (book_id) REFERENCES books(id),
    FOREIGN KEY (student_id) REFERENCES students(id)
);


