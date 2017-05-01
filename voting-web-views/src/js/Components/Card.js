import React from 'react';

export default class Card extends React.Component {
    render () {
        return (
            <div class="card voting-card">
                <div class="view overlay hm-white-slight">
                    <img src="https://mdbootstrap.com/img/Photos/Horizontal/Nature/4-col/img%20%287%29.jpg" class="img-fluid round-image" alt=""/>
                    <a href="#">
                        <div class="mask waves-effect waves-light"></div>
                    </a>
                </div>

                <div class="card-block">
                    <h4 class="card-title">Card title</h4>
                    <p class="card-text">Some quick example text to build on the card title and make up the bulk of the card's content.</p>
                    <a href="#" class="btn btn-primary">Button</a>
                </div>
            </div>
        );
    }
}
