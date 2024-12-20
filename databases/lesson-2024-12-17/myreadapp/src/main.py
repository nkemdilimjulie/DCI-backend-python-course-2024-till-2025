"""Control the flow of the app"""

from src import utils
from src.db.models.book import Book
from src.db.models.reader import Reader


class MenuDisplay:
    """
    MENU
    ----------------
    1. DATA MANIPULATION
        1. INSERT READER
        2. INSERT BOOK
        3. INSERT MYREAD
    2. DATA QUERY
        1. HOW MAY BOOKS DO WE HAVE IN THE DATABASE
    """

    @staticmethod
    def display_menu():
        print(
            """
        WELCOME TO MY READ APP
        
        MENU
        -----------
        1. DATA MANIPULATION
        2. DATA QUERY
        99. QUIT
        """
        )

    @staticmethod
    def display_DM_menu():
        print(
            """
        MENU > DATA MANIPULATION
        ----------
        1. INSERT READER
        2. INSERT BOOK
        3. INSERT MYREAD
        99.QUIT
        00. BACK
        
        """
        )

    @staticmethod
    def display_DQ_menu():
        print(
            """
              MENU > DATA QUERY
            --------------
            1. List title of all ebooks read by Doctors?
            2. How many books are there altogether?
            3. How many readers are done reading at least one book?
            4. How many books do we have per category?
            5. How many books do we have per read status?
            6. Who completely read the most books and how many?
            7. Who haven't read a single book yet?
            8. Which book is the most popular(read the most)?
            99.QUIT
            00.Back
            """
        )


class InputOption:
    @staticmethod
    def book_insert_input():
        fields = [
            "isbn",
            "title",
            "edition",
            "description",
            "page_count",
            "category",
            "published_date",
            "publisher",
            "authors",
            "lang",
            "format",
        ]
        optionals = [2, 3, 5, 8, 10]
        extra_info = {
            5: "(programming, art, history, politics, other)",
            10: "(ebook, hardcover)",
            8: "(Separated by comma)",
        }
        data = utils.insert_inputs(fields, optionals, extra_detail=extra_info)
        # Process the data before returning
        data["authors"] = data["authors"].split(",") if data["authors"] else None
        data["page_count"] = int(data["page_count"])
        data["published_date"] = int(data["published_date"])
        data["edition"] = int(data["edition"]) if data["edition"] else None

        # TODO: Do more checks like for 'format', and 'category'
        return data

    @staticmethod
    def reader_insert_input():
        fields = ["username", "title", "first_name", "last_name"]
        optionals = [1, 3]
        extra_fields = {1: "(Mrs, Mr, Dr, Ms, Miss)"}

        data = utils.insert_inputs(fields, optionals, extra_detail=extra_fields)
        # TODO: Check that title's value is what is supported or raise a ValueError

        return data


def main():
    # Display the main menu
    while True:
        MenuDisplay.display_menu()
        option = input("Choose an option to continue: ")
        if option == "1":
            while True:
                MenuDisplay.display_DM_menu()
                option = input("Choose an option to continue: ")
                if option == "1":
                    # TODO: INSERT READER
                    reader_data = InputOption.reader_insert_input()
                    # insert into the database
                    inserted_data = Reader.insert_data(**reader_data)
                    if inserted_data:
                        print(f"Reader {inserted_data.username} inserted successfully")
                    else:
                        print("Insertion failed!!!")

                elif option == "2":
                    # TODO: INSERT BOOK
                    book_details = InputOption.book_insert_input()
                    inserted_data = Book.insert_data(**book_details)

                    if inserted_data:
                        print(f"Book '{inserted_data.title}' inserted successfully")
                    else:
                        print("Insertion failed!!!")

                elif option == "3":
                    # TODO: INSERT MYREAD
                    ## Step 1: Display all books(counter, book title), then ask the user to select
                    ## Step 2: Get the reader's username (Assumption: Get random reader's username)
                    #### SELECT username FROM reader ORDER BY RANDOM() LIMIT 1;
                    ## Step 3: Get all other input from the user

                    ## Step 4: Insert
                    pass
                elif option == "00":
                    break
                elif option == "99":
                    exit(1)
        elif option == "2":
            # TODO: DQ
            pass
        elif option == "00":
            print("Good Bye!!")
            exit(1)
        else:
            print("The option chosen is not supported!!")
            print("Try again!!")


if __name__ == "__main__":
    main()
