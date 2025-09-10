import React, { useState, useEffect } from "react";

function Practice() {
  const [dark, setDark] = useState(false);
  const [data, setData] = useState(null);

  const toggleTheme = () => setDark((prev) => !prev);

  useEffect(() => {
    // Example API: JSONPlaceholder
    fetch("https://jsonplaceholder.typicode.com/posts/1")
      .then((res) => res.json())
      .then((json) => setData(json))
      .catch((err) => setData({ error: "Failed to fetch data" }));
  }, []);

  return (
    <div
      style={{
        minHeight: "100vh",
        background: dark ? "#222" : "#fff",
        color: dark ? "#fff" : "#222",
        transition: "background 0.3s, color 0.3s",
        display: "flex",
        flexDirection: "column",
        alignItems: "center",
        justifyContent: "center"
      }}
    >
      <button onClick={toggleTheme} style={{ marginBottom: "2rem" }}>
        Switch to {dark ? "Light" : "Dark"} Theme
      </button>
      <h1>{dark ? "Dark" : "Light"} Theme Active</h1>
      <div style={{ marginTop: "2rem" }}>
        <h2>Fetched Data:</h2>
        {data ? (
          <pre style={{ textAlign: "left" }}>{JSON.stringify(data, null, 2)}</pre>
        ) : (
          <p>Loading...</p>
        )}
      </div>
    </div>
  );
}

export default Practice;