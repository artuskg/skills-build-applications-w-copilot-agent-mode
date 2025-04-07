import React from 'react';

function Activities() {
  const activities = [
    { id: 1, name: 'Cycling', duration: '1 hour' },
    { id: 2, name: 'Running', duration: '30 minutes' },
    { id: 3, name: 'Swimming', duration: '45 minutes' },
  ];

  return (
    <div>
      <h1 className="text-center my-4">Activities</h1>
      <table className="table table-striped">
        <thead className="table-dark">
          <tr>
            <th>ID</th>
            <th>Name</th>
            <th>Duration</th>
          </tr>
        </thead>
        <tbody>
          {activities.map(activity => (
            <tr key={activity.id}>
              <td>{activity.id}</td>
              <td>{activity.name}</td>
              <td>{activity.duration}</td>
            </tr>
          ))}
        </tbody>
      </table>
      <button className="btn btn-primary mt-3">Add Activity</button>
    </div>
  );
}

export default Activities;
