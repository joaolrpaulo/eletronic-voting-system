import React from 'react';
import { hashHistory } from 'react-router';

import MainPageStore from 'Stores/mainPageStore.js';
import User from 'Models/User.js';
import MainPageTemplate from './MainPage.rt';

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
