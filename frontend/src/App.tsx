import { Routes, Route, Navigate } from 'react-router-dom';
import Login from './pages/Login';
import Dashboard from './pages/Dashboard';
import Calendar from './pages/Calendar';
import CreateWorkflow from './pages/CreateWorkflow';
import ActiveWorkflows from './pages/ActiveWorkflows';
import EditWorkflow from './pages/EditWorkflow';
import MyTasks from './pages/MyTasks';
import CreateTask from './pages/CreateTasks';
import PrivateRoute from './components/PrivateRoute';
import NotFound from './pages/NotFound';
import Unauthorized from './pages/Unauthorized';

function App() {
  // Exemplo simples de fallback de carregamento (pode ser expandido para Suspense etc.)
  // Aqui não há carregamento dinâmico, mas pode servir de base para melhorias futuras.
  // O wrapper div ajuda a manter a consistência visual e facilita debug.
  return (
    <div className="app-wrapper">
      <Routes>
        <Route path="/" element={<Navigate to="/login" replace />} />
        <Route path="/login" element={<Login />} />
        <Route
          path="/dashboard"
          element={
            <PrivateRoute requiredRole="user">
              <Dashboard />
            </PrivateRoute>
          }
        />
        <Route
          path="/calendar"
          element={
            <PrivateRoute requiredRole="user">
              <Calendar />
            </PrivateRoute>
          }
        />
        <Route
          path="/create"
          element={
            <PrivateRoute requiredRole="user">
              <CreateWorkflow />
            </PrivateRoute>
          }
        />
        <Route
          path="/active"
          element={
            <PrivateRoute requiredRole="user">
              <ActiveWorkflows />
            </PrivateRoute>
          }
        />
        <Route
          path="/edit"
          element={
            <PrivateRoute requiredRole="user">
              <EditWorkflow />
            </PrivateRoute>
          }
        />
        <Route
          path="/tasks"
          element={
            <PrivateRoute requiredRole="user">
              <MyTasks />
            </PrivateRoute>
          }
        />
        <Route
          path="/create-task"
          element={
            <PrivateRoute requiredRole="user">
              <CreateTask />
            </PrivateRoute>
          }
        />
        <Route path="/unauthorized" element={<Unauthorized />} />
        <Route path="*" element={<NotFound />} />
      </Routes>
    </div>
  );
}

export default App;