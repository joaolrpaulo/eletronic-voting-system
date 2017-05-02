import { EventEmitter } from 'events';

import dispatcher from './../Utils/dispatcher.js';
import { axiosMethods } from './../Utils/configs.js';

class VotingPageStore extends EventEmitter {
    constructor () {
        super();
        this.polls = [];
    }

    retrievePolls () {
        axiosMethods.get('/polls')
            .then((response) => {
                this.polls = response.data;
                this.emit('change');
            })
            .catch((error) => {
                console.log(error);
            });
    }

    getAll () {
        return this.polls;
    }

    handleActions (action) {
        switch (action.type) {
        case 'RETRIEVE_POLLS': {
            this.retrievePolls();
            break;
        }
        }
    }
}

const votingPageStore = new VotingPageStore();
dispatcher.register(votingPageStore.handleActions.bind(votingPageStore));
export default votingPageStore;
