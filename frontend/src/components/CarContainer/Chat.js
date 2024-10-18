import React, {useEffect, useRef, useState} from 'react';
import {socketService} from "../../services/socketService";

const Chat = () => {
    const [room, setRoom] = useState(null);
    const roomInput = useRef(null);

    const [messages, setMessages] = useState([])

    const [socketClient, setSocketClient] = useState()

    useEffect(() => {
        if (room) {
            socketInit(room).then(client => setSocketClient(client))
        }
    }, [room])

    const socketInit = async (room) => {
        const {chat} = await socketService();
        const client = await chat(room);

        client.onopen = () => {
            console.log('Chat socket connected');
        }

        client.onmessage = ({data}) => {
            const {message, user} = JSON.parse(data.toString())
            setMessages(prevState => [...prevState, {user, message}])
        }

        return client;
    }

    const roomHendler = () => {
        setRoom(roomInput.current.value);
    }

    const handlerEnter = (e) => {
        if (e.key === 'Enter') {
            socketClient.send(JSON.stringify({
                data: e.target.value,
                action: 'send_message',
                request_id: new Date().getTime(),
            }))
            e.target.value = '';
        }
    }

    return (
        <div>
            {
                !room
                    ?
                    <div>
                        <input type="text" ref={roomInput}/>
                        <button onClick={roomHendler}>Go to room</button>
                    </div>
                    :
                    <div>
                        {
                            messages.map(msg => <div>{msg.user}: {msg.message}</div>)
                        }
                        <input type={'text'} onKeyDown={handlerEnter}/>
                    </div>
            }
        </div>
    );
};

export default Chat;