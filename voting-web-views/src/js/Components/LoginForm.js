import React from 'react';

import * as MainPageActions from './../Actions/mainPageActions.js';

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
        const username = document.getElementById('username').value;
        const password = document.getElementById('password').value;

        MainPageActions.logInUser(username, password);
    }

    render () {
        return (
            <div class="card submission-forms" data-wow-duration="2.5s">
                <div class="card-block">
                    <div class="text-center">
                        <h3>Login</h3>
                        <hr/>
                    </div>
                        <span class="glyphicon glyphicon-star" aria-hidden="true">aaa</span>
                    <div class="md-form">
                        <i class="fa fa-user prefix"></i>
                        <input type="text" id="username" class="form-control"/>
                        <label for="form3">Your username</label>
                    </div>
                    <div class="md-form">
                        <i class="fa fa-lock prefix"></i>
                        <input type="password" id="password" class="form-control"/>
                        <label for="form4">Your password</label>
                    </div>

                    <div class="text-center">
                        <button onClick={this.formSubmit.bind(this)} class="btn btn-primary btn-rounded btn-lg waves-effect">Login</button>
                        <br/>
                        <fieldset class="form-group">
                            <button onClick={this.toggleForm.bind(this)} class="btn btn-danger btn-lg waves-effect">Sign Up</button>
                        </fieldset>
                    </div>

                </div>
            </div>
        );
    }
}
