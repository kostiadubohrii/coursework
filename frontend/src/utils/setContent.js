import Skeleton from '../components/skeleton/Skeleton'
import ErrorMessage from '../components/errorMessage/ErrorMessage';

const setContent = (process, Component, data) => {
    switch (process) {
        case 'loading':
            return <Skeleton />;
        case 'confirmed':
            return <Component data={data} />;
        case 'error':
            return <Skeleton />;
        default:
            throw new Error('Unexpected process state');
    }
}

export default setContent;