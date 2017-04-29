import React from 'react';

import Card from './Card.js';

export default class VotingPage extends React.Component {
    render () {
        return (
            <div class="nimvelo">
                <div class="container">
                    <div class="row">
                        <Card/>
                    </div>
                </div>
            </div>
        );
    }
}
