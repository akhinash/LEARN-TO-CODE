import React from 'react'

const List = () => {
    const numbers =[1,2,3,4,5,6]
    const listItems= numbers.map((number)=><li>{number}</li>)
  return (
    <div>
      {listItems}
    </div>
  )
}

export default List
