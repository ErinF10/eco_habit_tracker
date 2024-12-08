import React from "react";
import Navbar from "../components/common/Navbar";
import Header from "../components/common/Header";
import Habit from "../components/manage_habits/Habit";
import '../styles/manageHabits.css';
import { useCurrentUser } from "../UserContext";
import { useHabits } from "../HabitContext";
import { useState, useEffect } from "react";
import api from "../api";


const ManageHabits = () => {

    const { habits, setHabits } = useHabits();
    const [newHabitTitle, setNewHabitTitle] = useState('');

    const { currentUser } = useCurrentUser();

    const handleAdd = async () => {
        if (typeof newHabitTitle !== 'string' || newHabitTitle.trim() === '') {
            alert('Please enter a valid habit title');
            return;
        }

        try {
            console.log('title:', newHabitTitle);
            const newHabit = await api.post('/habits', { description: newHabitTitle });
            console.log(newHabit.data.id, currentUser.id);
            await api.post('/userhabits', { user_id: currentUser.id, habit_id: newHabit.data.id });
            
            setHabits([...habits, newHabit]); // Add the new habit to the state

            setNewHabitTitle(''); // Clear the input field
            console.log(`New habit id ${newHabit.data.id} created for user ${currentUser.id}`);
        } catch (error) {
            console.error('Error adding habit:', error);
            alert('Failed to add habit. Please try again.');
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
                    {habits && habits.length > 0 ? (
                        <ul>
                            {habits.map((habit) => (
                                <Habit 
                                    key={habit.id}
                                    id={habit.id}
                                    title={habit.description}
                                    // onSave={ onSave(title, selectedDays) }
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