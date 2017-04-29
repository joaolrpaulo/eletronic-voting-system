import React from 'react';

import RegisterForm from './RegisterForm.js';
import LoginForm from './LoginForm.js';
import MainPageStore from './../Stores/mainPageStore.js';

export default class MainPage extends React.Component {
    constructor () {
        super();
        this.state = {
            loggingIn: true
        };
    }

    componentWillMount () {
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

    render () {
        return (
            <div class="view-fullscreen hm-black-strong">
                <div class="full-bg-img flex-center">
                    <div class="container">
                        <div class="row" id="home">
                            <div class="col-lg-6">
                                <div class="description">
                                    <h2 class="h2-responsive wow fadeInLeft">Electronic Voting System</h2>
                                    <hr class="hr-dark wow fadeInLeft"/>
                                    <p class="wow fadeInLeft" data-wow-duration="2.5s">Lorem ipsum dolor sit amet, consectetur adipisicing elit. Rem repellendus quasi fuga nesciunt dolorum nulla magnam veniam sapiente, fugiat! Commodi sequi non animi ea dolor molestiae, quisquam iste, maiores. Nulla.</p>
                                    <br/>
                                    <a class="btn btn-outline-white btn-lg wow fadeInLeft" data-wow-delay="0.7s">Learn more</a>
                                </div>
                            </div>
                            <div class="col-lg-6">
                                {
                                    (this.state.loggingIn)
                                    ? <LoginForm/>
                                    : <RegisterForm/>
                                }
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        );
    }
}
