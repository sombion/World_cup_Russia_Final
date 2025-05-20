import { Routes, Route } from 'react-router-dom'
import { LoginPage } from './pages/LoginPage'
import { RegisterPage } from './pages/RegisterPage'
import { CreateLotteryPage } from './pages/admin/CreateLotteryPage'
import { LotteryDetailsPage } from './pages/LotteryDetailPage'
import PublicLotteryPage from './pages/PublicLotteryPage'
// import { PrivateRoute } from './components/PrivateRoute'
// import { AdminRoute } from './components/AdminRoute'
//import type { ReactNode } from 'react'
import { Navbar } from './components/NavBar/NavBar'
//import { WithoutNavbar } from './layouts/WithoutNavBar'

export const AppRouter = () => {
  
// const LayoutWithNavbar = ({ children }: { children: ReactNode }) => {
//   return (
//     <>
//       <Navbar />
//       {children}
//     </>
//   );
// };

  return (
    <>
      <Navbar/>
      <Routes>
        {/* Публичные маршруты */}
        <Route path="/login" element={<LoginPage />} />
        <Route path="/register" element={<RegisterPage />} />

          <Route path="/lotteries" element={
              <PublicLotteryPage />
          } />

        <Route path="/lotteries/:id" element={
            <LotteryDetailsPage />
        } />
        
        {/* Админские маршруты */}
         <Route path="/lotteries" element={
            <PublicLotteryPage />
        } />

        
         <Route path="/admin/lotteries/create" element={
            <CreateLotteryPage />
        }/>

        {/* Fallback */}
        <Route path="*" element={<LoginPage />} />
      </Routes>
    </>
  )
}
// const LayoutWithNavbar = () => {
//   return (
//     <>
//       <Navbar />
//     </>
//   );
// };