const sqlite3 = require("sqlite3").verbose();
const db = new sqlite3.Database("academy-api-app.db", (err) => {
  if (err) {
    console.error("Error opening database " + err.message);
  } else {
    console.log("Connected to the SQlite database.");
  }
});

db.serialize(() => {
  db.run(
    `CREATE TABLE IF NOT EXISTS courses (
      id INTEGER PRIMARY KEY AUTOINCREMENT,
      name TEXT NOT NULL,
      duration INTEGER NOT NULL,
      price REAL NOT NULL,
      description TEXT NOT NULL
    )`,
    (err) => {
      if (err) {
        console.error("Error creating courses table " + err.message);
      } else {
        console.log("Table courses created or already exists.");
      }
    }
  );

  db.run(
    `CREATE TABLE IF NOT EXISTS students (
      id INTEGER PRIMARY KEY AUTOINCREMENT,
      name TEXT NOT NULL,
      age INTEGER NOT NULL,
      email TEXT NOT NULL,
      phone TEXT NOT NULL
    )`,
    (err) => {
      if (err) {
        console.error("Error creating students table " + err.message);
      } else {
        console.log("Table students created or already exists.");
      }
    }
  );

  db.run(
    `CREATE TABLE IF NOT EXISTS instructors (
      id INTEGER PRIMARY KEY AUTOINCREMENT,
      name TEXT NOT NULL,
      email TEXT NOT NULL,
      phone TEXT NOT NULL,
      porcentaje INTEGER NOT NULL
    )`,
    (err) => {
      if (err) {
        console.error("Error creating instructors table " + err.message);
      } else {
        console.log("Table instructors created or already exists.");
      }
    }
  );

  db.run(
    `CREATE TABLE IF NOT EXISTS course_students (
      id INTEGER PRIMARY KEY AUTOINCREMENT,
      student_id INTEGER NOT NULL REFERENCES students(id),
      course_id INTEGER NOT NULL REFERENCES courses(id)
    )`,
    (err) => {
      if (err) {
        console.error("Error creating enrollments table " + err.message);
      } else {
        console.log("Table enrollments created or already exists.");
      }
    }
  );

  db.run(
    `CREATE TABLE IF NOT EXISTS course_instructors (
      id INTEGER PRIMARY KEY AUTOINCREMENT,
      instructor_id INTEGER NOT NULL REFERENCES instructors(id),
      course_id INTEGER NOT NULL REFERENCES courses(id)
    )`,
    (err) => {
      if (err) {
        console.error("Error creating course_instructors table " + err.message);
      } else {
        console.log("Table course_instructors created or already exists.");
      }
    }
  );
});

module.exports = db;
