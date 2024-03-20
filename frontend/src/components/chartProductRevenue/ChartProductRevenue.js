import { useState } from 'react';

import '../../styles/charts-style.scss';

import { Bar } from 'react-chartjs-2';
import { Chart as ChartJS } from 'chart.js/auto';

import SearchPanel from '../searchPanel/SearchPanel';
import ChartFilters from '../chartFilters/ChartFilters';
import ChartProductList from '../chartProductList/ChartProductList';
import { LimAlert, ExistAlert } from '../alertMessages/alertMessages';

import { monthsConfig } from '../../services/yearConfit';
import { coloursConfig } from '../../services/coloursConfig';

const ChartProductRevenue = () => {
    const [data, setData] = useState({ labels: monthsConfig, datasets: [{ label: 'Choose product' }] });
    const [limAlert, setLimAlert] = useState(false);
    const [existAlert, setExistAlert] = useState(false);
    const [year, setYear] = useState('2024');

    const [availibleColours, setAvailibleColours] = useState(coloursConfig);

    const onProductSelected = (productData) => {

        const newData = { //set new object of product 
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
                let availible = null; // Set the flag in null. Later will be changed onto a colour.
                let i = 0; // set the iterator 
                while (i < availibleColours.length && availible === null) { // run lopp. while i less
                    // than length of array and availible was not found
                    if (availibleColours[i].availible) { // When the availible colour is found 
                        availible = availibleColours[i].colour; // set availible colour
                    }
                    i++;
                }
                newData.backgroundColor = availible; // set backgroound colour of the item to be dislayed

                setData(prevState => ({ // this function updates the informatiion inside the chart
                    ...prevState,
                    datasets: [...prevState.datasets, newData]
                }));

                const updatedColours = [...availibleColours];
                updatedColours[i - 1].availible = false; // Set the selected colour availibility to false
                setAvailibleColours(updatedColours) // save it 
            } else {
                setAlert() // set alert
            }
        } else {
            setAlert()
        }
    }

    function setAlert() { // alert setting function
        setExistAlert(true)
        setTimeout(() => { // define how long the alert will be shown for
            setExistAlert(false) // afte time is out remove the alert
        }, 4000)
    }

    const onDeleteProduct = (id, colour) => { //take two parameters
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
        setAvailibleColours(prev => ([
            ...prev.map(item => ({
                colour: item.colour,
                availible: true
            }))
        ]))
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