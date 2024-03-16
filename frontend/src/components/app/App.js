import AppPanel from "../appPanel/AppPanel";
import ChartsSection from "../chartsSection/ChartsSection";

import useStatisticsService from '../../services/productsService';

import { Provider } from "react-redux";

function App() {

  const { store } = useStatisticsService();

  return (
    <>
      <Provider store={store}>
        <AppPanel />
        <ChartsSection />
      </Provider>
    </>
  );
}

export default App;
