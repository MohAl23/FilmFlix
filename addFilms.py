from connect import *  

def insert_films():
    films = []
    fName = input("Enter Film Title: ")
    year = input("Enter Release Year: ")
    rate = input("Enter Mature Rating: ")
    fDuration = input("Enter Film Duration: ")
    fGenre = input("Enter Film Genre: ")
    
    
    
    # Printing data for verification
    print(f"Data: {fName}, {year},{fGenre} ")
    
    films.append(fName)
    films.append(year)
    films.append(rate)
    films.append(fDuration)
    films.append(fGenre)
   

    try:
        # Using placeholders and parameters to prevent SQL injection
        dbCursor.execute("INSERT INTO tblFilms (title, yearReleased, rating, duration, genre)VALUES (?, ?, ?, ?, ?)", (fName, year,rate,fDuration,fGenre ))
        dbCon.commit()
        print(f"{fName} inserted into the Table")
    except sqlite3.OperationalError as e:
        dbCon.rollback()
        print(f"Insert failed: {e}")

if __name__ == "__main__":
    insert_films()