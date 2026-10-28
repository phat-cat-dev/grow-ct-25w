import { createRoot } from "react-dom/client";
import CourseNode from "./CourseNode.jsx";
import data from "./course-node.sample.json";

createRoot(document.getElementById("root")).render(
  <CourseNode
    course={data.course}
    conceptLabels={data.conceptLabels}
    hrefFor={(l) => `#open-${l.lesson_id}`}
  />
);
