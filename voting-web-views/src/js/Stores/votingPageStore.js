import { EventEmitter } from 'events';
import axios from 'axios';

import dispatcher from './../dispatcher.js';
import { axiosConfig } from './../configs.js';
import User from './../User.js';

class VotingPageStore extends EventEmitter {
    constructor () {
        super();
        this.polls = [];
    }

    retrievePolls () {
        axios.get(axiosConfig.baseUrl + '/polls', axiosConfig.get(User.getToken()))
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
