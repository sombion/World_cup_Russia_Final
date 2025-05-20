import { Navigate } from 'react-router-dom';
import { observer } from 'mobx-react-lite';
import { authStore } from '../stores/authStore';
import { type ReactNode } from 'react';

interface AdminRouteProps {
  children: ReactNode;
}

export const AdminRoute = observer(({ children }: AdminRouteProps) => {


  if (!authStore.isAuthenticated) {
    return Navigate({ to: '/login', replace: true });
  }
  if (!authStore.user?.is_admin) {
    return Navigate({ to: '/login', replace: true });
  }
  return children;
});