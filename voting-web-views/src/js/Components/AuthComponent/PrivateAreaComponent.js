import React from 'react';
import { hashHistory } from 'react-router';

import User from './../../Models/User.js';

export default class PrivateAreaComponent extends React.Component {
    componentDidMount () {
        if (!User.isLoggedIn) {
            hashHistory.push('/');
        }
    }

    render () {
        if (User.isLoggedIn) {
            return this.props.children;
        } else {
            return null;
        }
    }
}
