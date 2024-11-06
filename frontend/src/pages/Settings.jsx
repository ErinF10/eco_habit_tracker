import React from "react";
import Navbar from "../components/common/navbar";
import Header from "../components/common/header";
import ProfileInfo from "../components/profile/ProfileInfo";
import '../styles/settings.css';

const Settings = () => {
    return (
        <div className="settings">
        <div className="navbar-container">
            <Navbar />
        </div>
        <div className="header-container">
            <Header page='Settings' />
        </div>
        <div className="main-content">
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
                    </div>

                </div>
                <button className="delete">Delete Profile</button>
            </div>
        </div>
    </div>
    )
}

export default Settings;