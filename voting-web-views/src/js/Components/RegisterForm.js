import React from 'react';

import * as MainPageActions from './../Actions/mainPageActions.js';

export default class RegisterForm extends React.Component {
    formSubmit () {
        const username = document.getElementById('username').value;
        const password = document.getElementById('password').value;
        const email = document.getElementById('email').value;
    }

    toggleLoggingInState () {
        MainPageActions.toggleLoggedInState();
    }

    render () {
        return (
            <div class="card wow fadeInRight" data-wow-duration="2.5s">
                <div class="card-block">
                    <div id="form-header">
                        <i onClick={this.toggleLoggingInState.bind(this)} id="left-arrow" class="fa fa-2x fa-arrow-circle-left refix"></i>
                        <h3 id="register-header-text" class="text-center">Register:</h3>
                    </div>
                    <hr/>
                    <div class="md-form">
                        <i class="fa fa-user prefix"></i>
                        <input type="text" id="username" class="form-control"/>
                        <label for="form3">Voter ID</label>
                    </div>
                    <div class="md-form">
                        <i class="fa fa-user prefix"></i>
                        <input type="text" id="username" class="form-control"/>
                        <label for="form3">Your name</label>
                    </div>
                    <div class="md-form">
                        <i class="fa fa-user prefix"></i>
                        <input type="text" id="username" class="form-control"/>
                        <label for="form3">City</label>
                    </div>
                    <div class="md-form">
                        <i class="fa fa-envelope prefix"></i>
                        <input type="email" id="email" class="form-control"/>
                        <label for="form2">Your email</label>
                    </div>

                    <div class="md-form">
                        <i class="fa fa-lock prefix"></i>
                        <input type="password" id="password" class="form-control"/>
                        <label for="form4">Your password</label>
                    </div>

                    <div class="text-center">
                        <button onClick={this.formSubmit.bind(this)} class="btn btn-danger btn-lg">Sign up</button>
                    </div>

                </div>
            </div>
        );
    }
}
