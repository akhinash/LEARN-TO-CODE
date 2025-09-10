import React, { useEffect, useState } from 'react'
import axios from 'axios'

const NewCompnent = () => {
    const [product,setProduct]=useState([])

    useEffect(()=>{
        axios.get("https://fakestoreapi.com/products")
        .then((response)=>{
            setProduct(response.data)
        })
        .catch((error)=>{
            console.error("fetching data error",error)
        })
    },[])
  return (
    <div>
        <h2>PRODUCT LIST</h2>
        {product.map(p=>(
            <div key={p.id}>
                <h4>{p.title}</h4>
                <img src={p.image} alt={p.title} style={{ height: '150px' }} />
                <p>{p.price}</p>
            </div>
        ))}
      
    </div>
  )
}

export default NewCompnent
