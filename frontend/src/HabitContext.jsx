import React, { createContext, useState, useEffect, useContext } from 'react';
import { useCurrentUser } from './UserContext';
import api from "./api";

const HabitContext = createContext();

export const HabitProvider = ({ children }) => {
    const { currentUser } = useCurrentUser();
    const [habits, setHabits] = useState([]);

    useEffect(() => {
        const fetchUserHabits = async () => {
            if (currentUser) {
                try {               
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
                } catch (error) {
                    console.error("Error fetching user data:", error);
                    console.error("Error Details:", error.response?.data);
                }
            }
        };
        fetchUserHabits();
    }, [currentUser]);

    return (
        <HabitContext.Provider value={{ habits, setHabits }}>
            {children}
        </HabitContext.Provider>
    );
};

export const useHabits = () => useContext(HabitContext);