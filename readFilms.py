from connect import * 


# create a subroutine
def read_films():
    try:  # select all records from the table
        
        # dbCursor.execute("SELECT * FROM downloads")
        #fetchall(): fetehes all the the selected records
        dbCursor.execute("SELECT * FROM tblFilms")# row holds alll fetched records
        rows = dbCursor.fetchall()
            
        if not rows: # row is the record returned based on the specific MemberID
            print(f"No record(s) exists")
        # loop through all the records in the row variable 
        else:
            for aRecord in rows:
                # print all record 
                print(aRecord)
    except sqlite3.OperationalError as e:
        print(f"Records not found: {e}")
if __name__ == "__main__":
    read_films()

