const express = require("express");
const app = express();
const path = require("node:path");
const port = 3000;

studentsContoller = require("./controllers/studentsController");

// Configurar el motor de plantillas EJS
app.set("view engine", "ejs");
app.set("views", path.join(__dirname, "views"));

app.use(express.urlencoded({ extended: true }));

app.get("/", (req, res) => {
  res.send("Bienvenido a mi app");
});

app.get("/students", studentsContoller.listarEstudiantes);
app.post("/students", studentsContoller.crearEstudiante);

app.listen(port, () => {
  console.log(`Example app listening on port ${port}`);
});
