import React, { useState } from 'react'

const Numbers = () => {
  const [num, setNum] = useState([])
  const [nextnum, setNextnum] = useState(1)

  const handleAdd = () => {
    const newNum = String(nextnum).repeat(nextnum);
    setNum([...num,newNum])
    setNextnum(nextnum + 1)
  }

  const handleSub = () => {
    if (num.length > 1) {
      setNum(num.slice(0, -1))  
      setNextnum(nextnum - 1)   
    }
  }

  return (
    <div>
      <h1>COUNTER</h1>
      <p>{num.join()}</p>
      <button onClick={handleAdd}>+</button>
      <button onClick={handleSub}>-</button>
    </div>
  )
}

export default Numbers
