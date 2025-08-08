import React, { useState } from 'react';
import axios from 'axios';

// Tipo para os dados do formulário
interface WorkflowData {
  name: string;
  trigger: string;
  action: string;
  condition: string;
}

const CreateWorkflow: React.FC = () => {
  // Estado do formulário
  const [formData, setFormData] = useState<WorkflowData>({
    name: '',
    trigger: '',
    action: '',
    condition: '',
  });

  // Estado para feedback ao utilizador
  const [success, setSuccess] = useState<string | null>(null);
  const [error, setError] = useState<string | null>(null);
  const [loading, setLoading] = useState<boolean>(false);

  // Atualização dos campos do formulário
  const handleChange = (e: React.ChangeEvent<HTMLInputElement | HTMLSelectElement>) => {
    setFormData({ ...formData, [e.target.name]: e.target.value });
  };

  // Submissão do formulário
  const handleSubmit = async (e: React.FormEvent) => {
    e.preventDefault();
    setSuccess(null);
    setError(null);
    setLoading(true);

    try {
      // Envio para o endpoint do backend
      await axios.post('http://localhost:8000/workflows', formData);
      setSuccess('Workflow criado com sucesso!');
      setFormData({
        name: '',
        trigger: '',
        action: '',
        condition: '',
      });
    } catch (err) {
      setError('Erro ao criar workflow. Verifique os dados e tente novamente.');
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="max-w-lg mx-auto p-6 bg-white rounded shadow">
      <h1 className="text-2xl font-semibold mb-4">Criar Novo Workflow</h1>

      <form onSubmit={handleSubmit} className="space-y-4">
        {/* Campo: Nome */}
        <div>
          <label className="block text-sm font-medium mb-1">Nome do Workflow</label>
          <input
            type="text"
            name="name"
            value={formData.name}
            onChange={handleChange}
            className="w-full border rounded px-3 py-2"
            required
            placeholder="Ex: Atualizar CRM"
          />
        </div>

        {/* Campo: Trigger */}
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
            <option value="on_create">Ao criar registo</option>
            <option value="on_update">Ao atualizar registo</option>
            <option value="on_schedule">Agendado</option>
          </select>
        </div>

        {/* Campo: Ação */}
        <div>
          <label className="block text-sm font-medium mb-1">Ação</label>
          <input
            type="text"
            name="action"
            value={formData.action}
            onChange={handleChange}
            className="w-full border rounded px-3 py-2"
            required
            placeholder="Ex: Enviar e-mail"
          />
        </div>

        {/* Campo: Condição */}
        <div>
          <label className="block text-sm font-medium mb-1">Condição (opcional)</label>
          <input
            type="text"
            name="condition"
            value={formData.condition}
            onChange={handleChange}
            className="w-full border rounded px-3 py-2"
            placeholder="Ex: Se status = 'pendente'"
          />
        </div>

        {/* Botão de submissão */}
        <button
          type="submit"
          disabled={loading}
          className={`bg-blue-600 text-white px-4 py-2 rounded hover:bg-blue-700 ${loading ? 'opacity-50 cursor-not-allowed' : ''}`}
        >
          {loading ? 'A criar...' : 'Criar Workflow'}
        </button>
      </form>

      {/* Mensagens de sucesso ou erro */}
      {success && <p className="mt-4 text-green-600">{success}</p>}
      {error && <p className="mt-4 text-red-600">{error}</p>}
    </div>
  );
};

export default CreateWorkflow;