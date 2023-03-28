// Importing modules
import React, { useContext, useEffect, useState } from "react";
import './App.css';
import axios from 'axios';
import 'bootstrap/dist/css/bootstrap.min.css';
import Container from 'react-bootstrap/Container';
import Nav from 'react-bootstrap/Nav';
import Navbar from 'react-bootstrap/Navbar';
import { LinkContainer } from 'react-router-bootstrap'
import User from './user'
import UserView from './components/UserListView'

const UserApp = () => {
    const [username, setUsername] = useState("");
    const [password, setPassword] = useState("");
    const [userList, setUserList] = useState([]);

  // Read all users
  useEffect(() => {
    axios.get("/users/get")
      .then(res => {
        setUserList(res.data)
      })
  },[]);

  // Post a user
  const addUserHandler = () => {
    axios.post('/users/post', { 'name': username, 'password': password })
      .then(res => console.log(res)).then(() => {
    this.setState({name:'',password:''});
  })
};

const addUserHandlerWithRerender = () => {
    addUserHandler();
    window.location.reload();
};

    return (
    <div className="App list-group-item justify-content-center align-items-center mx-auto" style={{"width":"700px", "backgroundColor":"white", "marginTop":"15px"}}>
        <h6 className="card text-dark bg-warning py-0 mb-1" > Created by Márk Németh @ 2023 </h6>
        <Navbar bg="dark" variant="dark">
        <Container>
          <Navbar.Brand className="px-2">BookRent</Navbar.Brand>
          <Nav className="ml-auto px-1">
          <LinkContainer to="/rent">
            <Nav.Link className="px-3">Rents</Nav.Link>
          </LinkContainer>
          <LinkContainer to="/book">
            <Nav.Link className="px-2">Books</Nav.Link>
          </LinkContainer>
          <LinkContainer to="/user">
            <Nav.Link className="px-2">Users</Nav.Link>
          </LinkContainer>
          </Nav>
        </Container>
      </Navbar>

     <div className="card-body mt-5">
      <span className="card-text">
        <input className="mb-2 form-control titleIn"  onChange={event => setUsername(event.target.value)} placeholder='username'/>
        <input className="mb-2 form-control desIn"    onChange={event => setPassword(event.target.value)} placeholder='password'/>
      <button className="btn btn-outline-primary mx-2 mb-3" style={{'borderRadius':'50px',"font-weight":"bold"}} onClick={addUserHandlerWithRerender} >Create an User </button>
      </span>
      <h5 className="card text-white bg-dark mt-3 mb-4">Registered Users</h5>
      <div>
      <UserView userList={userList} />
      </div>
      </div>
    </div>
  );
}

export default UserApp;