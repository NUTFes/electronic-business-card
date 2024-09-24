// import { useState, useEffect } from "react";
import s from "./index.module.css";
import InputBox from "@/components/InputBox/index";
import Hero from "@/components/Hero/index";

// interface Product {
//   id: number;
//   name: string;
//   price: string;
//   description: string;
// }

export default function Home() {
  // const [products, setProducts] = useState<Product[]>([]);

  // useEffect(() => {
  //   fetch("http://localhost:13000/api/products/")
  //     .then((response) => response.json())
  //     .then((data) => setProducts(data));
  // }, []);

  return (
    <section className={s.container}>
      <div className={s.component}>
        <Hero />
      </div>
      <div className={s.component}>
        <InputBox />
      </div>
    </section>
  );
}
