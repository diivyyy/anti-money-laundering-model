import React from 'react';
import Dashboard from './components/Dashboard';
import TransactionDetails from './components/TransactionDetails';
import TransactionGraph from './components/TransactionGraph';

function App() {
  return (
    <div>
      <Dashboard />
      <TransactionDetails />
      <TransactionGraph />
    </div>
  );
}

export default App;
