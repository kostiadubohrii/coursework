import {Alert} from 'react-bootstrap';

export const LimAlert = () => {
    return <Alert variant='warning' className='alert-warning'>You can only add 5 products to the chart</Alert>
}

export const ExistAlert = () => {
    return <Alert variant='warning' className='alert-warning'>This product is alredy displayed  in the chart</Alert>
}