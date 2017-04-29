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

    render () {
        return (
            <div class="card wow fadeInRight" data-wow-duration="2.5s">
                <div class="card-block">
                    <div class="text-center">
                        <h3><i class="fa fa-user"></i> Login:</h3>
                        <hr/>
                    </div>
                    <div class="md-form">
                        <i class="fa fa-user prefix"></i>
                        <input type="text" id="form3" class="form-control"/>
                        <label for="form3">Your username</label>
                    </div>
                    <div class="md-form">
                        <i class="fa fa-lock prefix"></i>
                        <input type="password" id="form4" class="form-control"/>
                        <label for="form4">Your password</label>
                    </div>

                    <div class="text-center">
                        <button class="btn btn-primary btn-rounded btn-lg">Login</button>
                        <br/>
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
