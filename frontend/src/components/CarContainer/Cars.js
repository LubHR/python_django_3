import React, {useEffect, useState} from 'react';
import {CarService} from "../../services/carService";
import {socketService} from "../../services/socketService";

const Cars = () => {
    const [cars, setCars] = useState([])
    const [triger, setTriger] = useState(null)

    useEffect(() => {
        CarService.getAll().then(({data}) => setCars(data));
    }, [triger])

    useEffect(() => {
        socketInit()
    }, [])

    const socketInit = async () => {
        const {cars} = await socketService()
        const client = await cars()

        client.onopen = () => {
            console.log("Client connected");
            client.send(JSON.stringify({
                action: 'subscribe_to_car_activity',
                request_id: new Date().getTime(),
            }))
        }

        client.onmessage = ({data}) => {
            console.log(data)
            setTriger(prev => !prev)
        }
    }

    return (
        <div>
            {cars.map(car => <div>{JSON.stringify(car)}</div>)}
        </div>
    );

};

export default Cars;