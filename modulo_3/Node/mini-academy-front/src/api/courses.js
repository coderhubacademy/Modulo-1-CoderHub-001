const BASE_URL = "http://localhost:3000/api";

export async function getCourses() {
  const response = await fetch(`${BASE_URL}/courses`);
  if (!response.ok) {
    throw new Error("Error al obtener los cursos");
  }
  return response.json();
}

export async function getCourse(id) {
  const response = await fetch(`${BASE_URL}/courses/${id}`);
  if (!response.ok) {
    throw new Error("Error al obtener el curso");
  }
  console.log("Response", response);
  return response.json();
}
