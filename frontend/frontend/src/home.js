import React, { useContext, useEffect, useState } from "react";
import './App.css';
import axios from 'axios';
import 'bootstrap/dist/css/bootstrap.min.css';
import Container from 'react-bootstrap/Container';
import Nav from 'react-bootstrap/Nav';
import Navbar from 'react-bootstrap/Navbar';
import { LinkContainer } from 'react-router-bootstrap'

const Home = () => {

   const [message, setMessage] = useState("");

  // Making the request
  const getWelcomeMessage = async () => {
    const requestOptions = {
      method: "GET",
      headers: {
        "Content-Type": "application/json",
      },
    };

    const response = await fetch("/nemethxmark", requestOptions);
    const data = await response.json();
    if (!response.ok) {
      console.log("something messed up");
    } else {
      setMessage(data.message);
    }
  };

  useEffect(() => {
    getWelcomeMessage();
  }, []);

    return (
    <div className="App list-group-item justify-content-center align-items-center mx-auto" style={{"width":"700px", "backgroundColor":"white", "marginTop":"15px"}}>
        <Navbar bg="dark" variant="dark">
        <Container>
          <Navbar.Brand className="px-2">BookRent</Navbar.Brand>
          <Nav className="ml-auto px-1">
          <LinkContainer to="/home">
            <Nav.Link className="px-3">Users</Nav.Link>
          </LinkContainer>
          </Nav>
        </Container>
      </Navbar>

     <div className="card-body mt-5">
      <span className="card-text">
        <input className="mb-2 form-control titleIn"  placeholder='book'/>
        <input className="mb-2 form-control desIn"    placeholder='start_date of rent'/>
        <input className="mb-2 form-control desIn"    placeholder='due_date of rent'/>
      <button className="btn btn-outline-primary mx-2 mb-3" style={{'borderRadius':'50px',"font-weight":"bold"}} >Rent a Book </button>
      </span>
      <h5 className="card text-white bg-dark mt-4 mb-4">Your rents</h5>
      <h5 className="card text-white bg-dark mt-3 mb-4">Available books</h5>
      </div>
      <h6 className="card text-dark bg-warning py-1 mb-0" >Copyright 2023, All rights reserved &copy;</h6>
    </div>
  );
}

export default Home;
