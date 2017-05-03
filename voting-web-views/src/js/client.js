import React from 'react';
import ReactDOM from 'react-dom';
import { IndexRoute, Router, hashHistory, Route } from 'react-router';

import 'Styles/styles.scss';

import Navbar from 'Components/Navbar/Navbar.js';
import MainPage from 'Components/Layouts/MainPage/MainPage.js';
import VotingPage from 'Components/Layouts/VotingPage/VotingPage.js';
import PrivateAreaComponent from 'Components/AuthComponent/PrivateAreaComponent.js';

import { init } from 'Utils/configs.js';
init();

export default class Layout extends React.Component {
    render () {
        return (
            <div>
                <Navbar/>
                {this.props.children}
            </div>
        );
    }
}

const app = document.getElementById('app');
ReactDOM.render(
    <Router history={hashHistory}>
        <Route path='/' component={Layout}>
            <IndexRoute component={MainPage}/>
            <Route component={PrivateAreaComponent}>
                <Route path='voting' component={VotingPage}/>
            </Route>
        </Route>
        <Route path="*" component={MainPage}/>
    </Router>,
    app);
