const estudiantes = require("../models/studentModel");

exports.listarEstudiantes = (req, res) => {
  // console.log("Listando estudiantes", estudiantes);
  // res.status(200);
  // res.end("Estudiantes listados");

  res.render("students", {
    estudiantes: estudiantes,
    titulo: "Lista de Estudiantes",
  });
};

exports.crearEstudiante = (req, res) => {
  const { nombre, edad } = req.body;
  const nuevoEstudiante = {
    id: estudiantes.length + 1,
    nombre: nombre,
    edad: edad,
  };
  estudiantes.push(nuevoEstudiante);
  res.status(201);
  res.redirect("/students");
};
