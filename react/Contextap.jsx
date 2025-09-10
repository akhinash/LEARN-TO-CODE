import React, { createContext } from 'react'
import Child from './child';

export const MyContext = createContext();

function Contextap(){
  return (
    <div>
        <MyContext.Provider value="Hello,React">

            <Child/>
        </MyContext.Provider>
      
    </div>
  )
}

export default Contextap

