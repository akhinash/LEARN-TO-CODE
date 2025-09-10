
import { createContext } from "react";
import Child2 from "./Child2";

export const MyContext1 = createContext()

function Contextap2() {
    return (
    <div>
        <MyContext1.Provider value={"Akhinash"}>
            <Child2/></MyContext1.Provider>
    </div>
)
}



export default Contextap2