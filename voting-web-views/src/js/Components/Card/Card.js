import React from 'react';

import { axiosMethods } from 'Utils/configs.js';
import CardTemplate from './Card.rt';

export default class Card extends React.Component {
    request () {
        axiosMethods.get('/user')
             .then((response) => {
                 console.log(response);
             })
             .catch((error) => {
                 console.log(error);
             });
    }
}

Card.prototype.render = CardTemplate;
