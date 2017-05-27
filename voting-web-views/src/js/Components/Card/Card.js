import React from 'react';
import srs from 'secure-random-string';

import CardTemplate from './Card.rt';
import { axiosMethods } from 'Utils/configs.js';
import { SERVER_PUBLIC_KEY } from 'Utils/globals';

export default class Card extends React.Component {
    constructor () {
        super();

        this.state = {
            modalIsOpen: false,
            identifier: null
        };
    }

    generateObject () {
        const radioButtons = document.getElementsByClassName('radio_button');
        const encrypt = new JSEncrypt();
        encrypt.setPublicKey(SERVER_PUBLIC_KEY);

        const voteId = this.getVoteId();
        const item = radioButtons[voteId].id;
        const identifier = srs({ length: 128 });
        let encryptedObject = {
            item,
            identifier
        };
        this.setState({ identifier });
        encryptedObject = JSON.stringify(encryptedObject);
        encryptedObject = encrypt.encrypt(encryptedObject);
        return encryptedObject;
    }

    getVoteId () {
        const radioButtons = document.getElementsByClassName('radio_button');
        let voteId = -1;
        for (let i = 0; i < radioButtons.length; i++) {
            if (radioButtons[i].checked) {
                voteId = i;
                break;
            }
        }
        return voteId;
    }

    voteIsAcceptable () {
        const voteId = this.getVoteId();
        if (voteId === -1) {
            return false;
        }
        return true;
    }

    vote() {
        if (!this.voteIsAcceptable()) {
            swal('Error', 'You must choose a party', 'error');
            return;
        }

        const body = {
            message: this.generateObject()
        };
        axiosMethods.post('/vote/' + this.props.poll_id, body)
                    .then(response => {
                        setTimeout(() => {
                            swal('Good job!', 'You have successfully voted for this poll, your token is ' + this.state.identifier, 'success');
                            this.setState({
                                modalIsOpen: false
                            });
                        }, 1000);
                    })
                    .catch(error => {
                        setTimeout(() => {
                            swal('Error', 'An error occured while voting', 'error');
                        }, 1000);
                    });

    }

    toggleModal () {
        this.setState({
            modalIsOpen: !this.state.modalIsOpen
        });
    }
}
Card.prototype.render = CardTemplate;
