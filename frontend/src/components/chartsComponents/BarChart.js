import { useState } from 'react'; 

import {ButtonGroup, Button} from 'react-bootstrap';
import './styles.scss';
import {Bar} from 'react-chartjs-2';
import {Chart as ChartJS} from 'chart.js/auto';

import {globalData} from '../../services/data';
import SearchPanel from '../searchPanel/SearchPanel';


const BarChart = () => {
    const [userData, setUserData] = useState({
        labels: ['Jun', 'Jul', 'Aug','Sep','Oct','Nov'],
        // ,'Dec','Jan','Feb',"Mar",'Apr','May'
        datasets: [{}]
    });
    const [years, setYears] = useState(['2023','2024'])

    const onProductSelected = (data) => {
        const newData  = {   
            id: data.id,
            label: data.name,
            data: data.revenue
        }

        const productExists = userData.datasets.find(item => item.id === newData.id);
        if (userData.datasets[0].id === undefined){
            setUserData(prevState => ({
                ...prevState,
                datasets: []
            }))
        }

        if (!productExists) {
            setUserData(prevState => ({
                ...prevState,
                datasets: [...prevState.datasets, newData]
            }))
        }
        
    }
    return (
        <div className="section">
            <div className="section_settings_large">
                <div className="title">Products ordered for a year</div>
                <div className="menu">
                    <div className="search-panel">
                        <SearchPanel onProductSelected={onProductSelected} data={globalData}/>
                    </div>
                    <ButtonGroup>
                        {
                            years.map((item, i) => {
                                return <Button variant="secondary" key={i}>Year {item}</Button>
                            })
                        }
                    </ButtonGroup>
                </div>  
            </div>
            <div class="chart">
                <Bar data={userData} />
            </div> 
        </div>
    )
}

export default BarChart;