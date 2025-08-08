import React, { useEffect, useState } from 'react';
import { useParams, useNavigate } from 'react-router-dom';
import axios from 'axios';

interface WorkflowData {
  name: string;
  trigger: string;
  action: string;
  condition: string;
}

const EditWorkflow: React.FC = () => {
  const { id } = useParams<{ id: string }>();
  const navigate = useNavigate();
  const [formData, setFormData] = useState<WorkflowData>({
    name: '',
    trigger: '',
    action: '',
    condition: '',
  });
  const [loading, setLoading] = useState(true);
  const [success, setSuccess] = useState<string | null>(null);
  const [error, setError] = useState<string | null>(null);

  useEffect(() => {
    const fetchWorkflow = async () => {
      try {
        const response = await axios.get(`http://localhost:8000/workflows/${id}`);
        setFormData(response.data);
      } catch (err) {
        setError('Erro ao carregar workflow.');
      } finally {
        setLoading(false);
      }
    };

    fetchWorkflow();
  }, [id]);

  const handleChange = (e: React.ChangeEvent<HTMLInputElement | HTMLSelectElement>) => {
    setFormData({ ...formData, [e.target.name]: e.target.value });
  };

  const handleSubmit = async (e: React.FormEvent) => {
    e.preventDefault();
    setError(null);
    setSuccess(null);

    try {
      await axios.put(`http://localhost:8000/workflows/${id}`, formData);
      setSuccess('Workflow atualizado com sucesso!');
      setTimeout(() => navigate('/workflows'), 1500);
    } catch (err) {
      setError('Erro ao atualizar workflow.');
    }
  };

  return (
    <div className="max-w-lg mx-auto p-6 bg-white shadow rounded">
      <h1 className="text-2xl font-bold mb-4">Editar Workflow</h1>

      {loading ? (
        <p>A carregar...</p>
      ) : (
        <form onSubmit={handleSubmit} className="space-y-4">
          <div>
            <label className="block text-sm font-medium mb-1">Nome</label>
            <input
              type="text"
              name="name"
              value={formData.name}
              onChange={handleChange}
              className="w-full border rounded px-3 py-2"
              required
            />
          </div>

          <div>
            <label className="block text-sm font-medium mb-1">Trigger</label>
            <select
              name="trigger"
              value={formData.trigger}
              onChange={handleChange}
              className="w-full border rounded px-3 py-2"
              required
            >
              <option value="">Seleciona um trigger</option>
              <option value="on_create">Ao criar</option>
              <option value="on_update">Ao atualizar</option>
              <option value="on_schedule">Agendado</option>
            </select>
          </div>

          <div>
            <label className="block text-sm font-medium mb-1">Ação</label>
            <input
              type="text"
              name="action"
              value={formData.action}
              onChange={handleChange}
              className="w-full border rounded px-3 py-2"
              required
            />
          </div>

          <div>
            <label className="block text-sm font-medium mb-1">Condição</label>
            <input
              type="text"
              name="condition"
              value={formData.condition}
              onChange={handleChange}
              className="w-full border rounded px-3 py-2"
            />
          </div>

          <button
            type="submit"
            className="bg-blue-600 text-white px-4 py-2 rounded hover:bg-blue-700"
          >
            Guardar Alterações
          </button>
        </form>
      )}

      {success && <p className="mt-4 text-green-600">{success}</p>}
      {error && <p className="mt-4 text-red-600">{error}</p>}
    </div>
  );
};

export default EditWorkflow;