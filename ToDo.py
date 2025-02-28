import sqlite3

# Database Setup
conn = sqlite3.connect("todo.db")
cursor = conn.cursor()
cursor.execute("""
    CREATE TABLE IF NOT EXISTS tasks (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        task TEXT NOT NULL,
        status TEXT DEFAULT 'Pending'
    )
""")
conn.commit()

# Function to add a task
def add_task():
    task = input("Enter a task: ").strip()
    if task:
        cursor.execute("INSERT INTO tasks (task) VALUES (?)", (task,))
        conn.commit()
        print(f"✅ Task '{task}' added successfully!")
    else:
        print("⚠️ Task cannot be empty.")

# Function to view all tasks
def show_tasks():
    cursor.execute("SELECT * FROM tasks")
    tasks = cursor.fetchall()
    if not tasks:
        print("📭 No tasks found.")
    else:
        print("\n📌 Your To-Do List:")
        for row in tasks:
            print(f"{row[0]}. {row[1]} ({row[2]})")

# Function to mark a task as done
def mark_done():
    show_tasks()
    task_id = input("Enter the task ID to mark as done: ").strip()
    if task_id.isdigit():
        cursor.execute("UPDATE tasks SET status='Completed' WHERE id=?", (task_id,))
        conn.commit()
        print(f"✅ Task {task_id} marked as Completed!")
    else:
        print("⚠️ Invalid ID. Please enter a valid number.")

# Function to delete a task
def delete_task():
    show_tasks()
    task_id = input("Enter the task ID to delete: ").strip()
    if task_id.isdigit():
        cursor.execute("DELETE FROM tasks WHERE id=?", (task_id,))
        conn.commit()
        print(f"🗑 Task {task_id} deleted successfully!")
    else:
        print("⚠️ Invalid ID. Please enter a valid number.")

# Main Menu
def main():
    while True:
        print("\n🔹 To-Do List Menu:")
        print("1️⃣ Add Task")
        print("2️⃣ View Tasks")
        print("3️⃣ Mark Task as Done")
        print("4️⃣ Delete Task")
        print("5️⃣ Exit")

        choice = input("Enter your choice: ").strip()
        if choice == "1":
            add_task()
        elif choice == "2":
            show_tasks()
        elif choice == "3":
            mark_done()
        elif choice == "4":
            delete_task()
        elif choice == "5":
            print("👋 Exiting... Have a great day!")
            break
        else:
            print("⚠️ Invalid choice. Please enter a number between 1 and 5.")

# Run the program
main()