import BookItem from './Book'

export default function BookView(props) {
    return (
        <div>
            <ul>
                {props.bookList.map(book => <BookItem book={book} />)}
            </ul>
        </div>
    )
}