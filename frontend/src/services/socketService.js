import {authService} from "./authService";
import {w3cwebsocket as W3cwebsocket} from 'websocket';

const baseUrl = "ws://localhost:81/api";

const socketService = async () => {
    const {data: {token}} = await authService.getSocketToken()
    return {
        chat: (room) => new W3cwebsocket(`${baseUrl}/chat/${room}/?token=${token}`),
    };
}

export {
    socketService
}