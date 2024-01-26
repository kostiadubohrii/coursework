
const DropDown = ({ dropdownRef, handleItemClick, results }) => {
    return (
        <div className="dropdown display-none" ref={dropdownRef}>
            <ul>
                {
                    results.map(item => {
                        return <li key={item.id} onClick={() => handleItemClick(item)}>{item.name}</li>
                    })
                }
            </ul>
        </div>
    )
}

export default DropDown