import { useState, useEffect, useCallback, useRef } from 'react'; 

import Form from 'react-bootstrap/Form';
import './searchPanel.scss';


const SearchPanel = (props) => {
	const [name, setName] = useState('');
	const [data, setData] = useState(props.data);
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
		props.onProductSelected(product)
		toggleDisplay(true)
		clearInput()
	}

	const inputRef = useRef();

	const clearInput = () => {
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