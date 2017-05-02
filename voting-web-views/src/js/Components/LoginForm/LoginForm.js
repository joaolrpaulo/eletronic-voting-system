import React from 'react';

import * as MainPageActions from './../../Actions/mainPageActions.js';
import LoginFormTemplate from './LoginForm.rt';

export default class RegisterForm extends React.Component {
    constructor () {
        super();
        this.clicked = false;
    }

    toggleForm () {
        this.clicked = !this.clicked;
        MainPageActions.toggleLoggedInState();
    }

    getClickedRegister () {
        return this.clicked;
    }

    formSubmit (ev) {
        const voterId = document.getElementById('voterId').value;
        const password = document.getElementById('password').value;

        MainPageActions.logInUser(voterId, password);
    }
}

RegisterForm.prototype.render = LoginFormTemplate;
