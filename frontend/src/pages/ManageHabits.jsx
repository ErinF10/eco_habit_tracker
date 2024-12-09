import React from "react";
import Navbar from "../components/common/Navbar";
import Header from "../components/common/Header";
import Habit from "../components/manage_habits/Habit";
import '../styles/manageHabits.css';
import { useCurrentUser } from "../UserContext";
import { useUserHabits } from "../UserHabitContext";
import { useState, useEffect } from "react";
import api from "../api";


const ManageHabits = () => {

    const { userHabits, setUserHabits } = useUserHabits();
    const [habits, setHabits] = useState([])
    const [newHabitTitle, setNewHabitTitle] = useState('');

    const { currentUser } = useCurrentUser();

    const getHabits = async () => {
        if (!currentUser) return; // Check if currentUser exists
        try {
            const response = await api.get(`/habits/user/${currentUser.id}`); // Ensure this matches your backend endpoint
            setHabits(response.data);
            console.log("habits list:",habits);
        } catch (error) {
            console.error('Error fetching habits:', error);
        }
    };
    useEffect(() => {
        getHabits();
    }, [currentUser]);

    const handleAdd = async () => {
        if (typeof newHabitTitle !== 'string' || newHabitTitle.trim() === '') {
            alert('Please enter a valid habit title');
            return;
        }

        try {
            console.log('title:', newHabitTitle);
            const newHabit = await api.post('/habits', { description: newHabitTitle });
            // console.log(newHabit.data.id, currentUser.id);
            const response = await api.post('/userhabits', { user_id: currentUser.id, habit_id: newHabit.data.id });
            const user_habit = response.data;
            console.log("user_habit:", user_habit)
            setUserHabits([...userHabits, user_habit]); // Add the new habit to the state

            setNewHabitTitle(''); // Clear the input field
            console.log(`New habit id ${newHabit.data.id} created for user ${currentUser.id}`);
            console.log("user_habit.id:", user_habit.new_user_habit.id);
            const habitSchedule = await api.post('/userhabitschedules', {user_habit_id: user_habit.new_user_habit.id})
        }
        catch (error) {
            console.error('Error adding habit or schedule:', error);
        }

    }


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
                    <input
                        type="text"
                        placeholder="Enter a new habit"
                        value={newHabitTitle}
                        onChange={(e) => setNewHabitTitle(e.target.value)}
                        autoFocus
                    />                      
                    <button onClick={handleAdd}>+ Add</button>
                    </div>
                </div>
                <div className="current-habits">
                    <h1>Current Habits</h1>
                    {/* {userHabits && userHabits.length > 0 ? (
                        <ul>
                            {userHabits.map((userHabit) => (
                                <Habit 
                                    key={userHabit.id}
                                    id={userHabit.id}
                                    title={userHabit.habit.description}
                                />
                            ))}
                        </ul>
                    ) : (
                        <p>No habits yet</p>
                    )} */}
                    {habits && habits.length > 0 ? (
                        <ul>
                            {habits.map((habit) => (
                                <Habit 
                                    key={habit.id}
                                    id={habit.id}
                                    title={habit.description}
                                />
                            ))}
                        </ul>
                    ) : (
                        <p>No habits yet</p>
                    )}
                </div>
            </div>
        </div>
    )
}

export default ManageHabits;