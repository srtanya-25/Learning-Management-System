import React, {useContext} from 'react'
import HelloWorld from './Hello'
import StudentContext from '../context/StudentContext';

export const StudentList = () => {
  // const h2Element = React.createElement("h1",null,"Hello");
  const studentName = useContext(StudentContext)
  return (
    <>
        <h1>Hello</h1>
        {/* { h2Element } */}
        {/* <p>Wssup?</p> */}
        <p>Welcome {studentName}</p>
    </>
  )
}
export default StudentList;