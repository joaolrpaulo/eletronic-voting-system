import dispatcher from './../dispatcher.js';

export function retrievePolls () {
    dispatcher.dispatch({
        type: 'RETRIEVE_POLLS'
    });
}
