import StudentList from "./StudentList";

const Mentor = ( {studentName} ) => {
    // const handleClick = () => {
    //     sendData("John Doe")
    // }
  return (
    <>
        {/* <h3>Mentor Component</h3>
        <button onClick= {handleClick}>
            Send data to Parent
        </button> */}
        <StudentList/>
    </>
  )
}

export default Mentor