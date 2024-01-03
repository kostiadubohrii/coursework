import { useState } from 'react'; 

import {ButtonGroup, Button} from 'react-bootstrap';
import './styles.scss';
import {Bar} from 'react-chartjs-2';
import {Chart as ChartJS} from 'chart.js/auto';

import {UserData} from '../../services/data';


const BarChart = () => {
  const [userData, setUserData] = useState({
    labels: UserData.map((data) => data.year),
    datasets: [{
      label: "Users Gained",
      data: UserData.map((data) => data.userGain)
    }]
  });
    return (
        <div className="section">
            <div className="section_settings">
                <div className="title">Products ordered for a year</div>
                <div clasNames="panel">
                    <ButtonGroup>
                        <Button variant="secondary">Year 2023</Button>
                        <Button variant="secondary">Year 2024</Button>
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