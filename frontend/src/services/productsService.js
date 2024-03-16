import { useHttp } from "../hooks/http.hook"

const useStatisticsService = () => {
    const { request, process, store } = useHttp();

    const _apiBase = 'http://127.0.0.1:8000/api/';

    const getAllProducts = async () => {
        const res = await request(`${_apiBase}v1/statistics/`);
        return res.data;
    }

    const getAllYears = async () => {
        const res = await request(`${_apiBase}v1/years/`);
        return res.data;
    }

    return {
        getAllProducts,
        getAllYears,
        process,
        store
    }
}

export default useStatisticsService;