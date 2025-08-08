import React, { useEffect, useState } from 'react';
import axios from 'axios';

interface WorkflowStats {
  total: number;
  active: number;
  inactive: number;
  executionsToday: number;
}

const Dashboard: React.FC = () => {
  const [stats, setStats] = useState<WorkflowStats | null>(null);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState<string | null>(null);

  useEffect(() => {
    const fetchStats = async () => {
      try {
        // Simulando uma chamada de API
        const response = await axios.get('http://localhost:8000/dashboard/stats');
        setStats(response.data);
      } catch (err) {
        setError('Erro ao carregar estatísticas.');
      } finally {
        setLoading(false);
      }
    };

    fetchStats();
  }, []);

  return (
    <div className="p-6 max-w-6xl mx-auto">
      <h1 className="text-3xl font-bold mb-6">Dashboard</h1>

      {loading && <p>A carregar dados...</p>}
      {error && <p className="text-red-500">{error}</p>}

      {!loading && stats && (
        <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-6">
          <div className="bg-white p-4 rounded shadow">
            <h2 className="text-sm text-gray-500">Total de Workflows</h2>
            <p className="text-2xl font-bold">{stats.total}</p>
          </div>
          <div className="bg-white p-4 rounded shadow">
            <h2 className="text-sm text-gray-500">Ativos</h2>
            <p className="text-2xl font-bold text-green-600">{stats.active}</p>
          </div>
          <div className="bg-white p-4 rounded shadow">
            <h2 className="text-sm text-gray-500">Inativos</h2>
            <p className="text-2xl font-bold text-red-600">{stats.inactive}</p>
          </div>
          <div className="bg-white p-4 rounded shadow">
            <h2 className="text-sm text-gray-500">Execuções Hoje</h2>
            <p className="text-2xl font-bold">{stats.executionsToday}</p>
          </div>
        </div>
      )}

      {!loading && !stats && (
        <p className="mt-4 text-gray-500">Sem dados disponíveis no momento.</p>
      )}
    </div>
  );
};

export default Dashboard;