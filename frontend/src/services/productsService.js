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

export const getYears = () => {
    const years = fullData.map(item => item.year);
    return years;
}