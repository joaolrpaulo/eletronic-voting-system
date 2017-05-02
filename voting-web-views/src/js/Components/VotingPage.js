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
    }

    componentWillMount () {
        VotingPageStore.on('change', this.getAll.bind(this));
        VotingPageActions.retrievePolls();
    }

    componentWillUnmount () {
        VotingPageStore.removeListener('change', this.getAll.bind(this));
    }

    getAll () {
        this.setState({
            polls: VotingPageStore.getAll()
        });
    }

    render () {
        const polls = this.state.polls.map(poll => {
            return <Card
                       key={poll.id}
                       title={poll.title}
                       description={poll.description}
                       imgSrc="https://mdbootstrap.com/img/Photos/Horizontal/Nature/4-col/img%20%287%29.jpg"
                   />;
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
