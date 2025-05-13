const courseModel = require("../models/CourseModel");

exports.getAllCourses = (req, res) => {
  courseModel.getAllCourses((err, courses) => {
    if (err) {
      res.status(500).json({ error: err.message });
    } else {
      res.status(200).json(courses);
    }
  });
};

exports.getCourseById = (req, res) => {
  console.log("Params", req.params);
  console.log("Query", req.query);
  const courseId = req.params.id;
  courseModel.getCourseById(courseId, (err, course) => {
    if (err) {
      res.status(500).json({ error: err.message });
    } else if (!course) {
      res.status(404).json({ error: "Course not found" });
    } else {
      res.status(200).json(course);
    }
  });
};

exports.createCourse = (req, res) => {
  const newCourse = req.body;
  courseModel.createCourse(newCourse, (err, course) => {
    if (err) {
      res.status(500).json({ error: err.message });
    } else {
      res.status(201).json(course);
    }
  });
};
exports.updateCourse = (req, res) => {
  const courseId = req.params.id;
  const updatedCourse = req.body;
  courseModel.updateCourse(courseId, updatedCourse, (err, result) => {
    if (err) {
      res.status(500).json({ error: err.message });
    } else if (result.changes === 0) {
      res.status(404).json({ error: "Course not found" });
    } else {
      res.status(200).json({ message: "Course updated successfully" });
    }
  });
};

exports.deleteCourse = (req, res) => {
  const courseId = req.params.id;
  courseModel.deleteCourse(courseId, (err, result) => {
    if (err) {
      res.status(500).json({ error: err.message });
    } else if (result.changes === 0) {
      res.status(404).json({ error: "Course not found" });
    } else {
      res.status(200).json({ message: "Course deleted successfully" });
    }
  });
};
