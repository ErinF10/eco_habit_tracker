import React, { useState, useEffect } from "react";
import Navbar from "../components/common/Navbar";
import Header from "../components/common/Header";
import CompletionIcon from "../components/dashboard/CompletionIcon";
import '../styles/dashboard.css';
import { Link } from "react-router-dom";
import api from "../api";
import { useCurrentUser } from "../UserContext";
import { useUserHabits } from "../UserHabitContext";

const Dashboard = () => {
    const {userHabits, setUserHabits} = useUserHabits();
    const { currentUser } = useCurrentUser();

    // const [habits, setHabits] = useState([])
    const [streak, setStreak] = useState(0);
    const [bestStreak, setBestStreak] = useState(0);
    // const [completedUserHabits, setCompletedUserHabits] = useState({});
    const [todayHabits, setTodayHabits] = useState([]);

    useEffect(() => {
        const fetchUserData = async () => {
            if (currentUser) {
                try {
                    const userStreak = await api.get(`/userstreaks/${currentUser.id}`);
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

    

    // const getTodayHabits = async () => {
    //     if (!currentUser) return [];
    //     try {
    //         const schedulesResponse = await api.get(`/user-habit-schedules/${currentUser.id}`);
    //         const schedules = schedulesResponse.data;
    //         return userHabits.filter(userHabit => {
    //             const schedule = schedules.find(schedule => schedule.user_habit_id === userHabit.id);
    //             console.log(`Checking habit ${userHabit.id}:`, schedule);
    //             return schedule && schedule[currentDay];
    //         });
    //     } catch (error) {
    //         console.error("Error fetching user habit schedules:", error);
    //         return [];
    //     }
    // };

    // useEffect(() => {
    //     const getHabitDescriptions = async () => {
    //         if (todayHabits) {
    //             const response = await api.get(`/habit/${todayHabits}`);
    //             console.log(response.data);
    //         }
    //     }
    //     getHabitDescriptions();
    // }, [])

    // useEffect(() => {
    //     const fetchTodayHabits = async () => {
    //         const habitsForToday = await getTodayHabits();
    //         console.log("habits for today:", habitsForToday)
    //         setTodayHabits(habitsForToday);
    //     };
    //     fetchTodayHabits();
    //     console.log("Today's habits:", todayHabits);
    // }, [userHabits, currentUser]);

    // const handleUserHabitToggle = (userHabitId) => {
    //     setCompletedUserHabits(prev => ({ ...prev, [userHabitId]: !prev[userHabitId] }));
    // };

    const getCurrentDay = () => {
        const options = { weekday: 'long' };
        return new Intl.DateTimeFormat('en-US', options).format(new Date()).toLowerCase();
    };
    const currentDay = getCurrentDay();

    useEffect(() => {
        const getHabits = async () => {
            try {
                if (currentUser && currentDay) {
                    const response = await api.get(`/habits/user/${currentUser.id}/${currentDay}`);
                    console.log(response)
                    setTodayHabits(response.data);
                    console.log("Today's habits:", todayHabits);
                }
            } catch (error) {
                console.error('Error fetching habits:', error);
            }
        };
        getHabits();
    }, [currentUser, currentDay]);


    const handleSubmit = (e) => {
        e.preventDefault();
        console.log('Completed habits:', completedUserHabits);
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
                        {todayHabits.length > 0 ? (
                            <form onSubmit={handleSubmit}>
                                <ul>
                                    {todayHabits.map((habit) => (
                                        <li key={habit.id}>
                                            <label>
                                                <input
                                                    type="checkbox"
                                                    // checked={completedUserHabits[habit.id] || false}
                                                    onChange={() => handleUserHabitToggle(habit.id)}
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
                            <h1>0/10 Habits Complete</h1>
                            <p>Last Week: 0/10 Habits Complete</p>
                        </div>
                    </div>
                    <div className="progress-chart">
                        <h2>Weekly Progress</h2>
                        <div className="completion-icons">
                            <CompletionIcon day='M' completionStatus='complete'/>
                            <CompletionIcon day='T' completionStatus='partial'/>
                            <CompletionIcon day='W' completionStatus='complete'/>
                            <CompletionIcon day='T' completionStatus='complete'/>
                            <CompletionIcon day='F' completionStatus='incomplete'/>
                            <CompletionIcon day='S' completionStatus='unseen'/>
                            <CompletionIcon day='S' completionStatus='unseen'/>
                        </div>
                    </div>
                    <p>You're <strong>{bestStreak - streak}</strong> days away from a new record!</p>
                </div>
            </div>
        </div>
    );
};

export default Dashboard;