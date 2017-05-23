// Global configs file
import axios from 'axios';

import User from 'Models/User.js';

export const axiosConfig = {
    baseUrl: 'https://144.64.14.55',
    post: function (loggingIn) {
        if (loggingIn) {
            return {
                headers: {
                    'Content-Type': 'application/json'
                }
            };
        } else {
            const token = User.getToken();
            return {
                headers: {
                    'Content-Type': 'application/json',
                    'Authorization': token
                }
            };
        }
    },
    get: function () {
        const token = User.getToken();
        return {
            headers: {'Authorization': token}
        };
    }
};

export const axiosMethods = {
    get: function (endPoint) {
        return axios.get(axiosConfig.baseUrl + endPoint, axiosConfig.get());
    },

    post: function (endPoint, body) {
        if (endPoint === '/login') {
            return axios.post(axiosConfig.baseUrl + endPoint, body, axiosConfig.post(true));
        } else {
            return axios.post(axiosConfig.baseUrl + endPoint, body, axiosConfig.post(false));
        }
    }
};

export const init = () => {
    new WOW().init();
};
