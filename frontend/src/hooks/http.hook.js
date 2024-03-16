import { useState, useCallback } from 'react';
import { createStore, bindActionCreators } from 'redux';
import * as actions from '../actions/actions';
import reducer from '../reducer/reducer';


export const useHttp = () => {
    const [process, setProcess] = useState('loading')

    const store = createStore(reducer);

    const { dispatch } = store;

    const { change } = bindActionCreators(actions, dispatch)

    const request = useCallback(async (url, method = 'GET', body = null, headers = { 'Content-Type': 'application/json' }) => {
        try {
            const response = await fetch(url, { method, body, headers });

            if (!response.ok) {
                change('error')
                throw new Error(`Could not fetch ${url}, status ${response.status}, error ${response.error}`);
            }
            const data = await response.json();
            change('confirmed')
            return data
        } catch (error) {
            change('error')
            throw error;
        }
    }, [])

    const clearError = useCallback(() => {
        change('loading')
    }, []);

    return { request, clearError, process, store };
}