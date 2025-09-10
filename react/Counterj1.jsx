import React, { useState } from "react";

function CounterJ1() {
  const [count, setCount] = useState(0);

  return (
    <div style={{ margin: "1rem" }}>
      <h2>Counter: {count}</h2>
      <button onClick={() => setCount(count + 1)}>Increment</button>
      <button onClick={() => setCount(count - 1)} style={{ marginLeft: "0.5rem" }}>
        Decrement
      </button>
    </div>
  );
}

export default CounterJ1;