from connect import *

# create a subroutine
def update_films():
    try:
        # the id of the record to be updated
        idField = input("Enter the filmID to update a record: ")

        # select a record using FilmID from the table
        dbCursor.execute(f"SELECT * FROM tblFilms WHERE filmID = {idField}")
        
        row = dbCursor.fetchone()  # use fetchone() to fetch the selected record

        # None: A singleton object used to check/signal if value is absent
        if row == None:  # row is the record returned based on the specific FilmID
            print(f"No record with the filmID {idField} exists")
        else:
            # the field selected for update
            fieldName = input("Enter the field (Film Title, Year, Rating, Duration, or Genre) to update: ").title()

            # get the new value for the selected field
            fieldValue = input(f"Enter the new value for {fieldName}: ")

            # UPDATE tblFilms SET Title = "New Title" WHERE FilmID = 1/2/3/4....
            # use FilmID as a primary and unique field to update a record
            dbCursor.execute(f"UPDATE tblFilms SET {fieldName} = ? WHERE filmID = ?", (fieldValue, idField))
            dbCon.commit()
            print(f"{idField} Updated in the Films table")
    except sqlite3.OperationalError as e:
        print(f"Update failed: {e}")

if __name__ == "__main__":
    update_films()
