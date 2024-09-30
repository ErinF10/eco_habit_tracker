import React from "react";
import Navbar from "../components/common/navbar";
import Header from "../components/common/header";

const ManageHabits = () => {
    return (
        <div>
            <div className="navbar-container">
                <Navbar />
            </div>
            <div className="main-content">
                <div className="header-container">
                    <Header page='Manage Habits' />
                </div>
                <p>content</p>
            </div>
        </div>
    )
}

export default ManageHabits;