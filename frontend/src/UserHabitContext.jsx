import React, { createContext, useState, useEffect, useContext } from 'react';
import { useCurrentUser } from './UserContext';
import api from "./api";

const UserHabitContext = createContext();

export const UserHabitProvider = ({ children }) => {
    const { currentUser } = useCurrentUser();
    const [userHabits, setUserHabits] = useState([]);

    useEffect(() => {
        const fetchUserHabits = async () => {
            if (currentUser) {
                try {               
                    if (currentUser && currentUser.id) {
                        const response = await api.get(`/userhabits/user/${currentUser.id}`);
                        console.log('Habits Response:', response.data);
                        
                        if (response.data && Array.isArray(response.data)) {
                            setUserHabits(response.data);
                        } else {
                            console.error("Unexpected response format:", response.data);
                        }
                    } else {
                        console.warn('No valid user ID to fetch habits');
                    }  
                } catch (error) {
                    console.error("Error fetching user data:", error);
                    console.error("Error Details:", error.response?.data);
                }
            }
        };
        fetchUserHabits();
    }, [currentUser]);

    return (
        <UserHabitContext.Provider value={{ userHabits, setUserHabits }}>
            {children}
        </UserHabitContext.Provider>
    );
};

export const useUserHabits = () => useContext(UserHabitContext);