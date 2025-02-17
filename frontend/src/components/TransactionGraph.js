import React from 'react';
import { Line } from 'react-chartjs-2';

const TransactionGraph = ({ transactions }) => {
  const data = {
    labels: transactions.map((t) => t.date),
    datasets: [
      {
        label: 'Transaction Amounts',
        data: transactions.map((t) => t.amount),
        fill: false,
        backgroundColor: 'rgba(75,192,192,0.6)',
        borderColor: 'rgba(75,192,192,1)',
      },
    ],
  };

  return (
    <div>
      <h2>Transaction Graph</h2>
      <Line data={data} />
    </div>
  );
};

export default TransactionGraph;
