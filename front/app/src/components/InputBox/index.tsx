import { useState, useRef } from "react";
import { toPng } from "html-to-image";
import download from "downloadjs";
import s from "./index.module.css";

export default function Home() {
  const [profile, setProfile] = useState({
    name: "",
    office: "",
    grade: "",
  });
  const cardRef = useRef<HTMLDivElement | null>(null);

  const handleChange = (
    e: React.ChangeEvent<HTMLInputElement | HTMLSelectElement>
  ) => {
    const { name, value } = e.target;
    setProfile((prevProfile) => ({
      ...prevProfile,
      [name]: value,
    }));
  };

  const handleDownload = () => {
    if (cardRef.current === null) {
      return;
    }
    toPng(cardRef.current)
      .then((dataUrl: string) => {
        download(dataUrl, "profile-card.png");
      })
      .catch((err: Error) => {
        console.error("Oops, something went wrong!", err);
      });
  };

  // 背景色をofficeの値によって変更
  const getBackgroundColor = (office: string) => {
    switch (office) {
      case "企画局":
        return "blue";
      case "財務局":
        return "green";
      case "渉外局":
        return "red";
      case "情報局":
        return "purple";
      case "制作局":
        return "orange";
      case "総務局":
        return "yellow";
      default:
        return "gray"; // デフォルトの色
    }
  };

  return (
    <div className={s.container}>
      {/* プロフィールカード */}
      <div className={s.component}>
        <div
          ref={cardRef}
          style={{
            border: "1px solid black",
            padding: "10px",
            marginTop: "20px",
            backgroundColor: getBackgroundColor(profile.office),
            color: "white",
          }}
        >
          <h2>Profile Card</h2>
          <p> 名前：{profile.name}</p>
          <p> 所属局：{profile.office}</p>
          <p> 学年：{profile.grade}</p>
        </div>
      </div>
      <div className={s.component}>
        <form>
          <div className={s.inputForm}>
            <label>名前・ニックネーム(無い場合は省略)</label>
            <input
              type="text"
              name="name"
              value={profile.name}
              onChange={handleChange}
            />
          </div>
          <div className={s.inputForm}>
            <label>所属局</label>
            <select
              name="office"
              value={profile.office}
              onChange={handleChange}
            >
              <option value="">-------</option>
              <option value="企画局">企画局</option>
              <option value="財務局">財務局</option>
              <option value="渉外局">渉外局</option>
              <option value="情報局">情報局</option>
              <option value="制作局">制作局</option>
              <option value="総務局">総務局</option>
            </select>
          </div>
          <div className={s.inputForm}>
            <label>学年</label>
            <select
              name="grade"
              value={profile.grade}
              onChange={handleChange}
            >
              <option value="">-------</option>
              <option value="B1">B1</option>
              <option value="B2">B2</option>
              <option value="B3">B3</option>
              <option value="B4">B4</option>
              <option value="M1">M1</option>
              <option value="M2">M2</option>
            </select>
          </div>
        </form>
      </div>
      <div className={s.component}>
        <button onClick={handleDownload} style={{ marginTop: "20px" }}>
          生成する
        </button>
      </div>
    </div>
  );
}
