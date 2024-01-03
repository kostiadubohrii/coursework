import { useState} from 'react'; 

import './styles.scss';
import {Line} from 'react-chartjs-2';
import {Chart as ChartJS} from 'chart.js/auto';

import SearchPanel from '../searchPanel/SearchPanel';

const ProductChart = () => {
	const [userData, setUserData] = useState({
			labels: ['Jun', 'Jul', 'Aug','Sep','Oct','Nov','Dec','Jan','Feb',"Mar",'Apr','May'],
			datasets:[
				{	
					label: 'This colour represents a product',
					data: [],
					}
				]
  		});
	
	const onProductSelected = (data) => {
		setUserData({
			...userData,
			datasets:[
				{	
					...userData.datasets[0],
					label: data.name,
					data: data.values,
					}
				]
		})
	}

	
    return (
        <div class="section">
            <div class="section_settings">
                <div class="title">A product order history</div>
                <div class="search">
                   <SearchPanel onProductSelected={onProductSelected} />
                </div>
            </div>
            <div class="chart">
                <Line data={userData}/>
            </div> 
        </div>
    )
}

export default ProductChart;