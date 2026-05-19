import { useState, useRef } from 'react'

const InputBox = () => {
    const [name, setName] = useState("")
    const refElement = useRef("AA") 
    console.log(refElement)
    const previousNameRef = useRef("")

    const clearText =()=> {
      setName("")
      refElement.current.focus()
    }
    const handleInput = (e) => {
      previousNameRef.current = name
      setName(e.target.value)
    }
  return (
    <>
        <h2>Inputing Values</h2>
        <input ref={refElement} type = 'text' value={name} 
        onChange={handleInput}/>
        <button onClick={clearText}>Clear</button>
        <br/>
        <p>Previous Name: {previousNameRef.current}</p>
        <p>Current Name: {name}</p>

    </>
  )
}

export default InputBox