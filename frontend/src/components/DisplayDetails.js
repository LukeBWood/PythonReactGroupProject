import React, { useState, useEffect } from 'react';
import axios from "axios";
import boolToStr from "./BoolToStringNice";
import UserCard from "./UserCard";

const MyDetails = props => {
    const [userDetails, setUserDetails] = useState([]);

    useEffect(() => {
        const fetchUserDetails = async () => {
            try {
                const response = await axios({
                    method: "GET",
                    url: `http://localhost:8000/userdetails/?user_id=${props.userId}`,
                    headers: {
                        "Content-Type": "application/json"
                    }
                });
                setUserDetails(response.data);
            } catch (error) {
                console.log(error);
            }
        };
        fetchUserDetails();
    }, []);

    if (userDetails) {
        console.log(userDetails.is_active);
    }

    return (
        <div className="display_details sec__one">
            <h1>My Details</h1>
            <UserCard
                id={userDetails.id}
                firstName={userDetails.first_name}
                lastName={userDetails.last_name}
                email={userDetails.email}
                businessArea={userDetails.profile ? userDetails.profile.business_area.name : ""}
                active={userDetails ? boolToStr(userDetails.is_active): ""}
                admin={userDetails.profile ? boolToStr(userDetails.profile.is_admin) : ""}
                mentee={userDetails.profile ? boolToStr(userDetails.profile.is_mentee) : ""}
                mentor={userDetails.profile ? boolToStr(userDetails.profile.is_mentor) : ""}
                topicsOfInterest={userDetails.profile ? userDetails.profile.topics_of_interest.map(topic => topic.skill.name) : []}
                topicsOfExpertise={userDetails.profile ? userDetails.profile.topics_of_expertise.map(topic => topic.skill.name) : []}
            />
        </div>
    );
}

export default MyDetails;