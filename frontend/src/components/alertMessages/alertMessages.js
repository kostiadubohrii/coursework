import { Alert } from 'react-bootstrap';

export const LimAlert = () => {
    return <Alert variant='warning' className='alert-warning'>You can only add 5 products on the chart</Alert>
}

export const ExistAlert = () => {
    return <Alert variant='warning' className='alert-warning'>Product has alredy been displayed on the chart</Alert>
}