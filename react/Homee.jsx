// import React, { useContext } from "react";
// import Themecontext from "./Themecontext"; // match default export

// const Homee = () => {
//   const { darkMode, toggleTheme } = useContext(Themecontext); // match context name

//   const themeStyle = {
//     backgroundColor: darkMode ? "#333" : "#fff",
//     color: darkMode ? "#fff" : "#000",
//     minHeight: "100vh",
//     display: "flex",
//     flexDirection: "column",
//     alignItems: "center",
//     justifyContent: "center",
//   };

//   return (
//     <div style={themeStyle}>
//       <h1>{darkMode ? "Dark Mode" : "Light Mode"}</h1>
//       <button onClick={toggleTheme}>Toggle Theme</button>
//     </div>
//   );
// };

// export default Homee;


import React, { useContext } from "react";
import { ThemeContext } from "./ThemeContext";

const Homee = () => {
  const { darkMode, toggleTheme } = useContext(ThemeContext);

  const themeStyle = {
    backgroundColor: darkMode ? "" : "#fff",
    color: darkMode ? "#fff" : "#000",
    minHeight: "100vh",
    display: "flex",
    flexDirection: "column",
    alignItems: "center",
    justifyContent: "center",
  };

  return (
    <div style={themeStyle}>
      <h1>{darkMode ? "Dark Mode" : "Light Mode"}</h1>
      <button onClick={toggleTheme}>
        Toggle Theme
      </button>
    </div>
  );
};

export default Homee;