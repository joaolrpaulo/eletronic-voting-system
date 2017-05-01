import React from 'react';

import Card from './Card.js';

export default class VotingPage extends React.Component {
    constructor () {
        super ();
    }

    render () {
        return (
            <div class="content nimvelo">
                <div class="row container container-cards margin-top">
                    <Card/>
                    <Card/>
                    <Card/>
                    <Card/>
                    <Card/>
                    <Card/>
                    <Card/>
                    <Card/>
                    <Card/>
                </div>
            </div>
        );
    }
}
