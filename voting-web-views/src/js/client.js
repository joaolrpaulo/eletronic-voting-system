import React from 'react';
import ReactDOM from 'react-dom';

import './../styles/styles.scss';

import Navbar from './Components/Navbar.js';
import LoginForm from "./Components/LoginForm.js";

export default class Layout extends React.Component {
    render() {
        return (
            <div>
                <Navbar/>
                <div class="view hm-black-strong">
                    <div class="full-bg-img flex-center">
                        <LoginForm/>
                    </div>
                </div>
            </div>
        );
    }
}

ReactDOM.render(<Layout/>, document.getElementById('app'));
