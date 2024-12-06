import React, { createContext, useState, useEffect, useContext } from 'react';
import { useUser } from "@clerk/clerk-react";
import api from "../api";

const UserContext = createContext();

export const UserProvider = ({ children }) => {
    const { isLoaded, isSignedIn, user } = useUser();
    const [currentUser, setCurrentUser] = useState(null);

    useEffect(() => {
        const syncAndFetchUser = async () => {
            if (isLoaded && isSignedIn && user) {
                try {
                    // Sync user
                    await api.post('/users/sync-user', {
                        clerk_id: user.id,
                        username: user.username,
                        email: user.primaryEmailAddress?.emailAddress ?? null,
                    });

                    // Fetch user data
                    const userResponse = await api.get(`/users/${user.id}`);
                    setCurrentUser(userResponse.data);
                } catch (error) {
                    console.error("Error syncing or fetching user:", error);
                }
            }
        };

        syncAndFetchUser();
    }, [isLoaded, isSignedIn, user]);

    return (
        <UserContext.Provider value={{ currentUser, setCurrentUser }}>
            {children}
        </UserContext.Provider>
    );
};

export const useCurrentUser = () => useContext(UserContext);