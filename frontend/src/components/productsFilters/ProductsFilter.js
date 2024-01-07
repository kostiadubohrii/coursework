import { useEffect, useState } from "react"
import { ButtonGroup, ToggleButton } from "react-bootstrap";

import { yearsFilters } from "../../services/data";

const ProductsFilters = (props) => {
    const [years, setYears] = useState([]);

    useEffect(() => {
        setYears(yearsFilters)
    }, [])

    const renderFilters = (arr) => {
        if (arr.length === 0) {
            return <h5 className="text-center mt-5">Filters are not found</h5>
        }

        return arr.map(({year, className}, i) => {
            return <ToggleButton 
                    variant={className} 
                    key={i} 
                    onClick={() => props.onYearSelected(year)}
                    >Year {year}</ToggleButton>
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