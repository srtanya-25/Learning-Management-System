import Mentor from "./Mentor"

const Teachers = ({studentName}) => {
//const Teachers = ({name, id}) => {
  return (
    <>
        <h2>Teachers</h2>
        {/* <h3>Name: {name} </h3> */}
        {/* <h3>ID: {id} </h3> */}
        <Mentor studentName={studentName}/>
    </>
    
  )
}

export default Teachers