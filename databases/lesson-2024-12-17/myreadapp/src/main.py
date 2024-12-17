"""Control the flow of the app"""

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
        00. QUIT
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
            00.Back
            """
        )


class InputOption:
    @staticmethod
    def reader_insert_input():
        username = input("Username: ")
        title = input("Title(Mrs, Mr, Dr, Ms, Miss ): ")
        first_name = input("First Name: ")
        last_name = input("Last Name: ")

        # TODO: Check that title's value is what is supported or raise a ValueError

        return {
            "username": username,
            "title": title,
            "first_name": first_name,
            "last_name": last_name,
        }


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
                    pass
                elif option == "3":
                    # TODO: INSERT MYREAD
                    pass
                elif option == "00":
                    break
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
