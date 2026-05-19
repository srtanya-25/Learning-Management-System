import React from 'react'

const Greeting = ({isLoggedin, name}) => {
  let message
//   console.log("Message is",message)

  if(isLoggedin){
    message = <h1>Welcome Back, {name}</h1>
  } else {
    message = <h1>Please log in to continue</h1>
  }

  return (
    <>
        {{isLoggedin} ? (<h1>Welcome back, {name}</h1>) : (<h1>Please login to continue</h1>)}
    </>
  )
}

export default Greeting