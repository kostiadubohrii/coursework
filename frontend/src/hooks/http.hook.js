import { useState, useCallback } from 'react';

export const useHttp = () => {
    const [process, setProcess] = useState('loading');

    const request = useCallback(async (url, method = 'GET', body = null, headers = { 'Content-Type': 'application/json' }) => {
        setProcess('loading')
        try {
            const response = await fetch(url, { method, body, headers });

            if (!response.ok) {
                setProcess('error')
                throw new Error(`Could not fetch ${url}, status ${response.status}, error ${response.error}`);
            }
            const data = await response.json();
            setProcess('confirmed')
            return data
        } catch (error) {
            setProcess('error')
            throw error;
        }
    }, [])

    const clearError = useCallback(() => {
        setProcess('loading')
    }, []);

    return { request, clearError, process };
}