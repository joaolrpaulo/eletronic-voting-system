import React from 'react';
import ReactDOM from 'react-dom';

import './../styles/styles.scss';

import Navbar from './Components/Navbar.js';
import MainPage from './Components/MainPage.js';
import VotingPage from './Components/VotingPage.js';

new WOW().init();

export default class Layout extends React.Component {
    render () {
        return (
            <div>
                <Navbar/>
                <VotingPage/>
            </div>
        );
    }
}

ReactDOM.render(<Layout/>, document.getElementById('app'));
