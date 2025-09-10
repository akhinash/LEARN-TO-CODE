import React from "react";

function ThemeToggle({ theme, toggleTheme }) {
  return (
    <button onClick={toggleTheme} style={{ margin: "1rem" }}>
      Switch to {theme === "light" ? "Dark" : "Light"} Theme
    </button>
  );
}

export default ThemeToggle;