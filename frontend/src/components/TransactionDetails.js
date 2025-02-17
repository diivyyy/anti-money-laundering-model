import React from 'react';

const TransactionDetails = ({ transactions }) => {
  return (
    <div>
      <h2>Transaction Details</h2>
      <table>
        <thead>
          <tr>
            <th>ID</th>
            <th>Amount</th>
            <th>Sender_account</th>
            <th>Receiver_account</th>
            <th>Ddte</th>
          </tr>
        </thead>
        <tbody>
          {transactions.map((transaction, index) => (
            <tr key={index}>
              <td>{transaction.id}</td>
              <td>{transaction.amount}</td>
              <td>{transaction.sender_account}</td>
              <td>{transaction.receiver_account}</td>
              <td>{transaction.date}</td>
            </tr>
          ))}
        </tbody>
      </table>
    </div>
  );
};

export default TransactionDetails;
