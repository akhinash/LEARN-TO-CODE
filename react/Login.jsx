import React, { useState } from "react";
import { useNavigate } from "react-router-dom";

function Login() {
    const [user, setUser] = useState("");
    const [pass, setPass] = useState("");
    const navigate = useNavigate();

    const handleSubmit = (e) => {
        e.preventDefault();

        if (user === "akhinash" && pass === "1234") {
            navigate("/dashboard");
        } else {
            alert("Invalid");
        }
    };

    return (
        <div>
            <h2>Login</h2>
            <form onSubmit={handleSubmit}>
                <input type="text"
                    placeholder="Username"
                    value={user}
                    onChange={(e) => setUser(e.target.value)}
                
                />
                <br/>
                <input type="password"
                    placeholder="Password"
                    value={pass}
                    onChange={(e) => setPass(e.target.value)}
                    
                />
                <br/>
                <button type="submit">Login</button>
            </form>
        </div>
    );
}

export default Login;
