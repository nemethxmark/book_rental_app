import UserItem from './User'

export default function UserView(props) {
    return (
        <div>
            <ul>
                {props.userList.map(user => <UserItem user={user} />)}
            </ul>
        </div>
    )
}