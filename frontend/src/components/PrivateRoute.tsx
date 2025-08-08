import React from 'react';
import { Navigate, useLocation } from 'react-router-dom';
import { getToken, isTokenValid } from '../components/utils/auth';

interface PrivateRouteProps {
  children: JSX.Element;
  requiredRole?: string;
}

const PrivateRoute: React.FC<PrivateRouteProps> = ({ children, requiredRole }) => {
  const token = getToken();
  const userRole = localStorage.getItem('role'); // Assumindo que o papel do utilizador está armazenado localmente
  const location = useLocation();

  if (!token || !isTokenValid(token)) {
    return <Navigate to="/login" state={{ from: location }} replace />;
  }

  if (requiredRole && userRole !== requiredRole) {
    return <Navigate to="/unauthorized" replace />;
  }

  return children;
};

export default PrivateRoute;