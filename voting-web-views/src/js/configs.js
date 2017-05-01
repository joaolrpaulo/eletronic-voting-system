// Global configs file
export const axiosConfig = {
    baseUrl: 'https://192.168.0.106',
    post: {
        headers: {'Content-Type': 'application/json'}
    },
    get: function (token) {
        return {
            headers: {'Authorization': 'Bearer ' + token}
        };
    }
};

export const init = () => {
    new WOW().init();
};
