import React, { useEffect, useState } from 'react';
import axios from 'axios';

const FlightStatus = () => {
  const [flights, setFlights] = useState([]);

  useEffect(() => {
    fetchFlightData();
  }, []);

  const fetchFlightData = async () => {
    try {
      const response = await axios.get('/api/flights');
      setFlights(response.data);
    } catch (error) {
      console.error('Error fetching flight data:', error);
    }
  };

  return (
    <div>
      <h1>Flight Status</h1>
      <table>
        <thead>
          <tr>
            <th>Flight Number</th>
            <th>Status</th>
            <th>Gate</th>
            <th>Time</th>
          </tr>
        </thead>
        <tbody>
          {flights.map(flight => (
            <tr key={flight.id}>
              <td>{flight.number}</td>
              <td>{flight.status}</td>
              <td>{flight.gate}</td>
              <td>{flight.time}</td>
            </tr>
          ))}
        </tbody>
      </table>
    </div>
  );
};

export default FlightStatus;
