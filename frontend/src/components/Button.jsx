import React from 'react'

const Button = () => {
    const handleClick = (message) => {
        console.log(message)
        alert(message)
    }
  return (
    <>
        <button onClick ={() => handleClick("Thanks For Clicking")}>
            Click Me
        </button>
    </>
  )
}

export default Button