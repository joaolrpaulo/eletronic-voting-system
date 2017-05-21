import React from 'react';

import CardTemplate from './Card.rt';

export default class Card extends React.Component {
    vote() {
        const radioButtons = document.getElementsByClassName('radio_button');
        for (let i = 0; i < radioButtons.length; i++) {
            if (radioButtons[i].checked) {
                console.log(radioButtons[i].value);
            }
        }
    }
}
Card.prototype.render = CardTemplate;
