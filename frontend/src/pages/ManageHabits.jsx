import React from "react";
import Navbar from "../components/common/Navbar";
import Header from "../components/common/Header";
import Habit from "../components/manage_habits/Habit";
import '../styles/manageHabits.css';

const ManageHabits = () => {
    return (
        <div className="manage-habits">
            <div className="navbar-container">
                <Navbar />
            </div>
            <div className="header-container">
                <Header page='Manage Habits' />
            </div>

            <div className="main-content">
                <div className="add-habit-container">
                    <h1>Add a New Habit</h1>
                    <div className="add-habit">
                        <input placeholder="Enter a new habit"></input>
                        <button>+ Add</button>
                    </div>
                </div>
                <div className="current-habits">
                    <h1>Current Habits</h1>
                    <Habit title='Take the subway'/>
                    <Habit title='Bring reusable bags to the store' />
                    <Habit title='Take a 15 minute shorter shower' />
                </div>
            </div>
        </div>
    )
}

export default ManageHabits;