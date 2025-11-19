import sqlite3, os

db = os.path.join(os.path.dirname(__file__), 'database.db')
print('DB path:', os.path.abspath(db))
if not os.path.exists(db):
    print('Database file not found')
    raise SystemExit(1)

conn = sqlite3.connect(db)
cur = conn.cursor()
cur.execute("SELECT name FROM sqlite_master WHERE type='table'")
tables = [r[0] for r in cur.fetchall()]
print('Tables:', tables)
counts = {}
for t in tables:
    try:
        cur.execute(f'SELECT COUNT(*) FROM {t}')
        counts[t] = cur.fetchone()[0]
    except Exception as e:
        counts[t] = str(e)
print('Counts:')
for k, v in counts.items():
    print(f'  {k}: {v}')
conn.close()

