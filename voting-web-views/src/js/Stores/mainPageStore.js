import { EventEmitter } from 'events';

import dispatcher from './../dispatcher.js';

class MainPageStore extends EventEmitter {
    constructor () {
        super();
        this.loggingIn = true;
    }

    getLoggingInState () {
        return this.loggingIn;
    }

    setLoggingInState () {
        this.loggingIn = !this.loggingIn;
    }

    handleActions (action) {
        switch (action.type) {
            case 'TOGGLE_LOGGED_IN_STATE': {
                this.setLoggingInState();
                break;
            }
        }
    }
}

const mainPageStore = new MainPageStore();
dispatcher.register(mainPageStore.handleActions.bind(mainPageStore));
export default mainPageStore;
