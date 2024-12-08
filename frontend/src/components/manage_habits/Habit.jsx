import React, { useState } from "react";
import { useCurrentUser } from "../../UserContext";
import { useHabits } from "../../HabitContext";
import api from "../../api";

const Habit = ({ id: habit_id, title: initialTitle }) => {

    const { currentUser } = useCurrentUser();
    const { habits, setHabits } = useHabits();
    const [isEditing, setIsEditing] = useState(false);
    const [title, setTitle] = useState(initialTitle);
    const [selectedDays, setSelectedDays] = useState({
        Mon: false, Tue: false, Wed: false, Thu: false, Fri: false, Sat: false, Sun: false
    });

    const handleTitleChange = (e) => setTitle(e.target.value);

    const handleEditClick = () => setIsEditing(true);

    const handleDelete = async () => {
        try {
            console.log("Deleting...");
            console.log(currentUser.id, habit_id);
            const response = await api.delete(`/userhabits/${currentUser.id}/${habit_id}`);
            console.log("Deleted: ", response);

        }
        catch (error) {
            console.error("Error deleting user habit:", error);
            console.error("Error Details:", error.response?.data);
        }
      
    }

    const handleSaveClick = async () => {
        setIsEditing(false);
        console.log("Updated habit:", title, selectedDays);
        if (typeof title !== 'string' || title.trim() === '') {
            alert('Please enter a valid habit title');
            return;
        }

        try {
            console.log('title:', title);
            const updatedHabit = await api.post('/habits', { description: title });
            console.log(updatedHabit.data.id, currentUser.id);
            await api.post('/userhabits', { user_id: currentUser.id, habit_id: updatedHabit.data.id });
            
            setHabits([...habits, updatedHabit]); // Add the new habit to the state
            setTitle(''); // Clear the input field
            console.log(`New habit id ${updatedHabit.data.id} created for user ${currentUser.id}`);

        } catch (error) {
            console.error('Error adding habit:', error);
            alert('Failed to add habit. Please try again.');
        }    
    };

    const toggleDay = (day) => {
        setSelectedDays(prev => ({ ...prev, [day]: !prev[day] }));
    };

    return (
        <div className="habit">
            <div className="habit-name">
                {isEditing ? (
                    <input
                        type="text"
                        value={title}
                        onChange={handleTitleChange}
                        autoFocus
                    />
                ) : (
                    <h3>{title}</h3>
                )}
                <div className="edit-delete">
                    {isEditing ? (
                        <button onClick={handleSaveClick}>Save</button>
                    ) : (
                        <button onClick={handleEditClick}>Edit</button>
                    )}
                    <button className="delete" onClick={handleDelete}>Delete</button>
                </div>
            </div>
            
            <div className="days-of-week-selector">
                {Object.entries(selectedDays).map(([day, isSelected]) => (
                    <button
                        key={day}
                        onClick={() => toggleDay(day)}
                        className={isSelected ? 'selected' : ''}
                    >
                        {day}
                    </button>
                ))}
            </div>
        </div>
    );
};

export default Habit;