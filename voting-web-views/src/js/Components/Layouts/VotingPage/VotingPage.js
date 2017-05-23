import React from 'react';

import Card from 'Components/Card/Card.js';
import VotingPageStore from 'Stores/votingPageStore.js';
import * as VotingPageActions from 'Actions/votingPageActions.js';
import VotingPageTemplate from './VotingPage.rt';

export default class VotingPage extends React.Component {
    constructor () {
        super();
        this.state = {
            polls: [],
            pollsHtml: []
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
        const polls = VotingPageStore.getAll();
        const pollsHtml = polls.map(poll => {
            return <Card
                       key={poll.poll_id}
                       title={poll.title}
                       description={poll.description}
                       imgSrc="https://mdbootstrap.com/img/Photos/Horizontal/Nature/4-col/img%20%287%29.jpg"
                       items={poll.items}
                   />;
        });

        this.setState({
            polls,
            pollsHtml
        });
    }
}

VotingPage.prototype.render = VotingPageTemplate;
