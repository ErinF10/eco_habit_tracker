import React from "react";
import Navbar from "../components/common/navbar";
import Header from "../components/common/header";

const Profile = () => {
    return (
        <div>
            <div className="navbar-container">
                <Navbar />
            </div>
            <div className="main-content">
                <div className="header-container">
                    <Header page='Profile' />
                </div>
                <p>content</p>
            </div>
        </div>

    )
}

export default Profile;