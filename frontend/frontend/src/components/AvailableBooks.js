import axios from 'axios'
import React from 'react'

function AvailableBookItem(props) {

    return (
        <div>
            <p>
                <div style={{ fontWeight: 'bold, underline'}}>{props.book.author} : {props.book.title}
                </div>
                <hr></hr>
            </p>
        </div>
    )
}

export default AvailableBookItem;
