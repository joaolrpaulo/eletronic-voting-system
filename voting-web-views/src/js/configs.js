// Global configs file
export const axiosConfig = {
    baseUrl: 'https://192.168.0.106',
    post: {
        headers: {'Content-Type': 'application/json'}
    },
    get: function (token) {
        console.log('Bearer ' + token);
        return {
            headers: {'Authorization': 'Bearer ' + token}
        };
    }
};
