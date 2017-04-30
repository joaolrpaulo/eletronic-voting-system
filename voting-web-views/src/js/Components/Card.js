import React from 'react';
import axios from 'axios';

import { axiosConfig } from './../configs.js';
import User from './../User.js';

export default class Card extends React.Component {
    request () {
        axios.get(axiosConfig.baseUrl + '/user', axiosConfig.get(User.getToken()))
             .then((response) => {
                 console.log(response);
             })
             .catch((error) => {
                 console.log(error);
             });
    }

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
                    <h4 class="card-title">
                        <p class="poll-name" data-toggle="collapse" data-target="#collapseExample" aria-expanded="false" aria-controls="collapseExample">Eleições Democráticas</p>
                    </h4>
                    <div class="collapse" id="collapseExample">
                        <div class="card card-block scrollable">
                            Anim pariatur cliche reprehenderit, enim eiusmod high life accusamus terry richardson ad squid. Nihil anim keffiyeh helvetica, craft beer labore wes anderson cred nesciunt sapiente ea proidentsdcsdcdsjkncdjkns dcnjksdnkjdsilcds. kjnk. Anim pariatur cliche reprehenderit, enim eiusmod high life accusamus terry richardson ad squid. Nihil anim keffiyeh helvetica, craft beer labore wes anderson cred nesciunt sapiente ea proidentsdcsdcdsjkncdjkns dcnjksdnkjdsilcds.
                        </div>
                    </div>
                    <br/>
                    <button type="button" class="btn btn-primary waves-effect waves-light" data-toggle="modal" data-target="#fullHeightModalRight">Large Modal</button>
                    <div class="modal fade right" id="fullHeightModalRight" role="dialog" tabindex="-1" aria-labelledby="myModalLabel" aria-hidden="true">
                        <div class="modal-dialog modal-full-height modal-right" role="document">
                            <div class="modal-content">
                                <div class="modal-header">
                                    <button type="button" class="close" data-dismiss="modal" aria-label="Close">
                                        <span aria-hidden="true">×</span>
                                    </button>
                                    <h4 class="modal-title w-100" id="myModalLabel">Modal title</h4>
                                </div>
                                <div class="modal-body">
                                    <p>Lorem ipsum dolor sit amet, consectetur adipisicing elit. Sapiente magnam, sunt, ea dolore eum quod. Minima fugiat enim aut soluta est reprehenderit reiciendis quos, qui, amet possimus laborum assumenda voluptate.
                                    </p>

                                    <ul class="list-group z-depth-0">
                                        <li class="list-group-item justify-content-between">
                                            Cras justo odio
                                            <span class="badge badge-primary badge-pill">14</span>
                                        </li>
                                        <li class="list-group-item justify-content-between">
                                            Dapibus ac facilisis in
                                            <span class="badge badge-primary badge-pill">2</span>
                                        </li>
                                        <li class="list-group-item justify-content-between">
                                            Morbi leo risus
                                            <span class="badge badge-primary badge-pill">1</span>
                                        </li>
                                        <li class="list-group-item justify-content-between">
                                            Cras justo odio
                                            <span class="badge badge-primary badge-pill">14</span>
                                        </li>
                                        <li class="list-group-item justify-content-between">
                                            Dapibus ac facilisis in
                                            <span class="badge badge-primary badge-pill">2</span>
                                        </li>
                                        <li class="list-group-item justify-content-between">
                                            Morbi leo risus
                                            <span class="badge badge-primary badge-pill">1</span>
                                        </li>
                                    </ul>

                                </div>
                                <div class="modal-footer">
                                    <button type="button" class="btn btn-secondary waves-effect waves-light" data-dismiss="modal">Close</button>
                                    <button type="button" class="btn btn-primary waves-effect waves-light">Save changes</button>
                                </div>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        );
    }
}
