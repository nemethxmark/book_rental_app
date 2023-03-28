import axios from 'axios'
import React from 'react'

function UserItem(props) {
    const deleteUserHandler = (user_id) => {
    axios.delete(`/users/delete/${user_id}`)
        .then(res => console.log(res.data)) }

    const deleteUserHandlerWithRerender = (user_id) => {
    deleteUserHandler(user_id);
    window.location.reload();

};
    return (
        <div>
            <p>
                <div style={{ fontWeight: 'bold, underline'}}>{props.user.name}
                <button onClick={() => deleteUserHandlerWithRerender(props.user.user_id)} className="btn btn-outline-danger my-2 mx-2" style={{'borderRadius':'10px',alignSelf: 'flex-end'}}>X</button>
                </div>
                <hr></hr>
            </p>
        </div>
    )
}

export default UserItem;
