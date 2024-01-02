import { useState, useEffect, useCallback, useRef } from 'react'; 

import Form from 'react-bootstrap/Form';
import './styles.scss';
import {Line} from 'react-chartjs-2';
import {Chart as ChartJS} from 'chart.js/auto';


const SearchPanel = () => {
	const [name, setName] = useState('');
	const [data, setData] = useState([{ name: 'Apple Iphone' }, { name: 'Apple watch' }, { name: 'HP M27fq' }]);
	const [results, setResults] = useState([]);
	const [product, setProduct] = useState(null);

	const dropdownRef = useRef(null);

	const handleChange = useCallback((e) => {
	  setName(e.target.value);
	}, []);
 
	useEffect(() => {
	  setResults(searchProduct(data, name));
	}, [name]);
 
	function searchProduct(items, name) {
	  name = name.toLowerCase().replace(/\s/g, '');
	  if (name.length === 0) {
		 return items;
	  }
 
	  return items.filter((item) => {
		 return item.name.toLowerCase().replace(/\s/g, '').indexOf(name) > -1;
	  });
	}

	function toggleDisplay(toRemove){
		if (toRemove) {
			dropdownRef.current.classList.remove('display-block');
			dropdownRef.current.classList.add('display-none');
		}else {
			dropdownRef.current.classList.remove('display-none');
			dropdownRef.current.classList.add('display-block');
		}
	}

	const handleClickOutside = (event) => {
		if (dropdownRef.current && !dropdownRef.current.contains(event.target)) {
			toggleDisplay(true)
		}
	};

	useEffect(() => {
		document.addEventListener('mousedown', handleClickOutside);

		return () => {
		  document.removeEventListener('mousedown', handleClickOutside);
		};

	}, []);

	const handleClick = () => {
		toggleDisplay(false)
	}

	const handleItemClick = (product) => {
		setProduct(product)
	}

	useEffect(() => {
		toggleDisplay(true)
	}, [product])


	return (
	  <>
		 <Form.Control 
		 		type="name" 
				id="name" 
				onChange={(e) => handleChange(e)} 
				onClick={handleClick}/>
		 <div className="dropdown display-none" ref={dropdownRef}>
			<ul>
				{
					results.map((item, i) => {
						return <li key={i} onClick={() => handleItemClick(item)}>{item.name}</li>
					})
				}
			</ul>
		 </div>
	  </>
	);
 };

const ProductChart = () => {
	const [userData, setUserData] = useState({
			labels: ['Jun', 'Jul', 'Aug','Sep','Oct','Nov','Dec','Jan','Feb',"Mar",'Apr','May'],
			datasets:[
				{	
					label: 'Iphone',
					data: [5, 6, 3, 15, 16, 19, 21, 20, 18, 15, 14, 15],
					}
			]
  		});

	
    return (
        <div class="section">
            <div class="section_settings">
                <div class="title">A product's history of selling</div>
                <div class="search">
                   <SearchPanel/>
                </div>
            </div>
            <div class="chart">
                <Line data={userData}/>
            </div> 
        </div>
    )
}

export default ProductChart;