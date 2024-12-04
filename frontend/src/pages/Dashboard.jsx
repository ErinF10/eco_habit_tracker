import React from "react";
import Navbar from "../components/common/Navbar";
import Header from "../components/common/Header";
import CompletionIcon from "../components/dashboard/CompletionIcon";
import '../styles/dashboard.css'
import { Link } from "react-router-dom";


const Dashboard = () => {
    return (
        <div className="dashboard">
            <div className="navbar-container">
                <Navbar />
            </div>
            <div className="header-container">
                <Header page='Dashboard' />
            </div>

            <div className="main-content">
                <div className="top-row">
                    <div className="todo-list">
                        <h1>Today's Todo's</h1>
                    </div>
                    <div className="button-container">
                        <Link to='/routine-survey'>
                            <button id='take-survey'>Take the Survey</button>
                        </Link>
                    </div>
                </div>
                
                <div className="analytics">
                    <div className="streaks-container">
                        <div className="current-streak-container">
                            <h2>Current Streak</h2>
                            <h1>12 days</h1>
                            <p>Previous Record: 20 days</p>
                        </div>
                        <div className="items-completed-container">
                            <h2>This Week</h2>
                            <h1>2/10 Habits Complete</h1>
                            <p>Last Week: 9/10 Habits Complete</p>
                        </div>
                        <p></p>
                    </div>
                    
                    <div className="progress-chart">
                        <h2>Weekly Progress</h2>
                        <div className="completion-icons">
                            <CompletionIcon day='M' completionStatus='complete'/>
                            <CompletionIcon day='T' completionStatus='partial'/>
                            <CompletionIcon day='W' completionStatus='complete'/>
                            <CompletionIcon day='T' completionStatus='incomplete'/>
                            <CompletionIcon day='F' completionStatus='complete'/>
                            <CompletionIcon day='S' completionStatus='unseen'/>
                            <CompletionIcon day='S' completionStatus='unseen'/>
                        </div>
                    </div>

                    <p>You’re <strong>8</strong> days away from a new record!</p>
                </div>
            </div>
            
        </div>
    )
}

export default Dashboard;