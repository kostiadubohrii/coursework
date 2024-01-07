import { useEffect, useState } from 'react'; 

import {Alert} from 'react-bootstrap';
import './styles.scss';

import {Bar} from 'react-chartjs-2';
import {Chart as ChartJS} from 'chart.js/auto';

import SearchPanel from '../searchPanel/SearchPanel';
import ProductsFilters from '../productsFilters/ProductsFilter';
import { LimAlert, ExistAlert } from '../alertMessages/alertMessages';

import { yearConfig } from '../../services/yearConfit';

const BarChart = () => {
    const [userData, setUserData] = useState({
        labels: yearConfig,
        // ,'Dec','Jan','Feb',"Mar",'Apr','May'
        datasets: [{label: 'Select a product', }]
    });
    const [limAlert, setLimAlert] = useState(false);
    const [existAlert, setExistAlert] = useState(false);
    const [year, setYear] = useState('2024');

    const onProductSelected = (data) => {
        const newData  = {   
            id: data.id,
            label: data.name,
            data: data.revenue
        }
        
        if (userData.datasets[0].id === undefined){
            setUserData(prevState => ({
                ...prevState,
                datasets: []
            }))
        }
        
        const productExists = userData.datasets.find(item => item.id === newData.id);
        
        if (!productExists) {
            if (userData.datasets.length < 5){
                setUserData(prevState => ({
                    ...prevState,
                    datasets: [...prevState.datasets, newData]
                }))
            }else {
                setLimAlert(true)  
                setTimeout(() => {
                    setLimAlert(false)  
                }, 4000)
            } 
        }else {
            setExistAlert(true)
            setTimeout(() => {
                setExistAlert(false)  
            }, 4000)
        }
    }

    const onDeleteProduct = (id) => {
        let length = userData.datasets.filter(item => item.id !== id).length;
        setUserData(prevState => ({
            ...prevState,
            datasets: length ? prevState.datasets.filter(item => item.id !== id): [{'label': 'Select a product'}]
        }))
    }

    const onYearSelected = (year) => {
        setYear(prevYear => {
            if (prevYear === year){
                return prevYear
            }else {
                return year
            }
        });
    };

    useEffect(() => {
        setUserData({
            labels: yearConfig,
            // ,'Dec','Jan','Feb',"Mar",'Apr','May'
            datasets: [{label: 'Select a product', }]
        })
    }, [year])

    return (
        <div className="section">
            <div className="section_settings">
                <div className="title">Product revenue per year</div>
                <div className="menu">
                    <div className="search-panel">
                        <SearchPanel onProductSelected={onProductSelected} filter={year}/>
                    </div>
                    <ProductsFilters onYearSelected={onYearSelected}/>
                </div> 
                <div className="alerts">
                    { limAlert ? <LimAlert/> : null}
                    { existAlert ? <ExistAlert/> : null}
                </div> 
                <div className="products-menu">
                    {
                        userData.datasets.map((item, i) => {
                            if (item.id === undefined) {
                                return null
                            }
                            return (
                                <div className="button-wrapper">
                                    <Alert variant="info" key={i} onClick={() => onDeleteProduct(item.id)}>{item.label}</Alert>
                                </div> 
                            )
                        })
                    }
                </div>
            </div>
            <div className="chart">
                <Bar data={userData} />
            </div> 
        </div>
    )
}

export default BarChart;