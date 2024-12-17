"""Control the flow of the app"""


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


def main():
    # Display the main menu
    MenuDisplay.display_menu()


if __name__ == "__main__":
    main()
