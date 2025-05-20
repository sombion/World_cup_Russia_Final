// components/Navbar/Navbar.tsx
import { observer } from "mobx-react-lite";
import { Link, useNavigate } from "react-router-dom";
import { authStore } from "../../stores/authStore";
import "./NavBar.module.scss";

export const Navbar = observer(() => {
  const navigate = useNavigate();

  const handleLogout = () => {
    authStore.logout();
    navigate("/login"); 
  };

   const launchGame2 = () => {
    window.open(`http://127.0.0.1:8000/games_2/`, '_blank');
  };

  if (authStore.isLoading) return <div>Загрузка...</div>;

  return (
    <nav className="navbar">
      <div className="navbar-left">
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
        <div className="navbar-right">
          <span className="user-info">
            {authStore.user?.login}
            {authStore.isAdmin && " (Admin)"}
          </span>
          <button onClick={launchGame2} className="game-button">
          Игра 2
        </button>
          {!authStore.isAdmin && (
            <span className="user-money">Баланс: {authStore.user?.money} ₽</span>
          )}
          <button onClick={handleLogout} className="logout-button">
            Выйти
          </button>
        </div>
      ) : (
        <Link to="/login" className="login-button">
          Войти
        </Link>
      )}
    </nav>
  );
});