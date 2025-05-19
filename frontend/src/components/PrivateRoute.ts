// // components/PrivateRoute.tsx
// import { observer } from 'mobx-react-lite';
// import { Navigate, Outlet } from 'react-router-dom';
// import { authStore } from '../stores/authStore';

// interface PrivateRouteProps {
//   adminOnly?: boolean;
// }

// export const PrivateRoute = observer(({ adminOnly = false }: PrivateRouteProps) => {
//   if (!authStore.isAuthenticated) {
//     return <Navigate to="/login" replace />;
//   }

//   if (adminOnly && !authStore.isAdmin) {
//     return <Navigate to="/" replace />;
//   }

//   return <Outlet />;
// });