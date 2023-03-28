import React, { useContext, useEffect, useState } from "react";
import './App.css';
import axios from 'axios';
import 'bootstrap/dist/css/bootstrap.min.css';
import Container from 'react-bootstrap/Container';
import Nav from 'react-bootstrap/Nav';
import Navbar from 'react-bootstrap/Navbar';
import { LinkContainer } from 'react-router-bootstrap'
import BookView from './components/BookListView'


const Book = () => {

    const [book_author, setAuthor] = useState("");
    const [book_title, setTitle] = useState("");
    const [bookList, setBookList] = useState([]);

  // Read all users
  useEffect(() => {
    axios.get("/books/get")
      .then(res => {
        setBookList(res.data)
      })
  },[]);

  // Post a user
  const addBookHandler = () => {
    axios.post('/books/post', { 'author': book_author, 'title': book_title })
      .then(res => console.log(res)).then(() => {
    this.setState({book_author:'',book_title:''});
  })
};

const addBookHandlerWithRerender = () => {
    addBookHandler();
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
        <input className="mb-2 form-control titleIn"  onChange={event => setAuthor(event.target.value)} placeholder='book_author'/>
        <input className="mb-2 form-control desIn"    onChange={event => setTitle(event.target.value)} placeholder='book_title'/>
      <button className="btn btn-outline-primary mx-2 mb-3" style={{'borderRadius':'50px',"font-weight":"bold"}} onClick={addBookHandlerWithRerender} >Create a Book </button>
      </span>
      <h5 className="card text-white bg-dark mt-3 mb-4">Registered Books</h5>
      <div>
      <BookView bookList={bookList} />
      </div>
      </div>
    </div>
  );
}

export default Book;
