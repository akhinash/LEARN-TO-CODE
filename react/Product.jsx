import axios from 'axios';
import React, { useEffect, useState } from 'react'

function Product() {
  const[products,setProducts]= useState([]);

  useEffect(()=>{
    axios.get("https://fakestoreapi.com/products")
    .then((response)=>{
      setProducts(response.data)
    })
    .catch((error)=>{
      console.log("error ",error)
    })
  },[])
  return (
    <div>

      <h2>PRODUCT</h2>
      {products.map(p=>(
        <div key={p.id}>
          <h2>{p.title}</h2>
          <img src={p.image} alt={p.title} />

          <p>{p.price}</p>
        </div>
      )

      )}
      
        
        
    </div>
  )
}

export default Product
