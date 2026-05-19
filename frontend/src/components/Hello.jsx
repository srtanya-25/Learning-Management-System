import React from "react"
const HelloWorld = () => {
    const h2Element = React.createElement("h2", null, "Hello Students")
    let name="John";
    return (
        <>
            {/*{h2Element} */}
            <h2> Hello Students </h2>
            <h3> Hello {name} </h3>
        </>
    );
};

export default HelloWorld;

// using components in app.jsx, rest all in global one in  main.jsx