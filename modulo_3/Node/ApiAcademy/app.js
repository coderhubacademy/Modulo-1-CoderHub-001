const express = require("express");
const app = express();
const cors = require("cors");

// Routes
const coursesRoutes = require("./routes/CoursesRoutes");

app.use(express.json());
app.use(express.urlencoded({ extended: true }));
app.use(cors());

app.use("/api/courses", coursesRoutes);

app.listen(3000, () => {
  console.log("Servidor corriendo en http://localhost:3000");
});
