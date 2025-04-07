import React from 'react';

function Teams() {
  const teams = [
    { id: 1, name: 'Blue Team', members: 5 },
    { id: 2, name: 'Gold Team', members: 4 },
    { id: 3, name: 'Red Team', members: 6 },
  ];

  return (
    <div>
      <h1 className="text-center my-4">Teams</h1>
      <table className="table table-striped">
        <thead className="table-dark">
          <tr>
            <th>ID</th>
            <th>Name</th>
            <th>Members</th>
          </tr>
        </thead>
        <tbody>
          {teams.map(team => (
            <tr key={team.id}>
              <td>{team.id}</td>
              <td>{team.name}</td>
              <td>{team.members}</td>
            </tr>
          ))}
        </tbody>
      </table>
      <button className="btn btn-primary mt-3">Add Team</button>
    </div>
  );
}

export default Teams;
