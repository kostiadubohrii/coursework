import { useState } from 'react';

import '../../styles/charts-style.scss';
import { Line } from 'react-chartjs-2';
import { Chart as ChartJS } from 'chart.js/auto';

import SearchPanel from '../searchPanel/SearchPanel';
import ChartFilters from '../chartFilters/ChartFilters';

import { monthsConfig } from '../../services/yearConfit';

const ChartProductOrder = () => {
    const [userData, setUserData] = useState({ labels: monthsConfig, datasets: [{ label: 'Choose product', data: [] }] })
    const [year, setYear] = useState('2024')

    const onProductSelected = (data) => {
        setUserData({
            ...userData,
            datasets: [
                {
                    ...userData.datasets[0],
                    label: data.name + ' sold out',
                    data: data[year].sold,
                }
            ]
        })
    }

    const onYearSelected = (year) => {
        setYear(year);
        setUserData({
            labels: monthsConfig,
            datasets: [{ label: 'Choose product', data: [] }]
        });
    }

    return (
        <div class="section">
            <div class="section_settings">
                <div class="title">Product orders per year</div>
                <div className="menu">
                    <div class="search-panel">
                        <SearchPanel onProductSelected={onProductSelected} year={year} />
                    </div>
                    <ChartFilters onYearSelected={onYearSelected} />
                </div>
            </div>
            <div class="chart">
                <Line data={userData} />
            </div>
        </div>
    )
}

export default ChartProductOrder;