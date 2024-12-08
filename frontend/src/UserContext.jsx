import React, { createContext, useState, useEffect, useContext } from 'react';
import { useUser } from "@clerk/clerk-react";
import api from "./api";

const UserContext = createContext();

export const UserProvider = ({ children }) => {
    const { isLoaded, isSignedIn, user } = useUser();
    const [currentUser, setCurrentUser] = useState(null);
    const [isLoading, setIsLoading] = useState(true);

    useEffect(() => {
        const syncAndFetchUser = async () => {
            if (isLoaded && isSignedIn && user) {
                try {
                    setIsLoading(true);
                    // Sync user
                    await api.post('/users/sync-user', {
                        clerk_id: user.id,
                        username: user.username,
                        email: user.primaryEmailAddress?.emailAddress ?? null,
                    });

                    // Fetch user data
                    const userResponse = await api.get(`/users/${user.id}`);
                    setCurrentUser(userResponse.data);

                    // Initialize streaks to 0 for new users 
                    await api.post('/userstreaks', userResponse.data.id);

                } catch (error) {
                    console.error("Error syncing or fetching user:", error);
                } finally {
                    setIsLoading(false);
                }
            } else {
                setCurrentUser(null);
                setIsLoading(false);
            }
        };
        
        syncAndFetchUser();
    }, [isLoaded, isSignedIn, user]);

    return (
        <UserContext.Provider value={{ currentUser, setCurrentUser, isLoading }}>
            {children}
        </UserContext.Provider>
    );
};

export const useCurrentUser = () => useContext(UserContext);