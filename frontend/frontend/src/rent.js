import React, { useContext, useEffect, useState } from "react";
import './App.css';
import axios from 'axios';
import 'bootstrap/dist/css/bootstrap.min.css';
import Container from 'react-bootstrap/Container';
import Nav from 'react-bootstrap/Nav';
import Navbar from 'react-bootstrap/Navbar';
import { LinkContainer } from 'react-router-bootstrap'
import RentsView from './components/RentsListView'
import AvailableBooksView from './components/AvailableBooksView'
import DatePicker from "react-datepicker";

const Rent = () => {

    const [username, setUsername] = useState("");
    const [author, setAuthor] = useState("");
    const [title, setTitle] = useState("");
    const [start_date, setStartdate] = useState(new Date());
    const [due_date, setDuedate] = useState(new Date());
    const [availablebooksList, setAvailableBooksList] = useState([]);
    const [rentsList, setRentsList] = useState([]);

      // Read all users
    useEffect(() => {
    axios.get("/books/get_by_date")
      .then(res => {
        setAvailableBooksList(res.data)
      })
    },[]);

     // Read all users
    useEffect(() => {
    axios.get("/rents/get_active")
      .then(res => {
        setRentsList(res.data)
      })
    },[]);

     // Post a user
  const addRentHandler = () => {
    axios.post('/rents/post', { 'name': username, 'author': author,'title': title,'start_date': start_date,'due_date': due_date })
      .then(res => console.log(res)).then(() => {
    this.setState({name:'',password:''});
        })
    };
    const addRentHandlerWithRerender = () => {
    addRentHandler();
    window.location.reload();
    }

    return (
    <div className="App list-group-item justify-content-center align-items-center mx-auto" style={{"width":"700px", "backgroundColor":"white", "marginTop":"15px"}}>
{/*         <h1> {message} </h1> */}
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
        <input className="mb-2 form-control titleIn"  onChange={event => setUsername(event.target.value)}  placeholder='username'/>
        <input className="mb-2 form-control titleIn"  onChange={event => setAuthor(event.target.value)} placeholder='book_author'/>
        <input className="mb-2 form-control titleIn"  onChange={event => setTitle(event.target.value)} placeholder='book_title'/>
        <input className="mb-2 form-control titleIn"    onChange={event => setStartdate(event.target.value)} placeholder='start_date of rent'/>
        <input className="mb-2 form-control titleIn"    onChange={event => setDuedate(event.target.value)} placeholder='due_date of rent'/>
      <button className="btn btn-outline-primary mx-2 mb-3" style={{'borderRadius':'50px',"font-weight":"bold"}} onClick={addRentHandlerWithRerender} >Rent a Book </button>
      </span>
      <h5 className="card text-white bg-dark mt-3 mb-4">Available books</h5>
      <div>
      <AvailableBooksView availablebooksList={availablebooksList} />
      </div>
      <h5 className="card text-white bg-dark mt-4 mb-4">Active Rents</h5>
      <div>
      <RentsView rentsList={rentsList} />
      </div>
      </div>
    </div>
  );
}

export default Rent;
