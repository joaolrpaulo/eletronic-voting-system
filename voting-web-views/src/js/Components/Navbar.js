import React from 'react';

export default class Navbar extends React.Component {
    render() {
        return (
                <nav class="navbar navbar-toggleable-md navbar-dark fixed-top scrolling-navbar">
                    <div class="container">
                        <button class="navbar-toggler navbar-toggler-right" type="button" data-toggle="collapse" data-target="#navbarNav1" aria-controls="navbarNav1" aria-expanded="false" aria-label="Toggle navigation">
                            <span class="navbar-toggler-icon"></span>
                        </button>
                        <a class="navbar-brand" href="#">
                            <strong>Navbar</strong>
                        </a>
                        <div class="collapse navbar-collapse" id="navbarNav1">
                            <ul class="navbar-nav mr-auto">
                                <li class="nav-item active">
                                    <a class="nav-link">Home <span class="sr-only">(current)</span></a>
                                </li>
                                <li class="nav-item">
                                    <a class="nav-link" href="#about">About</a>
                                </li>
                                <li class="nav-item">
                                    <a class="nav-link" href="#best-features">Features</a>
                                </li>
                                <li class="nav-item">
                                    <a class="nav-link" href="#contact">Contact</a>

                                </li>
                            </ul>
                            <form class="form-inline waves-effect waves-light">
                                <input class="form-control" type="text" placeholder="Search"/>
                            </form>
                        </div>
                    </div>
                </nav>
        )
    }
}
