import AvailableBookItem from './AvailableBooks'

export default function AvailableBooksView(props) {
    return (
        <div>
            <ul>
                {props.availablebooksList.map(book => <AvailableBookItem book={book} />)}
            </ul>
        </div>
    )
}