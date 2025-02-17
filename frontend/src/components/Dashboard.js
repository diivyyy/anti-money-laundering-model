import React, { useEffect, useState } from 'react';
import TransactionGraph from './TransactionGraph';
import TransactionDetails from './TransactionDetails';

const Dashboard = () => {
  const [transactions, setTransactions] = useState([]);

  useEffect(() => {
    fetch('/transactions')
      .then(response => response.json())
      .then(data => setTransactions(data));
  }, []);

  return (
    <div>
      <h1>AML Dashboard</h1>
      <TransactionGraph transactions={transactions} />
      <TransactionDetails transactions={transactions} />
    </div>
  );
};

export default Dashboard;
