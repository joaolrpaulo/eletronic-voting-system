import { EventEmitter } from 'events';
import axios from 'axios';
import https from 'https';

import dispatcher from './../dispatcher.js';

class MainPageStore extends EventEmitter {
    constructor () {
        super();
        this.loggingIn = true;
        this.instance = {
            headers: {'Content-Type': 'application/json'}
        };
    }

    getLoggingInState () {
        return this.loggingIn;
    }

    setLoggingInState () {
        this.loggingIn = !this.loggingIn;
        console.log('changed');
        this.emit('change');
    }

    logInUser (data) {
        axios.post('https://192.168.0.184/login', {
            voter_id: data.username,
            password: data.password
        }, this.instance)
            .then((response) => {
                console.log(response);
            })
            .catch((error) => {
                console.log(error);
            });
    }

    handleActions (action) {
        switch (action.type) {
        case 'TOGGLE_LOGGED_IN_STATE': {
            this.setLoggingInState();
            break;
        }
        case 'LOG_IN_USER': {
            this.logInUser(action.payload);
            break;
        }
        }
    }
}

const mainPageStore = new MainPageStore();
dispatcher.register(mainPageStore.handleActions.bind(mainPageStore));
export default mainPageStore;
