import React from "react";
import Navbar from "../components/common/Navbar";
import Header from "../components/common/Header";
import CompletionIcon from "../components/dashboard/CompletionIcon";
import '../styles/dashboard.css'
import { Link } from "react-router-dom";
import { useState, useEffect } from "react";
import { useUser } from "@clerk/clerk-react";
import api from "../api";
import { useCurrentUser } from "../UserContext";


const Dashboard = () => {
    const [habits, setHabits] = useState([]);
    const [streak, setStreak] = useState(0);
    const [bestStreak, setBestStreak] = useState(0);
    const [completedHabits, setCompletedHabits] = useState({});

    const { currentUser } = useCurrentUser();


    useEffect(() => {
        const fetchUserData = async () => {
            if (currentUser) {
                try {
                    const userStreak = await api.get(`/userstreaks/${currentUser.id}`);
               
        
                    if (currentUser && currentUser.id) {
                        const response = await api.get(`/userhabits/${currentUser.id}`);
                        console.log('Habits Response:', response.data);
                        
                        if (response.data && Array.isArray(response.data)) {
                            setHabits(response.data);
                        } else {
                            console.error("Unexpected response format:", response.data);
                        }
                    } else {
                        console.warn('No valid user ID to fetch habits');
                    }
                    
                    setStreak(userStreak.data.current_streak);
                    setBestStreak(userStreak.data.best_streak);
                } catch (error) {
                    console.error("Error fetching user data:", error);
                    console.error("Error Details:", error.response?.data);
                }
            }
        };
        fetchUserData();
    }, [currentUser]);

    const handleHabitToggle = (habitId) => {
        setCompletedHabits(prev => ({
            ...prev,
            [habitId]: !prev[habitId]
        }));
    };

    const handleSubmit = (e) => {
        e.preventDefault();
        // Here you would typically send the completed habits to your backend
        console.log('Completed habits:', completedHabits);
        // Add API call to update completed habits in the backend
    };

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
                        {habits && habits.length > 0 ? (
                            <form onSubmit={handleSubmit}>
                                <ul>
                                    {habits.map((habit) => (
                                        <li key={habit.id}>
                                            <label>
                                                <input
                                                    type="checkbox"
                                                    checked={completedHabits[habit.id] || false}
                                                    onChange={() => handleHabitToggle(habit.id)}
                                                />
                                                {habit.description}
                                            </label>
                                        </li>
                                    ))}
                                </ul>
                                <button type="submit">Save</button>
                            </form>
                        ) : (
                            <p>No habits for today</p>
                        )}
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
                            <h1>{streak} days</h1>
                            <p>Top streak: {bestStreak} days</p>
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

                    <p>You’re <strong>{bestStreak - streak}</strong> days away from a new record!</p>
                </div>
            </div>
            
        </div>
    )
}

export default Dashboard;