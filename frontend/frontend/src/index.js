import React from 'react';
import ReactDOM from 'react-dom';
import './index.css';
import App from './App';
import 'bootstrap/dist/css/bootstrap.min.css'
import { BrowserRouter as Router, Routes, Route } from "react-router-dom";
import User from './user'
import Book from './book'
import Rent from './rent'
ReactDOM.render(
       <Router>
      <Routes>
        <Route index path="/" element={<App />} />
        <Route path="/user" element={<User/>} />
        <Route path="/book" element={<Book/>} />
        <Route path="/rent" element={<Rent/>} />
      </Routes>
    </Router>,
  document.getElementById('root')
);