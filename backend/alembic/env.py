import React, { useEffect, useState } from 'react';

interface Workflow {
  id: number;
  name: string;
  description: string;
  is_active: boolean;
  created_at: string;
}

const ActiveWorkflows: React.FC = () => {
  const [workflows, setWorkflows] = useState<Workflow[]>([]);
  const [loading, setLoading] = useState<boolean>(true);
  const [error, setError] = useState<string | null>(null);

  useEffect(() => {
    const fetchWorkflows = async () => {
      try {
        // Substituir por chamada real à API futuramente
        const mockData: Workflow[] = [
          {
            id: 1,
            name: 'Customer Onboarding',
            description: 'Automate new customer onboarding process',
            is_active: true,
            created_at: '2024-05-01',
          },
          {
            id: 2,
            name: 'Weekly Report',
            description: 'Send weekly report emails to team',
            is_active: true,
            created_at: '2024-05-03',
          },
        ];
        setTimeout(() => {
          setWorkflows(mockData);
          setLoading(false);
        }, 1000);
      } catch (err) {
        setError('Failed to load workflows');
        setLoading(false);
      }
    };

    fetchWorkflows();
  }, []);

  if (loading) return <div className="p-6">Loading workflows...</div>;
  if (error) return <div className="p-6 text-red-600">{error}</div>;

  return (
    <div className="p-6">
      <h1 className="text-2xl font-bold mb-6">Active Workflows</h1>
      <div className="overflow-x-auto">
        <table className="min-w-full bg-white border border-gray-200 shadow">
          <thead className="bg-gray-100 text-left">
            <tr>
              <th className="p-3 border-b">Name</th>
              <th className="p-3 border-b">Description</th>
              <th className="p-3 border-b">Created At</th>
              <th className="p-3 border-b">Status</th>
            </tr>
          </thead>
          <tbody>
            {workflows.map((workflow) => (
              <tr key={workflow.id} className="hover:bg-gray-50">
                <td className="p-3 border-b">{workflow.name}</td>
                <td className="p-3 border-b">{workflow.description}</td>
                <td className="p-3 border-b">{workflow.created_at}</td>
                <td className="p-3 border-b">
                  {workflow.is_active ? (
                    <span className="text-green-600 font-semibold">Active</span>
                  ) : (
                    <span className="text-gray-500">Inactive</span>
                  )}
                </td>
              </tr>
            ))}
          </tbody>
        </table>
      </div>
    </div>
  );
};

export default ActiveWorkflows;