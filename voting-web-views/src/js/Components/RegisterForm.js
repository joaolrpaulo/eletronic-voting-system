import React from 'react';

export default class RegisterForm extends React.Component {
    render () {
        return (
            <div class="card wow fadeInRight" data-wow-duration="2.5s">
                <div class="card-block">
                    <div class="text-center">
                        <h3><i class="fa fa-user"></i> Register:</h3>
                        <hr/>
                    </div>
                    <div class="md-form">
                        <i class="fa fa-user prefix"></i>
                        <input type="text" id="form3" class="form-control"/>
                        <label for="form3">Your name</label>
                    </div>
                    <div class="md-form">
                        <i class="fa fa-envelope prefix"></i>
                        <input type="text" id="form2" class="form-control"/>
                        <label for="form2">Your email</label>
                    </div>

                    <div class="md-form">
                        <i class="fa fa-lock prefix"></i>
                        <input type="password" id="form4" class="form-control"/>
                        <label for="form4">Your password</label>
                    </div>

                    <div class="text-center">
                        <button class="btn btn-danger btn-lg">Sign up</button>
                    </div>

                </div>
            </div>
        );
    }
}
