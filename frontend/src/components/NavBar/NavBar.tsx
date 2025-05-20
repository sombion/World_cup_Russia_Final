// components/Navbar/Navbar.tsx
import { observer } from "mobx-react-lite";
import { Link, useNavigate } from "react-router-dom";
import { authStore } from "../../stores/authStore";
import styles from "./NavBar.module.scss";

export const Navbar = observer(() => {
  const navigate = useNavigate();

  const handleLogout = () => {
    authStore.logout();
    navigate("/login"); 
  };
const GAME_BASE_URL = import.meta.env.VITE_GAME_BASE_URL || 'http://127.0.0.1:8000';

const launchGame2 = () => {
  window.open(`${GAME_BASE_URL}/games_2/`, '_blank');
};

  if (authStore.isLoading) return <div>Загрузка...</div>;

  return (
    <nav className={styles["navbar"]}>
      <div className={styles["navbar-left"]}>
        {authStore.isAdmin ? (
          <> 
            <Link to="/admin/lotteries/create">Создать лотерею</Link>
            <Link to="/lotteries">Все лотереи</Link>
          </>
        ) : (
          <>
            <Link to="/lotteries">Главная</Link>
            <Link to="/lotteries">Лотереи</Link>
          </>
        )}
      </div>

      {authStore.isAuthenticated ? (
        <div className={styles["navbar-right"]}>
          <span className={styles["user-info"]}>
            {authStore.user?.login}
            {authStore.isAdmin && " (Admin)"}
          </span>
          <button onClick={launchGame2} className={styles["logout-button"]}>
          Игра 2
        </button>
          {!authStore.isAdmin && (
            <span className={styles["user-money"]}>Баланс: {authStore.user?.money} ₽</span>
          )}
          <button onClick={handleLogout} className={styles["logout-button"]}>
            Выйти
          </button>
        </div>
      ) : (
        <Link to="/login" className={styles["logout-button"]}>
          Войти
        </Link>
      )}
    </nav>
  );
});