import React, { useState, useEffect } from 'react'
import axios from 'axios'

const Delete = () => {
  const [product, setProduct] = useState([]) // should be array, not string

  useEffect(() => {
    axios.get("https://fakestoreapi.com/products")
      .then((response) => {
        setProduct(response.data)
      })
      .catch((error) => {
        console.error("fetching data error", error)
      })
  }, [])

  const handleDelete = (id) => {
    axios.delete(`https://fakestoreapi.com/products/${id}`) // fix: must include the id in URL
      .then(() => {
        setProduct(prev => prev.filter(p => p.id !== id))
      })
      .catch((error) => {
        console.error("error deleting product:", error)
      })
  }

  return (
    <div>
      <h2>PRODUCT LIST</h2>
      {product.map(p => (
        <div key={p.id} style={{ border: '1px solid #ccc', padding: '10px', margin: '10px 0' }}>
          <img src={p.image} alt={p.title} style={{ height: '100px' }} />
          <h4>{p.title}</h4>
          <p>Price: ${p.price}</p>
          <button onClick={() => handleDelete(p.id)}>Delete</button>
        </div>
      ))}
    </div>
  )
}

export default Delete
