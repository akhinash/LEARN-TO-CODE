import React from 'react'
import Usetoggle from './Usetoggle'

const Sapp = () => {
    const[isVisible,togglevisiblity]=toggle()
  return (
    <div>
        <button onClick={togglevisiblity}>
            {isVisible?'Hide':'Show'}Text
        </button>
        {isVisible && <p>this is toggled text</p>}
      
    </div>
  )
}

export default Sapp
