const db = require("../database/db");

const CourseModel = {
  getAllCourses: (callback) => {
    db.all("SELECT * FROM courses", [], (err, rows) => {
      if (err) {
        callback(err, null);
      } else {
        callback(null, rows);
      }
    });
  },

  getCourseById: (id, callback) => {
    db.get("SELECT * FROM courses WHERE id = ?", [id], (err, row) => {
      if (err) {
        callback(err, null);
      } else {
        callback(null, row);
      }
    });
  },

  createCourse: (course, callback) => {
    db.run(
      "INSERT INTO courses (name, duration, price, description) VALUES (?, ?, ?, ?)",
      [course.name, course.duration, course.price, course.description],
      function (err) {
        if (err) {
          callback(err, null);
        } else {
          callback(null, { id: this.lastID });
        }
      }
    );
  },
  updateCourse: (id, course, callback) => {
    db.run(
      "UPDATE courses SET name = ?, duration = ?, price = ?, description = ? WHERE id = ?",
      [course.name, course.duration, course.price, course.description, id],
      function (err) {
        if (err) {
          callback(err, null);
        } else {
          callback(null, { changes: this.changes });
        }
      }
    );
  },
  deleteCourse: (id, callback) => {
    db.run("DELETE FROM courses WHERE id = ?", [id], function (err) {
      if (err) {
        callback(err, null);
      } else {
        callback(null, { changes: this.changes });
      }
    });
  },
};

module.exports = CourseModel;
