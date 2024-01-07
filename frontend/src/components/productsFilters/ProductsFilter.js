import { useEffect, useState } from "react"
import { ButtonGroup, ToggleButton } from "react-bootstrap";

import { getYears } from "../../services/productsService";

const ProductsFilters = (props) => {
    const [years, setYears] = useState([]);
    const [curYear, setCurYear] = useState('2024');

    useEffect(() => {
        setYears(getYears())
    }, [])

    const handleClick = (year) => {
        props.onYearSelected(year);
        setCurYear(year);
    }

    const renderFilters = (arr) => {
        if (arr.length === 0) {
            return <h5 className="text-center mt-5">Filters are not found</h5>
        }

        return arr.map((year, i) => {
            if (year === curYear) {
                return <ToggleButton 
                    variant='success' 
                    key={i} 
                    onClick={() => handleClick(year)}
                    >Year {year}</ToggleButton>
            }else {
                return <ToggleButton 
                    variant='outline-success'
                    key={i} 
                    onClick={() => handleClick(year)}
                    >Year {year}</ToggleButton>
            }
           
        })
    }

    const elements = renderFilters(years);

    return (
        <ButtonGroup>
            {elements}
        </ButtonGroup>
    )
}


export default ProductsFilters