import React, { useEffect, useState } from 'react';
import axios from 'axios';

interface Task {
  id: number;
  title: string;
  description: string;
  status: 'pending' | 'in_progress' | 'completed';
  created_at: string;
}

const MyTasks: React.FC = () => {
  const [tasks, setTasks] = useState<Task[]>([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState<string | null>(null);

  useEffect(() => {
    const fetchTasks = async () => {
      try {
        const token = localStorage.getItem('token');
        const response = await axios.get('http://localhost:8000/my-tasks', {
          headers: {
            Authorization: `Bearer ${token}`,
          },
        });
        setTasks(response.data);
      } catch (err) {
        setError('Erro ao carregar as tarefas.');
      } finally {
        setLoading(false);
      }
    };

    fetchTasks();
  }, []);

  return (
    <div className="p-6">
      <div className="flex justify-between items-center mb-4">
        <h1 className="text-2xl font-bold">Minhas Tarefas</h1>
        <div className="flex gap-4">
          <button
            onClick={() => window.location.href = '/create-task'}
            className="bg-blue-600 text-white px-4 py-2 rounded hover:bg-blue-700 transition"
          >
            + Nova Tarefa
          </button>
          <button
            onClick={() => {
              localStorage.removeItem('token');
              window.location.href = '/login';
            }}
            className="bg-red-500 text-white px-4 py-2 rounded hover:bg-red-600 transition"
          >
            Terminar Sessão
          </button>
        </div>
      </div>

      {loading && <p>A carregar tarefas...</p>}
      {error && <p className="text-red-600">{error}</p>}
      {!loading && tasks.length === 0 && <p>Não existem tarefas atribuídas.</p>}

      <ul className="space-y-4">
        {tasks.map((task) => (
          <li
            key={task.id}
            className="border p-4 rounded shadow-sm bg-white"
          >
            <h2 className="text-xl font-semibold">{task.title}</h2>
            <p className="text-sm text-gray-600">{task.description}</p>
            <div className="mt-2 text-xs text-gray-500 flex items-center gap-2">
              <span
                className={`inline-block w-3 h-3 rounded-full ${
                  task.status === 'pending'
                    ? 'bg-yellow-400'
                    : task.status === 'in_progress'
                    ? 'bg-blue-400'
                    : 'bg-green-500'
                }`}
              />
              <span>Estado: <strong>{task.status}</strong></span>
            </div>
            <p className="text-xs text-gray-400">Criado em: {new Date(task.created_at).toLocaleString()}</p>
          </li>
        ))}
      </ul>
    </div>
  );
};

export default MyTasks;