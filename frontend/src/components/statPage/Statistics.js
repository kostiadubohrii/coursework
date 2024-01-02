import 'chart.js';
import './statistics.scss';

import BarChart from '../customCharts/BarChart';
import ProductChart from '../customCharts/ProductChart'

const Statistics = () => {
    return (
        <div className='custom-container'>
            <h1 className="title">Statistics</h1>
            <div className="menu">
                <BarChart/>
                <ProductChart/>
                {/* <div class="section section_doughnuts">
                    <div class="divider"> */}
                        
                        {/* <div class="doughtnut doughtnut_ordered-products">
                            <div class="title-settings">
                                <div class="title">Products ordered</div>
                                <div class="setting">
                                    <div class="btn-group" role="group2" aria-label="Basic radio toggle button group">
                                        <button type="button" class="btn btn-outline-primary">TOP 5</button>
                                        <button type="button" class="btn btn-outline-primary">TOP 10</button>
                                        <button type="button" class="btn btn-outline-primary">TOP 15</button>
                                    </div>
                                </div>
                            </div>
                            <div class="diagram produts-ordered-chart">
                                <canvas id="produts-ordered-chart"></canvas>
                            </div>
                        </div> */}
                    {/* </div>
                </div> */}
            </div>
        </div>
    )
}

export default Statistics;