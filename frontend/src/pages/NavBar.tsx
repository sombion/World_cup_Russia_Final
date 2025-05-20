import { Link } from 'react-router-dom';
import styles from '../styles/NavBar.module.scss';

export const NavBar = () => {
  return (
    <header className={styles["navbar"]}>
      <div className={styles["logo"]}>
        <Link to="/">Фил Гуд Инк</Link>
      </div>

      <nav className={styles["menu"]}>
        <Link to="/">Главная</Link>
        <Link to="/about">О нас</Link>
        <Link to="/services">Услуги</Link>
        <Link to="/contact">Контакты</Link>
      </nav>

      <div className={styles["auth"]}>
        <Link to="/login" className={styles["button"]}>Вход</Link>
        <Link to="/register" className={styles["button"]}>Регистрация</Link>
      </div>
    </header>
  );
};
