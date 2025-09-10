import React, { useState } from "react";
import { useNavigate } from "react-router-dom";

function Mock() {
    const [user, setUser] = useState("");
    const [pass, setPass] = useState("");
    const navigate = useNavigate();

    const handleSubmit = (e) => {
        e.preventDefault();

        if (user === "Akhinash" && pass === "1234") {
            navigate("/dashboard");
        } else {
            alert("Invalid");
        }
    };
    return(

        <form action="" onSubmit={handleSubmit}>
            <h2>Login</h2>
            <input type="text" placeholder="name" 
            value={user}
            onChange={(e) => setUser(e.target.value)}
            />
            <input type="password" placeholder="password" 
            value={pass}
            onChange={(e) => setPass(e.target.value)}
            />
            <button type="submit">Login</button>


        </form>

    )}

    export default Mock;