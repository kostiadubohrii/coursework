import {useState} from 'react'; 

import './styles.scss';
import {Line} from 'react-chartjs-2';
import {Chart as ChartJS} from 'chart.js/auto';

import SearchPanel from '../searchPanel/SearchPanel';
import ProductsFilters from '../productsFilters/ProductsFilter';

import { yearConfig } from '../../services/yearConfit';

const ProductChart = () => {
	const [userData, setUserData] = useState({
			labels: yearConfig,
			datasets:[
				{	
					label: 'This colour represents a product',
					data: [],
					}
				]
  		})
	const [year, setYear] = useState('2024')
	
	const onProductSelected = (data) => {
		setUserData({
			...userData,
			datasets:[
				{	
					...userData.datasets[0],
					label: data.name + ' sold out',
					data: data.sells,
					}
				]
		})
	}

	const onYearSelected = (year) => {
		setYear(year);
		setUserData({
			labels: yearConfig,
			datasets:[
				{	
					label: 'This colour represents a product',
					data: [],
					}
				]
  		});
	}
	
    return (
        <div class="section">
            <div class="section_settings">
                <div class="title">Product orders per year</div>
				<div className="menu">
					<div class="search-panel">
						<SearchPanel onProductSelected={onProductSelected} filter={year}/>
					</div>
					<ProductsFilters onYearSelected={onYearSelected}/>
				</div>
            </div>
            <div class="chart">
                <Line data={userData}/>
            </div> 
        </div>
    )
}

export default ProductChart;