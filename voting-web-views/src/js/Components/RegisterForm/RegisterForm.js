import React from 'react';

import * as MainPageActions from './../../Actions/mainPageActions.js';
import RegisterFormTemplate from './RegisterForm.rt';

export default class RegisterForm extends React.Component {
    formSubmit () {
        const user = {
            voter_id: document.getElementById('voter_id').value,
            name: document.getElementById('name').value,
            city: document.getElementById('city').value,
            password: document.getElementById('password').value,
            email: document.getElementById('email').value
        };

        MainPageActions.registerUser(user);
    }

    toggleLoggingInState () {
        MainPageActions.toggleLoggedInState();
    }
}

RegisterForm.prototype.render = RegisterFormTemplate;
