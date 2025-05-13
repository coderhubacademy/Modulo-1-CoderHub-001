import { useEffect, useState } from "react";
import { useParams } from "react-router-dom";
import { getCourse } from "../api/courses";

export default function CourseView() {
  const { id } = useParams();
  const [course, setCourse] = useState(null);

  useEffect(() => {
    getCourse(id)
      .then((data) => setCourse(data))
      .catch((error) => console.error("Error fetching course:", error));
  }, [id]);

  if (!course) {
    return <div>Cargando...</div>;
  }

  return (
    <div>
      <h1>{course.name}</h1>
      <p>{course.description}</p>
      <p>Duración: {course.duration} horas</p>
    </div>
  );
}
