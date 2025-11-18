import sqlite3
import os
from werkzeug.security import generate_password_hash

def seed_database():
    """Seed database with sample data"""
    db_path = os.path.join(os.path.dirname(__file__), 'database.db')
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    
    # Clear existing data (optional - comment out if you want to keep existing data)
    cursor.execute('DELETE FROM proofs')
    cursor.execute('DELETE FROM tasks')
    cursor.execute('DELETE FROM reports')
    cursor.execute('DELETE FROM users')
    
    # Create sample users
    users = [
        ('John Citizen', 'citizen1@example.com', generate_password_hash('password123'), 'citizen'),
        ('Jane Citizen', 'citizen2@example.com', generate_password_hash('password123'), 'citizen'),
        ('Moderator Admin', 'moderator@example.com', generate_password_hash('password123'), 'moderator'),
        ('Volunteer Alice', 'volunteer1@example.com', generate_password_hash('password123'), 'volunteer'),
        ('Volunteer Bob', 'volunteer2@example.com', generate_password_hash('password123'), 'volunteer'),
    ]
    
    user_ids = []
    for user in users:
        cursor.execute('''
            INSERT INTO users (name, email, password_hash, role)
            VALUES (?, ?, ?, ?)
        ''', user)
        user_ids.append(cursor.lastrowid)
    
    # Create sample reports
    reports = [
        (user_ids[0], 'Plastic Waste', 'Large pile of plastic bottles near the park entrance', 'high', 
         'Central Park, Main Entrance', 40.785091, -73.968285, 'uploads/seed/report1.png', 'pending', None, 0),
        (user_ids[0], 'Illegal Dumping', 'Furniture and electronics dumped in alleyway', 'high',
         'Downtown Alley, 5th Street', 40.758896, -73.985130, 'uploads/seed/report2.png', 'valid', 'Verified - needs immediate attention', 1),
        (user_ids[1], 'Litter', 'Cigarette butts and wrappers scattered around', 'low',
         'Riverside Walk', 40.748817, -73.968428, 'uploads/seed/report3.png', 'assigned', 'Assigned to volunteer', 0),
        (user_ids[1], 'Hazardous Waste', 'Broken glass and sharp objects on playground', 'high',
         'Community Playground, Oak Avenue', 40.7282, -73.9942, 'uploads/seed/report4.png', 'in_progress', 'In progress', 0),
        (user_ids[0], 'Organic Waste', 'Food waste attracting pests', 'medium',
         'Market Square', 40.7505, -73.9934, 'uploads/seed/report5.png', 'completed', 'Successfully cleaned up', 0),
    ]
    
    report_ids = []
    for report in reports:
        cursor.execute('''
            INSERT INTO reports (citizen_id, category, description, severity, location_text, 
                               latitude, longitude, photo_path, status, moderator_notes, is_anonymous)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
        ''', report)
        report_ids.append(cursor.lastrowid)
    
    # Create sample tasks
    tasks = [
        (report_ids[0], None, 'pending', None, None),
        (report_ids[1], None, 'pending', None, None),
        (report_ids[2], user_ids[3], 'assigned', '2024-01-15 10:00:00', None),
        (report_ids[3], user_ids[4], 'in_progress', '2024-01-16 09:00:00', None),
        (report_ids[4], user_ids[3], 'completed', '2024-01-14 14:00:00', '2024-01-14 16:30:00'),
    ]
    
    task_ids = []
    for task in tasks:
        cursor.execute('''
            INSERT INTO tasks (report_id, assigned_volunteer_id, status, assigned_at, completed_at)
            VALUES (?, ?, ?, ?, ?)
        ''', task)
        task_ids.append(cursor.lastrowid)
    
    # Create sample proof for completed task
    cursor.execute('''
        INSERT INTO proofs (task_id, volunteer_id, proof_photo_path, notes)
        VALUES (?, ?, ?, ?)
    ''', (task_ids[4], user_ids[3], 'uploads/seed/proof1.png', 'Cleanup completed successfully. All waste removed and area sanitized.'))
    
    conn.commit()
    conn.close()
    print("Database seeded successfully!")
    print("\nTest Credentials:")
    print("Citizen 1: citizen1@example.com / password123")
    print("Citizen 2: citizen2@example.com / password123")
    print("Moderator: moderator@example.com / password123")
    print("Volunteer 1: volunteer1@example.com / password123")
    print("Volunteer 2: volunteer2@example.com / password123")

if __name__ == '__main__':
    seed_database()

