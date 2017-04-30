import React from 'react';
import { browserHistory } from 'react-router';

import User from './../User.js';

export default class PrivateAreaComponent extends React.Component {
    componentDidMount () {
        const { currentUrl } = this.props;
        console.log('user is not logged in', User.isLoggedIn);

        if (!User.isLoggedIn) {
            browserHistory.replace('/');
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
