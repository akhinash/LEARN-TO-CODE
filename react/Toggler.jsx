import React, { useState } from 'react'

const Toggler = (initialValue) => {
    const[darkMode, setDarkMode]=useState(false)

    const toggle = () => setDarkMode(prevvalue =>!prevvalue)

    [value,toggle]

    
  return (
    <div>

        
        <button value={setDarkMode}>
            
        </button>
      
    </div>
  )
}

export default Toggler




