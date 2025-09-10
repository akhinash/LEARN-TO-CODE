// import React, { createContext, useState } from 'react';

// export const Themecontext = createContext();

// export const ThemeProvider = ({ children }) => {
//   const [darkMode, setDarkmode] = useState(false);

//   const toggleTheme = () => {
//     setDarkmode(prev => !prev);
//   };

//   return (
//     <Themecontext.Provider value={{ darkMode, toggleTheme }}>
//       {children}
//     </Themecontext.Provider>
//   );
// };

// export default Themecontext;


import { createContext, useState } from "react";

export const ThemeContext = createContext();

export const ThemeProvider = ({ children }) => {
  const [darkMode, setDarkMode] = useState(false);

  const toggleTheme = () => {
    setDarkMode(prevs => !prevs);
  };

  return (
    <ThemeContext.Provider value={{ darkMode, toggleTheme }}>
      {children}
    </ThemeContext.Provider>
  );
};