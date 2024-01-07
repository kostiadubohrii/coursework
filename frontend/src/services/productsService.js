import { fullData } from "./data"

export const getProducts = () => {
    return fullData.flatMap(item => item.data)
}

export const getProductByYear = (year) => {
    let res;
    fullData.forEach(item => {
        if (item.year === year){
           res = item.data
        }
    });

    return res;
}