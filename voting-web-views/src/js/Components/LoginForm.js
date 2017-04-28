import React from 'react';

export default class LoginForm extends React.Component {
    render() {
        return (
            <div class="login-form">
                <h1>Electronic Voting System</h1>
                <div class="form-group ">
                    <input type="text" class="form-control" placeholder="Username " id="UserName"/>
                    <i class="fa fa-user"></i>
                </div>
                <div class="form-group log-status">
                    <input type="password" class="form-control" placeholder="Password" id="Passwod"/>
                    <i class="fa fa-lock"></i>
                </div>
                <span class="alert">Invalid Credentials</span>
                <a class="link" href="#">Lost your password?</a>
                <button type="button" class="log-btn">Log in</button>
            </div>
        );
    }
}
