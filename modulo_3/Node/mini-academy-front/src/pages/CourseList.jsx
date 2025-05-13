import { useEffect, useState } from "react";
import { Link } from "react-router-dom";

export default function CourseList() {
  const [courses, setCourses] = useState([]);

  useEffect(() => {
    fetch("http://localhost:3000/api/courses")
      .then((response) => response.json())
      .then((data) => setCourses(data));
  }, []);

  return (
    <div>
      <h1>Lista de Cursos</h1>
      <ul>
        {courses.map((course) => (
          <>
            <h2>{course.name}</h2>
            <Link to={`/cursos/${course.id}`}> Ver curso </Link>
          </>
        ))}
      </ul>
    </div>
  );
}
