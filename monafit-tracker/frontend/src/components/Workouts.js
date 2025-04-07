import React from 'react';

function Workouts() {
  const workouts = [
    { id: 1, name: 'Cycling Training', description: 'Training for a road cycling event' },
    { id: 2, name: 'Crossfit', description: 'Training for a crossfit competition' },
    { id: 3, name: 'Running Training', description: 'Training for a marathon' },
  ];

  return (
    <div>
      <h1 className="text-center my-4">Workouts</h1>
      <table className="table table-striped">
        <thead className="table-dark">
          <tr>
            <th>ID</th>
            <th>Name</th>
            <th>Description</th>
          </tr>
        </thead>
        <tbody>
          {workouts.map(workout => (
            <tr key={workout.id}>
              <td>{workout.id}</td>
              <td>{workout.name}</td>
              <td>{workout.description}</td>
            </tr>
          ))}
        </tbody>
      </table>
      <button className="btn btn-primary mt-3">Add Workout</button>
    </div>
  );
}

export default Workouts;
