import sqlite3, os

DB = os.path.join(os.path.dirname(__file__), 'database.db')
if not os.path.exists(DB):
    print('Database not found at', DB)
    raise SystemExit(1)

conn = sqlite3.connect(DB)
conn.row_factory = sqlite3.Row
cur = conn.cursor()
cur.execute('SELECT id, name, email, role, created_at FROM users ORDER BY id')
rows = cur.fetchall()
if not rows:
    print('No users found')
else:
    print(f"Found {len(rows)} users:\n")
    for r in rows:
        print(f"id: {r['id']}\n  name: {r['name']}\n  email: {r['email']}\n  role: {r['role']}\n  created_at: {r['created_at']}\n")
conn.close()

