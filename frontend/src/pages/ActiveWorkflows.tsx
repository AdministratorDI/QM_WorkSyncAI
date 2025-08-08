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
        setLoading(true);
        setError(null);

        // Simulated API call
        const response = await new Promise<Workflow[]>((resolve) =>
          setTimeout(() => {
            resolve([
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
            ]);
          }, 1000)
        );

        setWorkflows(response);
      } catch (err) {
        setError('Failed to load workflows.');
      } finally {
        setLoading(false);
      }
    };

    fetchWorkflows();
  }, []);

  return (
    <div className="p-6">
      <h1 className="text-2xl font-semibold mb-4">Active Workflows</h1>

      {loading ? (
        <p className="text-gray-600">Loading workflows...</p>
      ) : error ? (
        <p className="text-red-600">{error}</p>
      ) : workflows.length === 0 ? (
        <p className="text-gray-600">No active workflows found.</p>
      ) : (
        <table className="w-full border border-gray-300">
          <thead>
            <tr className="bg-gray-100 text-left">
              <th className="p-2 border-b">Name</th>
              <th className="p-2 border-b">Description</th>
              <th className="p-2 border-b">Created At</th>
              <th className="p-2 border-b">Status</th>
            </tr>
          </thead>
          <tbody>
            {workflows.map((workflow) => (
              <tr key={workflow.id} className="hover:bg-gray-50">
                <td className="p-2 border-b">{workflow.name}</td>
                <td className="p-2 border-b">{workflow.description}</td>
                <td className="p-2 border-b">{workflow.created_at}</td>
                <td className="p-2 border-b">
                  {workflow.is_active ? (
                    <span className="text-green-600 font-semibold">Active</span>
                  ) : (
                    <span className="text-red-600 font-semibold">Inactive</span>
                  )}
                </td>
              </tr>
            ))}
          </tbody>
        </table>
      )}
    </div>
  );
};

export default ActiveWorkflows;