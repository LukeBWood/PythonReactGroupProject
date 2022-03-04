import React from 'react'
import { Card, CardBody, CardTitle, CardText, Button } from 'reactstrap';

const UserCard = props => {
    return (
        <div className="feedback_card sec__one">
          <Card>
            <CardBody>
               <CardText>
                 {props.feedback}
                 <p>Rating: { props.rating ? props.rating : '-' } /5.</p>
                 
               </CardText>
            </CardBody>
          </Card>
        </div>
    )
}

export default UserCard;