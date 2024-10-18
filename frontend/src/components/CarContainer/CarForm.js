import React from 'react';
import {useForm} from "react-hook-form";
import {CarService} from "../../services/carService";

const CarForm = () => {
    const {register, handleSubmit, reset} = useForm()

    const save = async (car) => {
        await CarService.create(car)
        reset()
    }
    return (
        <form onSubmit={handleSubmit(save)}>
            <input type={"text"} placeholder={"model"} {...register("model")}/>
            <input type={"text"} placeholder={"price"} {...register("price")}/>
            <input type={"text"} placeholder={"year"} {...register("year")}/>
            <button>save</button>
        </form>
    );
};

export default CarForm;