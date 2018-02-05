import React from 'react';
import PropTypes from 'prop-types';
import { Modal, Button  } from '@edx/paragon/static';

import ExperimentalCarousel from './ExperimentalCarousel.jsx';

// https://openedx.atlassian.net/browse/LEARNER-3926

export class PortfolioExperimentUpsellModal extends React.Component {
    constructor(props) {
        super(props);

        this.state = { isOpen: true };
    }

    render() {
        const slides = [
            (<div className='portfolio-slide-0'>
                <div className='slide-header'>You will soon have your new coding skills! After your course, Portfolio Builder introduces a guide to creating your first project and setting up your portfolio if you're new to Tech. By following the guide you will:</div>
                <ul className='upsell-modal-checkmark-group'>
                    <li><span className='fa fa-check upsell-modal-checkmark' aria-hidden='true' />Use your new coding skills</li>
                    <li><span className='fa fa-check upsell-modal-checkmark' aria-hidden='true' />Begin to build your portfolio</li>
                    <li><span className='fa fa-check upsell-modal-checkmark' aria-hidden='true' />Share what you can do!</li>
                </ul>
            </div>),
            (<div className='portfolio-slide-1'>
                <div className='slide-header'><b>Use Your New Coding Skills</b></div>
                <span>Want to practice what you've learned? We'll give you the idea, and you build it and make it your own. Get creative!</span>
            </div>),
            (<div className='portfolio-slide-2'>
                <div className='slide-header'><b>Build Your Portfolio</b></div>
                <span>Make your practice worth more. The project idea will make the perfect first item to add to your new Tech portfolio. Show them you can code.</span>
            </div>),
            (<div className='portfolio-slide-3'>
                <div className='slide-header'><b>Share What You Can Do</b></div>
                <span>Get tips on where to store your project how best to share it with employers.</span>
            </div>),
        ];

        const body = (
            <div>
                <ExperimentalCarousel id='portfolio-upsell-modal' slides={slides} />
                <img
                    className="upsell-certificate"
                    src="https://courses.edx.org/static/images/edx-verified-mini-cert.png"
                    alt=""
                />
            </div>
        );

        return (
            <Modal
                open={this.state.isOpen}
                className='portfolio-upsell-modal'
                title={'Portfolio Builder: My First Project'}
                onClose={() => {}}
                body={body}
                buttons={[
                    (<Button
                        label={'Upgrade ($100 USD)'}
                        display={'Upgrade ($100 USD)'}
                        buttonType='success'
                        // unfortunately, Button components don't have an href attribute
                        onClick={() => {}}
                    />),
                ]}
            />
        );
    }
}
