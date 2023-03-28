import axios from 'axios'
import React from 'react'

function BookItem(props) {
    const deleteBookHandler = (book_id) => {
    axios.delete(`/books/delete/${book_id}`)
        .then(res => console.log(res.data)) }

    const deleteBookHandlerWithRerender = (book_id) => {
    deleteBookHandler(book_id);
    window.location.reload();

};
    return (
        <div>
            <p>
                <div style={{ fontWeight: 'bold, underline'}}>{props.book.author} : {props.book.title}
                <button onClick={() => deleteBookHandlerWithRerender(props.book.book_id)} className="btn btn-outline-danger my-2 mx-2" style={{'borderRadius':'10px',alignSelf: 'flex-end'}}>X</button>
                </div>
                <hr></hr>
            </p>
        </div>
    )
}

export default BookItem;
