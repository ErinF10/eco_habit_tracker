import React, { useState, useEffect } from "react";
import { useCurrentUser } from "../../UserContext";
import { useUserHabits } from "../../UserHabitContext";
import api from "../../api";

const Habit = ({ id: habitId, title: initialTitle }) => {

    const { currentUser } = useCurrentUser();
    const { userHabits, setUserHabits } = useUserHabits();
    const [isEditing, setIsEditing] = useState(false);
    const [title, setTitle] = useState(initialTitle);
    const [userHabitId, setUserHabitId] = useState();
    const [selectedDays, setSelectedDays] = useState({
        Mon: false, Tue: false, Wed: false, Thu: false, Fri: false, Sat: false, Sun: false
    });
    const [userHabitSchedule, setUserHabitSchedule] = useState(null);
    useEffect( () => {
        const getUserHabitId = async () => {
            if (currentUser) {
                const response = await api.get(`/userhabits/${currentUser.id}/${habitId}`);
                const userHabit = response.data;
                console.log("user habit:", userHabit);
                setUserHabitId(userHabit.id);
            }
            
        }
        getUserHabitId();
    }, [currentUser]);
    
    // console.log("habit_id", habit_id);
    useEffect(() => {
        const initUserHabitSchedule = async () => {
            try {
                if (userHabitId) {
                    const response = await api.get(`/userhabitschedules/${userHabitId}`);
                    setUserHabitSchedule(response.data);
                    
                    // Update selectedDays based on the schedule
                    setSelectedDays({
                        Mon: response.data.monday,
                        Tue: response.data.tuesday,
                        Wed: response.data.wednesday,
                        Thu: response.data.thursday,
                        Fri: response.data.friday,
                        Sat: response.data.saturday,
                        Sun: response.data.sunday
                    });
                }
                
            } catch (error) {
                console.error("Error retrieving user habit schedule:", error);
                console.error("Error Details:", error.response?.data);
            }
        };

        initUserHabitSchedule();
    }, [currentUser.id, userHabitId]);

    const getUserHabitSchedule = async () => {
        try {
            if (userHabitId){ 
                const response = await api.get(`/userhabitschedules/${userHabitId}`);
                console.log(response);
                return response.data; 
            }
            
        } catch (error) {
            console.error("Error retrieving user habit schedule:", error);
            console.error("Error Details:", error.response?.data);
        }
    };
    let user_habit_schedule;

    const initUserHabitSchedule = async () => {
        user_habit_schedule = await getUserHabitSchedule();
        console.log(user_habit_schedule);
    };
    
    initUserHabitSchedule();
        
    const handleTitleChange = (e) => setTitle(e.target.value);

    const handleEditClick = () => setIsEditing(true);

    const handleDelete = async () => {
        try {
            if (userHabitId) {
                console.log("Deleting...");
                console.log(currentUser.id, userHabitId);
                const response = await api.get(`/userhabits/${userHabitId}`);
                console.log(response);
                const user_habit = response.data;
                console.log("habit to be deleted: ", user_habit);
                const deleted = await api.delete(`/userhabits/${currentUser.id}/${user_habit.habit_id}`);
                console.log("Deleted: ", deleted);
            }
            
        }
        catch (error) {
            console.error("Error deleting user habit:", error);
            console.error("Error Details:", error.response?.data);
        }
      
    }

    const handleSaveClick = async () => {
        setIsEditing(false);
        // console.log("Updated habit:", title, selectedDays);
        if (typeof title !== 'string' || title.trim() === '') {
            alert('Please enter a valid habit title');
            return;
        }

        try {
            if (currentUser) {
                console.log('title:', title);
                const updatedHabit = await api.post('/habits', { description: title });
                console.log(updatedHabit.data.id, currentUser.id);
                const response = await api.post('/userhabits', { user_id: currentUser.id, habit_id: updatedHabit.data.id });
                const updatedUserHabit = response.data;
                setUserHabits([...userHabits, updatedHabit]); // Add the new habit to the state
                setTitle(''); // Clear the input field

                console.log(`New habit id ${updatedHabit.data.id} created for user ${currentUser.id}`);
                console.log(updatedUserHabit)
                console.log(updatedUserHabit.new_user_habit.id)
    
                const habitSchedule = await api.post('/userhabitschedules', {user_habit_id : updatedUserHabit.new_user_habit.id} )
    
            }
            
        } catch (error) {
            console.error('Error adding habit:', error);
            alert('Failed to add habit. Please try again.');
        }    
    };

    const toggleDay = async (day) => {
        if (userHabitSchedule){
            setSelectedDays(prev => ({ ...prev, [day]: !prev[day] }));
            // console.log(day);
            const response = await api.put(`/userhabitschedules/${userHabitSchedule.id}?day=${day}`);
            // console.log("Updated schedule", response.data);
        }
        
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