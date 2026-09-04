import sqlite3

conn = sqlite3.connect(
    "youtube_manager.db"
)  # conn is used to connect with sql lite3 and commit the changes

cursor = conn.cursor()  # cursor is used to execute the sql query

cursor.execute("""CREATE TABLE IF NOT EXISTS videos (
    id INTEGER PRIMARY KEY,
    name TEXT NOT NULL,
    time TEXT NOT NULL
)""")


def list_videos():
    cursor.execute("SELECT * FROM videos")
    for row in cursor.fetchall():
        print("-" * 70)
        print(row)


def add_video(name, time):
    cursor.execute("INSERT INTO videos(name, time) VALUES (?, ?)", (name, time))
    conn.commit()  # commit() is used to save permanently in the database


def update_video(video_id, new_name, new_time):
    cursor.execute(
        "UPDATE videos SET name = ?, time = ? WHERE id = ?",
        (new_name, new_time, video_id),
    )
    conn.commit()


def delete_video(video_id):
    cursor.execute("DELETE FROM videos WHERE id = ?", (video_id,))
    conn.commit()


def main():
    while True:
        print("\n Youtube manager app with DB")
        print("1. List videos")
        print("2. Add videos")
        print("3. Update videos")
        print("4. Delete videos")
        print("5. exit videos")
        choice = input("Enter your choice: ")

        match choice:
            case "1":
                list_videos()
            case "2":
                name = input("Enter the video name: ")
                time = input("Enter the video time: ")
                add_video(name, time)
            case "3":
                video_id = input("Enter video ID to update: ")
                new_name = input("Enter the video name: ")
                new_time = input("Enter the video time: ")
                update_video(video_id, new_name, new_time)
            case "4":
                video_id = input("Enter video ID to delete: ")
                delete_video(video_id)
            case "5":
                break
            case _:
                print("Invalid choice")

    conn.close()


if __name__ == "__main__":
    main()
