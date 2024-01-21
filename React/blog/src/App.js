import logo from "./logo.svg";
import "./App.css";
import { useState } from "react";

function App() {
  let post = "강남 우동 맛집";
  let [글제목, 글내용수정] = useState([
    "남자 코트 추천",
    "강남 우동 맛집",
    "파이썬독학",
  ]);
  let [로고, setLogo] = useState("블로그임");
  let [따봉, 따봉변경] = useState(0);

  return (
    <div className="App">
      <div className="black-nav">
        <h4 style={{ color: "yellow", fontSize: "20px" }}>{로고}</h4>
      </div>

      <button
        onClick={() => {
          let copy = [...글제목];
          copy.sort();
          글내용수정(copy);
        }}
      >
        {" "}
        정렬버튼{" "}
      </button>

      <div className="list">
        <h4>
          {글제목[0]}{" "}
          <button
            onClick={() => {
              따봉변경(따봉 + 1);
            }}
          >
            {" "}
            👍
          </button>{" "}
          {따봉}
        </h4>
        <p>2월 17일 발행</p>
      </div>

      <div className="list">
        <h4>
          {글제목[1]}
          <button
            onClick={() => {
              let copy = [...글제목];
              copy[1] = "역삼 우동 맛집";
              글내용수정(copy);
            }}
          >
            {" "}
            글수정{" "}
          </button>
        </h4>
        <p>2월 17일 발행</p>
      </div>

      <div className="list">
        <h4>{글제목[2]}</h4>
        <p>2월 17일 발행</p>
      </div>
    </div>
  );
}

export default App;
