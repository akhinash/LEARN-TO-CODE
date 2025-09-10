import React from 'react'
import Product from './Product'
import Home from './Home'
import NewComponent from './NewCompnent'
import Delete from './Delete'
import Numbers from './Numbers'
import Toggler from './Toggler'
import User from './user'
import Contextap from './Contextap'
import Contextap2 from './Contextap2'
import CounterJ1 from './counterj1'
import Counterpra from './Counterpra'
import Practice from './Practice'
import Login from './Login'
import Dashboard from './Dashboard'
import { BrowserRouter, Routes, Route } from 'react-router-dom'





function App() {
  return (
    <div>
      {/* <Practice/> */}

     <BrowserRouter>
      <Routes>
        <Route path="/" element={<Login />} />
        <Route path="/dashboard" element={<Dashboard />} />
      </Routes>
      </BrowserRouter>

    
    </div>
  )
}

export default App
