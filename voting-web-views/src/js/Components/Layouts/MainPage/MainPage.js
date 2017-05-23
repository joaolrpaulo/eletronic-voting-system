import React from 'react';
import { hashHistory } from 'react-router';
import NodeRSA from 'node-rsa';

import MainPageStore from 'Stores/mainPageStore.js';
import User from 'Models/User.js';
import MainPageTemplate from './MainPage.rt';
import { SERVER_PUBLIC_KEY, SERVER_PRIVATE_KEY } from 'Utils/globals.js';

export default class MainPage extends React.Component {
    constructor () {
        super();

        this.state = {
            loggingIn: true
        };
    }

    componentWillMount () {
        if (sessionStorage.getItem ('token') != null) {
            User.setToken(sessionStorage.getItem('token')).toggleLoggedIn();
            hashHistory.push('/voting');
        }

        /* const key = new NodeRSA(SERVER_PRIVATE_KEY);
         * key.importKey(SERVER_PUBLIC_KEY, 'pkcs8');
         * const text = 'Hello RSA!';
         * var encrypted = key.encrypt(text);
         * console.log('encrypted: ', encrypted);
         * var decrypted = key.decrypt(encrypted, 'utf8');
         * console.log('decrypted: ', decrypted);*/
        /* encrypt.setPublicKey(SERVER_PUBLIC_KEY);
         * const encrypted = encrypt.encrypt('Hello World!');
         * console.log('ENCRYPTION', encrypted);*/

        MainPageStore.on('change', this.getLoggingInState.bind(this));
    }

    componentWillUnmount () {
        MainPageStore.removeListener('change', this.getLoggingInState.bind(this));
    }

    getLoggingInState () {
        this.setState({
            loggingIn: MainPageStore.getLoggingInState()
        });
    }
}

MainPage.prototype.render = MainPageTemplate;
