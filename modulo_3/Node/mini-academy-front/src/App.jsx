import { BrowserRouter, Routes, Route } from "react-router-dom";
import CourseList from "./pages/CourseList";
import CourseView from "./pages/CourseView";
import "./App.css";

function App() {
  return (
    <BrowserRouter>
      <Routes>
        <Route path="/" element={<CourseList />} />
        <Route path="/cursos/:id" element={<CourseView />} />
      </Routes>
    </BrowserRouter>
  );
}

export default App;
