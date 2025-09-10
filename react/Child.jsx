import React, { useContext } from "react";
import { MyContext } from "./Contextap";

function Child(){
    const value= useContext(MyContext);
    return <h1>{value}</h1>
}

export default Child