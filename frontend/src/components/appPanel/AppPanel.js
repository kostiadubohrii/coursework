import "./styles.scss";


const AppPanel = () => {

    return (
        <main className="header">
            <div className="header_title">
                Administration
            </div>
            <div className="header_links">
                <a href="http://16.171.199.194:8000/admin/"> HOME </a>
                /
                <a href="https://statistics-b5278.web.app/"> STATISTICS</a>
            </div>
        </main>
    )
}

export default AppPanel;