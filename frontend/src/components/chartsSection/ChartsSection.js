import 'chart.js';
import './chartsSection.scss';

import ChartProductOrder from '../chartProductOrder/ChartProductOrder';
import ChartProductRevenue from '../chartProductRevenue/ChartProductRevenue';

const ChartsSection = () => {
    return (
        <div className='custom-container'>
            <h1 className="title">Statistics</h1>
            <div className="menu">
                <ChartProductRevenue />
                <ChartProductOrder />
            </div>
        </div>
    )
}

export default ChartsSection;