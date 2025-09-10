import React, { useContext } from 'react'
import { Authcontext } from './Authcontext'

const Home = () => {
    const { login, setLogin } = useContext(Authcontext)
    return (
        // <div>
        //     <h2>{login ? "welcome back" : 'please log in'}</h2>
        //     <button onClick={() => { setLogin(!login) }}>
        //         {login ? 'log out' : 'log in'}</button>

        // </div>

    //     <BrowserRouter>
    //   <Routes>
    //     <Route path="/" element={<Login />} />
    //     <Route path="/dashboard" element={<Dashboard />} />
    //   </Routes>
    // </BrowserRouter> 
        <>
        hiii
        </>
    )
}

export default Home
