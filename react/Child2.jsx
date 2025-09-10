import React, { useContext } from "react";

import { MyContext1 } from "./Contextap2";

function Child2(){
    const value= useContext(MyContext1);
    return <h1>{value}</h1>
}

export default Child2