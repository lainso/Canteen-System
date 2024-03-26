import axios from "axios";
import { baseURL_main } from '../config/baseURL.js'

//创建axios
var instance = axios.create({
    baseURL: baseURL_main,
    timeout: 5000,
    withCredentials: true
});

let csrfToken = null;

export const getCsrfToken = async () => {
    const response = await instance.get('/api/customer/account/getToken');
    csrfToken = response.data.csrf_token;
    return csrfToken;
};

instance.interceptors.request.use(async (config) => {
    if (config.method !== 'get') {
        config.headers['X-CSRFToken'] = await getCsrfToken();
    }
    return config;
}, (error) => {
    return Promise.reject(error);
});

instance.interceptors.response.use(
    response => {
        if (response.data.code === 302 && response.data.redirect) {
            window.location.href = response.data.redirect;
        }
        return response;
    },
    error => {
        if (error.response && error.response.data.code === 302 && error.response.data.redirect) {
            window.location.href = error.response.data.redirect;
        }
        return Promise.reject(error);
    }
);

// 四种http请求的封装
export const $get = async (url, params = {}) => {
    let { data } = await instance.get(url, { params })
    return data
}

export const $post = async (url, params = {}) => {
    let { data } = await instance.post(url, params)
    return data
}

export const $put = async (url, params = {}) => {
    let { data } = await instance.put(url, params)
    return data
}

export const $delete = async (url, params = {}) => {
    let { data } = await instance.delete(url, { params })
    return data
}