import { EventEmitter } from 'events';
import axios from 'axios';
import { hashHistory } from 'react-router';

import dispatcher from './../dispatcher.js';
import { axiosConfig } from './../configs.js';
import User from './../User.js';

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
        this.emit('change');
    }

    logInUser (data) {
        axios.post(axiosConfig.baseUrl + '/login', {
            voter_id: data.username,
            password: data.password
        }, axiosConfig.post)
            .then((response) => {
                User.setToken(response.data.token).toggleLoggedIn();
                console.log(User.getToken());
                hashHistory.push('/voting');
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
