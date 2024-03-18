import { useState } from 'react';

import '../../styles/charts-style.scss';

import { Bar } from 'react-chartjs-2';
import { Chart as ChartJS } from 'chart.js/auto';

import SearchPanel from '../searchPanel/SearchPanel';
import ChartFilters from '../chartFilters/ChartFilters';
import ChartProductList from '../chartProductList/ChartProductList';
import { LimAlert, ExistAlert } from '../alertMessages/alertMessages';

import { monthsConfig } from '../../services/yearConfit';

const ChartProductRevenue = () => {
    const [data, setData] = useState({ labels: monthsConfig, datasets: [{ label: 'Choose product' }] });
    const [limAlert, setLimAlert] = useState(false);
    const [existAlert, setExistAlert] = useState(false);
    const [year, setYear] = useState('2024');

    const [availibleColours, setAvailibleColours] = useState([
        { colour: '#36a2eb', availible: true },
        { colour: '#ff6384', availible: true },
        { colour: '#4bc0c0', availible: true },
        { colour: '#ff9f40', availible: true },
        { colour: '#9966ff', availible: true }]);

    const onProductSelected = (productData) => {

        const newData = {
            id: productData.id,
            label: productData.name,
            data: productData[year].revenue,
        }

        if (data.datasets[0].id === undefined) {
            setData(prevState => ({
                ...prevState,
                datasets: []
            }))
        }

        const productExists = data.datasets.find(item => item.id === newData.id);

        if (!productExists) {
            if (data.datasets.length < 5) {
                let availible = null;
                let i = 0;
                while (i < availibleColours.length && availible === null) {
                    if (availibleColours[i].availible) {
                        availible = availibleColours[i].colour;
                    }
                    i++;
                }
                newData.backgroundColor = availible;

                setData(prevState => ({
                    ...prevState,
                    datasets: [...prevState.datasets, newData]
                }));

                const updatedColours = [...availibleColours];
                updatedColours[i - 1].availible = false;
                setAvailibleColours(updatedColours)
            } else {
                setLimAlert(true)
                setTimeout(() => {
                    setLimAlert(false)
                }, 4000)
            }
        } else {
            setExistAlert(true)
            setTimeout(() => {
                setExistAlert(false)
            }, 4000)
        }
    }

    const onDeleteProduct = (id, colour) => {
        let length = data.datasets.filter(item => item.id !== id).length;
        setData(prevState => ({
            ...prevState,
            datasets: length ? prevState.datasets.filter(item => item.id !== id) : [{ 'label': 'Choose product' }]
        }))
        availibleColours.forEach((item, i) => {
            if (item.colour === colour) {
                const updatedColours = [...availibleColours];
                updatedColours[i].availible = true;
                setAvailibleColours(updatedColours)
            }
        })


    }

    const onYearSelected = (year) => {
        setYear(prevYear => {
            if (prevYear === year) {
                return prevYear
            } else {
                return year
            }
        });

        setData({ labels: monthsConfig, datasets: [{ label: 'Choose product' }] })
    };

    return (
        <div className="section">
            <div className="section_settings">
                <div className="title">Product revenue per year</div>
                <div className="menu">
                    <div className="search-panel">
                        <SearchPanel onProductSelected={onProductSelected} year={year} />
                    </div>
                    <ChartFilters onYearSelected={onYearSelected} />
                </div>
                <div className="alerts">
                    {limAlert ? <LimAlert /> : null}
                    {existAlert ? <ExistAlert /> : null}
                </div>
                <div className="products-menu">
                    <ChartProductList data={data} onDeleteProduct={onDeleteProduct} />
                </div>
            </div>
            <div className="chart">
                <Bar data={data} />
            </div>
        </div>
    )
}

export default ChartProductRevenue;