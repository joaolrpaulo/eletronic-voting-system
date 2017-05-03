import dispatcher from 'Utils/dispatcher.js';

export function retrievePolls () {
    dispatcher.dispatch({
        type: 'RETRIEVE_POLLS'
    });
}
