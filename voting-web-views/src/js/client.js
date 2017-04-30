import React from 'react';
import ReactDOM from 'react-dom';
import { IndexRoute, Router, hashHistory, Route } from 'react-router';

import './../styles/styles.scss';

import Navbar from './Components/Navbar.js';
import MainPage from './Components/MainPage.js';
import VotingPage from './Components/VotingPage.js';
import PrivateAreaComponent from './Components/PrivateAreaComponent';

new WOW().init();

window.onerror = function (msg, url, ln) {
    console.log('here');
    return true;
};

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
    </Router>,
    app);
