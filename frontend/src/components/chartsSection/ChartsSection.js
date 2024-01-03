import 'chart.js';
import './chartsSection.scss';

import BarChart from '../chartsComponents/BarChart';
import ProductChart from '../chartsComponents/ProductChart'

const ChartsSection = () => {
    return (
        <div className='custom-container'>
            <h1 className="title">Statistics</h1>
            <div className="menu">
                <BarChart/>
                <ProductChart/>
            </div>
        </div>
    )
}

export default ChartsSection;