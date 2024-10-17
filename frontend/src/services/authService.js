import {apiServices} from "./apiService";
import {urls} from "../constants/urls";

const authService = {
    async login(user) {
        const {data: {access}} = await apiServices.post(urls.auth.login, user);
        localStorage.setItem('access', access);
    },

    getSocketToken() {
        return apiServices.get(urls.auth.socket);
    }
}

export {
    authService
}