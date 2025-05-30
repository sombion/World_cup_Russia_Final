import { Navigate } from 'react-router-dom';
import { observer } from 'mobx-react-lite';
import { authStore } from '../stores/authStore';
import type { ReactElement } from 'react';

interface PrivateRouteProps {
  children: ReactElement;
}

export const PrivateRoute = observer(({ children }: PrivateRouteProps) => {
  if (!authStore.isAuthenticated) {
    return Navigate({ to: '/login', replace: true });
  }
  return children;
});