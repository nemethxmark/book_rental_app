import RentItem from './Rents'

export default function RentView(props) {
    return (
        <div>
            <ul>
                {props.rentsList.map(rent => <RentItem rent={rent} />)}
            </ul>
        </div>
    )
}