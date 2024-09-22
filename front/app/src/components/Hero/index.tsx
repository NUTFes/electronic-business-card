import { useState, useRef } from "react";
import s from "./index.module.css";

export default function Home() {
  return (
    <div className={s.container}>
      <div className={s.title}>
        <h1>自己紹介</h1>
        <h1>NUTFES</h1>
        <h1>カードジェネレータ</h1>
      </div>
    </div>
  );
}
