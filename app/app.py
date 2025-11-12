import os
import mysql.connector
from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/")
def home():
    return jsonify({"message": "Hello from Flask + MySQL!"})

@app.route("/notes")
def notes():
    connection = mysql.connector.connect(
        host=os.getenv("MYSQL_HOST", "localhost"),
        user=os.getenv("MYSQL_USER", "root"),
        password=os.getenv("MYSQL_PASSWORD", "root"),
        database=os.getenv("MYSQL_DATABASE", "devopsdb")
    )

    cursor = connection.cursor()
    cursor.execute("CREATE TABLE IF NOT EXISTS notes (id INT AUTO_INCREMENT PRIMARY KEY, text VARCHAR(255))")
    cursor.execute("INSERT INTO notes (text) VALUES ('Hello from Docker Compose!')")
    connection.commit()

    cursor.execute("SELECT * FROM notes")
    rows = cursor.fetchall()
    cursor.close()
    connection.close()

    return jsonify(rows)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
