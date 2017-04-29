import React from 'react';

export default class Navbar extends React.Component {
    render () {
        return (
            <nav class="navbar navbar-toggleable-md navbar-dark fixed-top scrolling-navbar">
                <div class="container">
                    <button class="navbar-toggler navbar-toggler-right" type="button" data-toggle="collapse" data-target="#navbarNav1" aria-controls="navbarNav1" aria-expanded="false" aria-label="Toggle navigation">
                        <span class="navbar-toggler-icon"></span>
                    </button>
                    <a class="navbar-brand waves-effect waves-light" href="http://mdbootstrap.com/material-design-for-bootstrap/" target="_blank">EVS</a>
                    <div class="collapse navbar-collapse" id="navbarNav1">
                        <ul class="nav navbar-nav nav-flex-icons ml-auto">
                            <li class="nav-item">
                                <a class="nav-link"><i class="fa fa-facebook"></i></a>
                            </li>
                            <li class="nav-item">
                                <a class="nav-link"><i class="fa fa-twitter"></i></a>
                            </li>
                            <li class="nav-item">
                                <a class="nav-link"><i class="fa fa-instagram"></i></a>
                            </li>
                        </ul>
                    </div>
                </div>
            </nav>
        );
    }
}
