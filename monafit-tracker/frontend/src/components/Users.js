import React from 'react';

function Users() {
  const users = [
    { id: 1, username: 'thundergod', email: 'thundergod@mhigh.edu' },
    { id: 2, username: 'metalgeek', email: 'metalgeek@mhigh.edu' },
    { id: 3, username: 'zerocool', email: 'zerocool@mhigh.edu' },
  ];

  return (
    <div>
      <h1 className="text-center my-4">Users</h1>
      <table className="table table-striped">
        <thead className="table-dark">
          <tr>
            <th>ID</th>
            <th>Username</th>
            <th>Email</th>
          </tr>
        </thead>
        <tbody>
          {users.map(user => (
            <tr key={user.id}>
              <td>{user.id}</td>
              <td>{user.username}</td>
              <td>{user.email}</td>
            </tr>
          ))}
        </tbody>
      </table>
      <button className="btn btn-primary mt-3">Add User</button>
    </div>
  );
}

export default Users;
