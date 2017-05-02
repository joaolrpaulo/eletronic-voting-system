import dispatcher from './../dispatcher.js';

export function toggleLoggedInState () {
    dispatcher.dispatch({
        type: 'TOGGLE_LOGGED_IN_STATE'
    });
}

export function logInUser (voterId, password) {
    dispatcher.dispatch({
        type: 'LOG_IN_USER',
        payload: {
            voterId,
            password
        }
    });
}

export function registerUser (user) {
    dispatcher.dispatch({
        type: 'REGISTER_USER',
        payload: {
            user
        }
    });
}
