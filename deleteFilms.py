from connect import *

def delete_films():
    try:
        # Use MemberID 
        idfield = input("Enter FilmID: ")
        
        # Select the record you want to delete
        dbCursor.execute(f"SELECT * FROM tblFilms WHERE FilmID = {idfield}")
        selectedrow = dbCursor.fetchone()
        
        # None function is used to check if a value exists
        if selectedrow is None:
            print(f"{idfield} does not exist")
        else:
            dbCursor.execute(f"DELETE FROM tblFilms WHERE FilmID = {idfield}")
            dbCon.commit()
            print(f"{idfield} has been deleted")
            
    except sqlite3.OperationalError as e:
        print(f"Delete failed: {e}")

if __name__ == "__main__":
    delete_films()
        