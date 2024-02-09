from connect import * 
import logging
import time
filename = __name__
logging.basicConfig(filename=r"Python Project/filmflix.db", level=logging.DEBUG)



# create a subroutine
def search():
    try:
        field = input("Would you like to search by filmID, title, yearReleased, rating, duration or genre? ")
        if field == "filmID":
            idInput = input("Enter the filmID to search: ")
            dbCursor.execute(f"SELECT * FROM tblFilms WHERE filmID = {idInput}")
            row = dbCursor.fetchone()
            
            if row is None:
                print(f"No record with the filmID {idInput} exists")
                logging.warning(f"On {time.asctime()}, file is {filename}, user entered {idInput} as {field}")
            else:
                for aRecord in row:
                    print(aRecord)
        elif field in ["title", "yearReleased", "rating", "duration", "genre"]:
            searchInput = input(f"Enter the {field} to search: ")
            dbCursor.execute(f"SELECT * FROM tblFilms WHERE {field} = '{searchInput}'")
            rows = dbCursor.fetchall()
            if not rows:
                print(f"No record with the {field} {searchInput} exists")
            else:
                for aRecord in rows:
                    print(aRecord)
        else:
            print(f"Invalid {field}, please try again")
    except sqlite3.OperationalError as e:
        print(f"Search failed: {e}")

if __name__ == "__main__":
    search()        
            
