import "./styles.scss";


const AppPanel = () => {

    return (
        <main className="header">
            <div className="header_title">
                Administration
            </div>
            <div className="header_links">
                <a href="http://127.0.0.1:8000/admin/"> HOME </a>
                /
                <a href="http://localhost:3000/"> STATISTICS </a>
            </div>
        </main>
    )
}   

export default AppPanel;