-- psql -U postgres -d dci -f create_tables.sql

CREATE SCHEMA IF NOT EXISTS project;
SET search_path TO project;

-- Create enum type
CREATE TYPE book_category_enum AS ENUM('programming', 'art', 'history' , 'politics', 'other');
CREATE TYPE reader_title_enum AS ENUM('Mrs', 'Mr', 'Dr', 'Ms', 'Miss');

-- Create tables
--- BOOK
CREATE TABLE book(
    isbn CHAR(13) PRIMARY KEY,
    title VARCHAR(100) NOT NULL,
    edition INT,
    description TEXT,
    page_count INT NOT NULL,
    category book_category_enum,
    published_date INT NOT NULL,
    publisher VARCHAR(100) NOT NULL,
    authors VARCHAR(100) ARRAY,
    lang VARCHAR(100) NOT NULL,
    format VARCHAR(10),
    read_estimated_time_in_minutes INT GENERATED ALWAYS AS ((page_count * 120)/60) STORED,

    -- Checks
    CHECK(LENGTH(isbn) = 13 AND isbn::BIGINT = isbn::BIGINT),
    CHECK(format in ('ebook', 'hardcover'))
);


-- READER
CREATE TABLE reader (
    username VARCHAR(50) PRIMARY KEY,
    title reader_title_enum,
    first_name VARCHAR(100) NOT NULL,
    last_name VARCHAR(100)
);

-- MYREAD
CREATE TABLE my_read(
    id SERIAL PRIMARY KEY,
    book_isbn CHAR(13) REFERENCES book(isbn),
    reader_username VARCHAR(50) REFERENCES reader(username),
    percentage_read INT DEFAULT 0,
    start_read_date DATE,
    end_read_date DATE

    -- FOREIGN KEY (book_isbn) REFERENCES book(isbn),
    -- FOREIGN KEY (reader_username) REFERENCES reader(username)

    -- EXERCISE - ADD ALL CONSTRAINTS

);

-- STATUS PERCENT

CREATE TABLE status_percent (
    read_status varchar(10) primary key,
    percentage_read INT4RANGE NOT NULL
);

