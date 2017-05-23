import React from 'react';

import CardTemplate from './Card.rt';
import { axiosMethods } from 'Utils/configs.js';

export default class Card extends React.Component {
    constructor () {
        super();

        this.state = {
            modalIsOpen: false
        };
    }

    vote() {
        const radioButtons = document.getElementsByClassName('radio_button');
        for (let i = 0; i < radioButtons.length; i++) {
            if (radioButtons[i].checked) {
                const body = {};
                axiosMethods.post('/vote/' + radioButtons[i].id, body)
                            .then(response => {
                                swal('Good job!', 'You clicked the button!', 'success');
                            })
                            .catch(error => {
                                switch (error.response.status) {
                                    case 403: {
                                        swal('Error', 'You can only vote once for each poll', 'error');
                                    }
                                }
                            });
                break;
            }
        }
        this.setState({
            modalIsOpen: false
        });
    }

    toggleModal () {
        this.setState({
            modalIsOpen: !this.state.modalIsOpen
        });
    }
}
Card.prototype.render = CardTemplate;
