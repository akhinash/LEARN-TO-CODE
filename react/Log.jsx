import React, { useState } from 'react'
import { Authcontext } from './Authcontext';
import Home from './Home';

const Log = () => {
    const[login,setLogin]=useState(false);
  return (
    <div>
        <Authcontext.Provider value={{login,setLogin}}>
            <Home/>
        </Authcontext.Provider>
      
    </div>
  )
}

export default Log
