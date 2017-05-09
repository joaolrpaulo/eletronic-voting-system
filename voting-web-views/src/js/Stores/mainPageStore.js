import { EventEmitter } from 'events';
import { hashHistory } from 'react-router';

import dispatcher from 'Utils/dispatcher.js';
import { axiosMethods } from 'Utils/configs.js';
import User from 'Models/User.js';

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

    logInUser ({voterId, password}) {
        const body = {
            voter_id: voterId,
            password
        };

        axiosMethods.post('/login', body)
            .then(response => {
                const token = response.data.token;

                User.setToken(token).toggleLoggedIn();
                hashHistory.push('/voting');
                sessionStorage.token = token;
            })
            .catch(() => {
                const paragraphWrongCredentials = document.getElementById('wrong-credentials');
                paragraphWrongCredentials.className = paragraphWrongCredentials.className.replace('invisible', 'wrong-credentials');
            });
    }

    registerUser ({voter_id, password, email, name, city}) {
        const body = {
            voter_id,
            password,
            email,
            name,
            city
        };

        axiosMethods.post('/register', body)
            .then(response => {
                console.log(response);
            })
            .catch(error => {
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
        case 'REGISTER_USER': {
            this.registerUser(action.payload.user);
            break;
        }
        }
    }
}

const mainPageStore = new MainPageStore();
dispatcher.register(mainPageStore.handleActions.bind(mainPageStore));
export default mainPageStore;
