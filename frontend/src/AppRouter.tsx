import { Routes, Route } from 'react-router-dom';
import { LoginPage } from './pages/LoginPage';
import { RegisterPage } from './pages/RegisterPage';
import { CreateLotteryPage } from './pages/admin/CreateLotteryPage';
//import { PrivateRoute } from './components/PrivateRoute';
// import { HomePage } from './pages/HomePage';
// import { AdminPage } from './pages/AdminPage';

export const AppRouter = () => {
  return (
    <Routes>
      <Route path="/login" element={<LoginPage />} />
      <Route path="*" element={<LoginPage />} />

      <Route path="/register" element={<RegisterPage />} />
      <Route path="/admin/lotteries/create" element={<CreateLotteryPage />} />
      
      {/* <Route element={<PrivateRoute />}>
        <Route path="/" element={<HomePage />} />
      </Route>

      <Route element={<PrivateRoute adminOnly />}>
        <Route path="/admin" element={<AdminPage />} />
      </Route> */}
    </Routes>
  );
};