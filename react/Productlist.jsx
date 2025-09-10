import React, { useEffect, useState } from 'react'


const Productlist = () => {
    const[poducts,setProducts]=useState([])
    const[newProduct,setNewproduct]=useState({
        title:'',
        price:'',
    })

    useEffect(()=>{
        axios.get("https://fakestoreapi.com/products")
        .then((response)=>{
            setProducts(response.data)
        })
        .catch((error );
        ))
    })
  return (
    <div>
      
    </div>
  )
}

export default Productlist
