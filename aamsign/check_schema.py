import sqlite3

def check_schema():
    try:
        conn = sqlite3.connect('db.sqlite3')
        cursor = conn.cursor()
        cursor.execute("PRAGMA table_info(shop_product)")
        columns = cursor.fetchall()
        
        found = False
        print("Columns in shop_product:")
        for col in columns:
            print(f"- {col[1]}")
            if col[1] == 'subcategory':
                found = True
        
        if found:
            print("\nSUCCESS: 'subcategory' column FOUND.")
        else:
            print("\nFAILURE: 'subcategory' column NOT FOUND.")
            
        conn.close()
    except Exception as e:
        print(f"Error: {e}")

if __name__ == '__main__':
    check_schema()
