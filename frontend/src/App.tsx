import { useEffect, useState } from 'react';

const API_URL = import.meta.env.VITE_API_URL as string;

function App() {
  const [message, setMessage] = useState("not received yet.");

  useEffect(() => {
    fetch(`${API_URL}/hello`)
      .then((res) => res.json())
      .then((data) => setMessage(data.message));
  }, []);


  return (
    <>
      <h1>Vite + React</h1>
      <div className="card">
        <p>Message: {message}</p>
        <p>
          Edit <code>src/App.tsx</code> and save to test HMR
        </p>
      </div>
      <p className="read-the-docs">
        Click on the Vite and React logos to learn more
      </p>
    </>
  )
}

export default App
