// Global configs file
import axios from 'axios';

import User from 'Models/User.js';

export const axiosConfig = {
    baseUrl: 'https://nuno.sytes.net',
    post: {
        headers: {'Content-Type': 'application/json'}
    },
    get: function (token) {
        return {
            headers: {'Authorization': 'Bearer ' + token}
        };
    }
};

export const axiosMethods = {
    get: function (endPoint) {
        return axios.get(axiosConfig.baseUrl + endPoint, axiosConfig.get(User.getToken()));
    },

    post: function (endPoint, body) {
        return axios.post(axiosConfig.baseUrl + endPoint, body, axiosConfig.post);
    }
};

export const init = () => {
    new WOW().init();
};
