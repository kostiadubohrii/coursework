import { Alert } from 'react-bootstrap';

const ChartProductList = ({ data, onDeleteProduct }) => {

    const elements = data.datasets.map((item) => {
        if (item.id === undefined) {
            return null
        }
        return (
            <Alert
                variant="info"
                key={item.id}
                onClick={() => onDeleteProduct(item.id, item.backgroundColor)}
                className='alert-item'
            >{item.label} &#10005;
            </Alert>
        )
    })

    return (
        <div className="products_list">
            {elements}
        </div>
    )
}

export default ChartProductList;