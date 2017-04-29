import dispatcher from './../dispatcher.js';

export function toggleLoggedInState () {
    dispatcher.dispatch({
        type: 'TOGGLE_LOGGED_IN_STATE'
    });
}
