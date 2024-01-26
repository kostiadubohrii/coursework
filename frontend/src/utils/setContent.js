import { Skeleton } from '../components/skeleton/Skeleton'

const setContent = (process, Component, data) => {
    switch (process) {
        case 'loading':
            return <Skeleton />;
        case 'confirmed':
            return <Component {...data} />;
        case 'error':
            return <Skeleton />;
        default:
            throw new Error('Unexpected process state');
    }
}

export default setContent;