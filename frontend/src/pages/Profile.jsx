import React from "react";
import Navbar from "../components/common/navbar";
import Header from "../components/common/header";
import ProfileInfo from "../components/profile/ProfileInfo";
import '../styles/profile.css'

const Profile = () => {
    return (
        <div className="profile">
            <div className="navbar-container">
                <Navbar />
            </div>
            <div className="header-container">
                <Header page='Profile' />
            </div>

            <div className="main-content">
                
                <div className="profile-information-container">

                    <h2>Personal Information</h2>

                    <div className="profile-settings">

                        <div className="profile-picture-settings">
                            <img src='' alt='Profile Picture'></img>
                            <button>Update Picture</button>
                        </div>

                        <div className="profile-info-settings">

                            <div className="top">
                                <h2>Profile</h2>
                                <button className="edit">Edit</button>
                            </div>

                            <div className="profile-info-container">
                                <ProfileInfo field='Username' contents='ErinForrest10' />
                                <ProfileInfo field='Name' contents='Erin Forrest'/>
                                <ProfileInfo field='Pronouns' contents='She/Her'/>
                                <ProfileInfo field='Location' contents='None'/>
                                <ProfileInfo field='Job Title' contents='None' />
                            
                            </div>
                            
                        </div>
                    </div>
                    
                    <div className="contact-settings">

                        <div className="top">
                            <h2>Contact Information</h2>
                            <button className="edit">Edit</button>
                        </div>

                        <div className="profile-info-container">
                            <ProfileInfo field='Email Address' contents='erinforrest11@gmail.com'/>
                            <ProfileInfo field='Phone Number' contents='None'/>
                        </div>
                        
                    </div>
                </div>
            </div>
        </div>

    )
}

export default Profile;