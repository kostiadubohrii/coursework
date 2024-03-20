import { useState, useEffect, useCallback, useRef } from 'react';

import Form from 'react-bootstrap/Form';
import './searchPanel.scss';

import DropDown from '../dropDown/dropDown';

import useStatisticsService from '../../services/productsService';

const SearchPanel = (props) => {
	const [name, setName] = useState('');
	const [data, setData] = useState([]);
	const [results, setResults] = useState([]);

	const { getAllProducts } = useStatisticsService();

	const dropdownRef = useRef(null);

	const handleChange = useCallback((e) => {
		setName(e.target.value);
	}, []);

	useEffect(() => {
		getAllProducts()
			.then(data => setData(() => filterData(data, props.year)))
	}, [props.year])

	useEffect(() => {
		setResults(searchProduct(data, name));
	}, [name, data]);

	function filterData(data, filter) {
		const filteredData = data.filter(item => item.hasOwnProperty(filter))
		const sm = filteredData.map(item => {
			if (item.name.length > 20) {
				return {
					...item,
					name: `${item.name.slice(0, 17)}...`
				}
			}
			return item
		})
		return sm;
	}

	//Searching -> 

	function searchProduct(items, name) { // sershing function. It takes items and name as arguments
		name = name.toLowerCase().replace(/\s/g, ''); // Compresses the value which is typed in. By making it in lower case and removing all spaces
		if (name.length === 0) { // If no name was provided, return all results.
			return items;
		}

		return items.filter((item) => { // Otherwise, filter all items by finding some similarities between serach value and items.s
			return item.name.toLowerCase().replace(/\s/g, '').indexOf(name) > -1;
		});
	}
	// ------------------
	// Dropdown menu toggling-> 

	function toggleDisplay(toRemove) {
		if (toRemove) {
			dropdownRef.current.classList.remove('display-block');
			dropdownRef.current.classList.add('display-none');
		} else {
			dropdownRef.current.classList.remove('display-none');
			dropdownRef.current.classList.add('display-block');
		}
	}
	// -----------------
	// Remoeve menu if click is outsite of it

	const handleClickOutside = (event) => {
		if (dropdownRef.current && !dropdownRef.current.contains(event.target)) {
			toggleDisplay(true)
		}
	};

	//----------------

	useEffect(() => {
		document.addEventListener('mousedown', handleClickOutside);

		return () => {
			document.removeEventListener('mousedown', handleClickOutside);
		};

	}, []);

	const handleClick = () => {
		toggleDisplay(false)
	}

	const inputRef = useRef();

	const handleItemClick = (product) => {
		toggleDisplay(true)
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
			<DropDown handleItemClick={handleItemClick} results={results} dropdownRef={dropdownRef} />
		</div>
	);
};

export default SearchPanel;