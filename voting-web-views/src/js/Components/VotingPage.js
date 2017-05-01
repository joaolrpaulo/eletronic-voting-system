import React from 'react';

import Card from './Card.js';
import VotingPageStore from './../Stores/votingPageStore.js';
import * as VotingPageActions from './../Actions/votingPageActions.js';

export default class VotingPage extends React.Component {
    constructor () {
        super();
        this.state = {
            polls: []
        };
        VotingPageActions.retrievePolls();
    }

    componentWillMount () {
        VotingPageStore.on('change', this.getAll.bind(this));
    }

    componentWillUnmount () {
        VotingPageStore.removeListener('change', this.getAll.bind(this));
    }

    getAll () {
        this.setState({
            polls: VotingPageStore.getPolls()
        });
        console.log('changed polls', this.state.polls);
    }

    render () {
        const polls = this.state.polls.map(poll => {
            return <Card/>;
        });

        return (
            <div class="content nimvelo">
                <div class="row container container-cards margin-top">
                    {polls}
                </div>
            </div>
        );
    }
}
