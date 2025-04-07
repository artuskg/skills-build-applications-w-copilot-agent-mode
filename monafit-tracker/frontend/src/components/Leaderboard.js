import React from 'react';

function Leaderboard() {
  const leaderboard = [
    { id: 1, username: 'thundergod', score: 100 },
    { id: 2, username: 'metalgeek', score: 90 },
    { id: 3, username: 'zerocool', score: 95 },
  ];

  return (
    <div>
      <h1 className="text-center my-4">Leaderboard</h1>
      <table className="table table-striped">
        <thead className="table-dark">
          <tr>
            <th>ID</th>
            <th>Username</th>
            <th>Score</th>
          </tr>
        </thead>
        <tbody>
          {leaderboard.map(entry => (
            <tr key={entry.id}>
              <td>{entry.id}</td>
              <td>{entry.username}</td>
              <td>{entry.score}</td>
            </tr>
          ))}
        </tbody>
      </table>
      <button className="btn btn-primary mt-3">View Full Leaderboard</button>
    </div>
  );
}

export default Leaderboard;
