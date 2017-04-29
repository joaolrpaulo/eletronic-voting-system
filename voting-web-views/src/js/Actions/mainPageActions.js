import dispatcher from './../dispatcher.js';

export function toggleLoggedInState () {
    dispatcher.dispatch({
        type: 'TOGGLE_LOGGED_IN_STATE'
    });
}

export function logInUser (username, password) {
    dispatcher.dispatch({
        type: 'LOG_IN_USER',
        payload: {
            username,
            password
        }
    });
}
