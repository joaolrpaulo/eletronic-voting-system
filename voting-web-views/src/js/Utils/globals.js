import axios from 'axios';

export const SERVER_PUBLIC_KEY =
    `-----BEGIN PUBLIC KEY-----
MIICIjANBgkqhkiG9w0BAQEFAAOCAg8AMIICCgKCAgEAmBfGBjQH05iPyTtksAAa
1r65Sw2XhOpWvDZ5nZpHQVZcIQOYLhpEkZPMo4bF5oO7IG1a7OOFe9kLGuB5kTRF
Mu1SjLVkszWsJ15B2HVpLE+oeyC/NCYbd3KqEFGU38hE0dcDGdXx/2FIaYgDwiXe
erQCwhD+LXAG7gt8L5M73KmPBLZRzF/XmvY7KIyP+kD/Xlx31PCw92OBnQUaZe5B
EuZP1wZvotMhw2jAvZy3LJQcpROcQbcYU7106WNielUBHEy0q6RMf57MM1o6UPN9
FFtj+l9LHyTkUBzANPnhh9qZ+5aZ23A1BAHqMlBoZuSsQ16Ou3N4GeuEoDRNaebz
0MZLtm6ssaN7uE32EqkY2hCy7dTnl7m/TZ/X1TjECZCHe3t+QJ8Y/RBX8jx6S0tI
zFfIvDTRPWuiO+KTx/qaV5/rD5/ICn0QRZBLkqA5XR8raBqHULXa2o+ZW/S8PTMD
+gV73SdidUfdHNJl8Xh3tKzvcSYmYfsbjeNtK8eN25IB48kplQpnXzjxWgV0sn4a
/RPY39ZCvPhpnb4OvlPSBYRLxT6k9YLfRcn7WQA+HVXuNMYigWkNVAjWyjaTlvcD
FwZDRXQYrQ4QS8RsBNDH0MoBT86oIro0y3Po4NbZ54mjJNph+sS075qrhDRvY4O7
gEi4az4NYnO2C+QyJorelgUCAwEAAQ==
-----END PUBLIC KEY-----`;

axios.interceptors.response.use(response => { return Promise.resolve(response); }, error => {
    if (error.response.status === 401) {
        sessionStorage.removeItem('token');
        location.reload();
        return Promise.reject(error);
    }
    return Promise.reject(error);
});
