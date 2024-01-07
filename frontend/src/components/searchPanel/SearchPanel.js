import { useState, useEffect, useCallback, useRef } from 'react'; 

import Form from 'react-bootstrap/Form';
import './searchPanel.scss';

import { fullData } from '../../services/data';

const SearchPanel = (props) => {
	const [name, setName] = useState('');
	const [data, setData] = useState(() => filterData(fullData, props.filter));
	const [results, setResults] = useState([]);
	const [filter, setFitler] = useState(props.filter)

	const dropdownRef = useRef(null);

	const handleChange = useCallback((e) => {
	  setName(e.target.value);
	}, []);

	useEffect(() => {
		setFitler(props.filter)

	}, [props.filter])

	useEffect(() => {
		setData(filterData(fullData, props.filter))
	}, [filter])
 
	useEffect(() => {
	  setResults(searchProduct(data, name));
	}, [name,data]);

	function filterData(data, filter){
		let filteredData = {};
		data.forEach(item => item.year === filter ? filteredData = item : null);
		return filteredData.data;
	}
 
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
		toggleDisplay(true)
		clearInput(product)
	}

	const inputRef = useRef();

	const clearInput = (product) => {
		props.onProductSelected(product)
		setName('');
		inputRef.current.value = '';
	}

	return (
	  	<div className="search">
		 	<Form.Control 
		 		type="name" 
				id="name" 
				onChange={(e) => handleChange(e)} 
				onClick={handleClick}
				ref={inputRef}
				/>
			 <div className="dropdown display-none" ref={dropdownRef}>
				<ul>
					{
						results.map((item, i) => {
						return <li key={i} onClick={() => handleItemClick(item)}>{item.name}</li>
						})
					}
				</ul>
		 	</div>
		 </div>
	);
};

export default SearchPanel;