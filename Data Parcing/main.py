import sqlite3
import requests
from LxmlSoup import LxmlSoup  

html = requests.get('https://www.tomfordfashion.com/en-us/eyewear/').text

soup = LxmlSoup(html)

eyeglasses = soup.find_all('a', class_='link')

conn = sqlite3.connect('your_database.db')
cursor = conn.cursor()

cursor.execute("PRAGMA table_info(your_table)")
columns = [column[1] for column in cursor.fetchall()]

if "link_text" not in columns:
    cursor.execute("ALTER TABLE your_table ADD COLUMN link_text TEXT")

if "link_href" not in columns:
    cursor.execute("ALTER TABLE your_table ADD COLUMN link_href TEXT")

conn.commit()

for tag in eyeglasses:
    link_text = tag.get_text(strip=True)
    link_href = tag.get('href')
    cursor.execute("INSERT INTO your_table (link_text, link_href) VALUES (?, ?)",
                   (link_text, link_href))
    print(f"Inserted: {link_text} | {link_href}")

conn.commit()
conn.close()



# from LxmlSoup import LxmlSoup
# import requests

# html = requests.get('https://www.tomfordfashion.com/en-us/eyewear/').text

# soup = LxmlSoup(html)

# eyeglasses = soup.find_all('a', class_='link')
