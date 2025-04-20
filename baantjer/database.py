import sqlite3
import csv

def import_csv():
    conn = sqlite3.connect('data.db')
    c = conn.cursor()

    # Create table if it doesn't exist
    c.execute('''
        CREATE TABLE IF NOT EXISTS boekenlijst (
            number INTEGER,
            title TEXT,
            isbn INTEGER,
            year INTEGER,
            available TEXT 
        )
    ''')

    try:
        with open('data.csv', 'r', encoding='utf8') as csvfile:
            reader = csv.reader(csvfile)
            for row in reader:
                if row:
                    c.execute(
                        'INSERT INTO boekenlijst (number, title, isbn, year, available) VALUES (?, ?, ?, ?, ?)',
                        row
                    )
        print("CSV file imported successfully into boekenlijst")
    except Exception as e:
        print(f"Error importing CSV: {str(e)}")

    conn.commit()
    conn.close()

if __name__ == '__main__':
    import_csv()