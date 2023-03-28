import axios from 'axios'
import React from 'react'

function RentItem(props) {
    const deleteRentHandler = (rent_id) => {
    axios.delete(`/rents/delete/${rent_id}`)
        .then(res => console.log(res.data)) }

    const deleteRentHandlerRerender = (rent_id) => {
    deleteRentHandler(rent_id);
    window.location.reload();

};
    return (
        <div>
            <p>
                <div style={{ fontWeight: 'bold, underline'}}>{props.rent.author}:{props.rent.title} rented by {props.rent.name}
                <button onClick={() => deleteRentHandlerRerender(props.rent.rent_id)} className="btn btn-outline-danger my-2 mx-2" style={{'borderRadius':'10px',alignSelf: 'flex-end'}}>X</button>
                </div>
                <hr></hr>
            </p>
        </div>
    )
}

export default RentItem;
