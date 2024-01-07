import { useState, useEffect, useCallback, useRef } from 'react'; 

import Form from 'react-bootstrap/Form';
import './searchPanel.scss';
import { fullData } from '../../services/data';

const SearchPanel = () => {
	const [name, setName] = useState('');
	const [data, setData] = useState(fullData);
	const [results, setResults] = useState([]);

	const dropdownRef = useRef(null);
	const inputRef = useRef();

	useEffect(() => {
		document.addEventListener('mousedown', handleClickOutside);

		return () => {
		  document.removeEventListener('mousedown', handleClickOutside);
		};
	}, [])

	useEffect(() => {
        setResults(searchProduct(data, name));
    }, [data, name]);

	// const filterData = (filter, data) => {
	// 	let results;
	// 	data.forEach(item => {
	// 		if (item.year === filter){
	// 		results = item.data
	// 		}
	// 	});
	// 	return results
	// }
 
	function searchProduct(data, name) {
		name = name.toLowerCase().replace(/\s/g, '');
		if (name.length === 0) {
			return data;
		}
	
		return data.filter((item) => {
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
	
	const handleChange = useCallback((e) => {
		setName(e.target.value);
	  }, []);

	const handleClick = () => {
		toggleDisplay(false)
	}

	const handleItemClick = (product) => {
		toggleDisplay(true)
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
					{results && results.map((item, i) => (
						 <li key={i} onClick={() => handleItemClick(item)}>
							{item.name}
						</li>
					))}
				</ul>
		 	</div>
		 </div>
	);
};

export default SearchPanel;