import {apiServices} from "./apiService";
import {urls} from "../constants/urls";

const CarService = {
    getAll() {
        return apiServices.get(urls.cars)
    },
    create(data) {
        return apiServices.post(urls.cars, data);
    }
}

export {
    CarService
}