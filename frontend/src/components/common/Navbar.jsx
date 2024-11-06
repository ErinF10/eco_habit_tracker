import React from "react";
import { Link } from "react-router-dom";

const Navbar = () => {
    const navItems = [
        {name: 'Dashboard', path: '/dashboard'},
        { name: 'Profile', path: '/profile' },
        { name: 'Manage Habits', path: '/manage-habits' },
        { name: 'Progress', path: '/progress' },
        { name: 'Settings', path: '/settings'},
    ]
    return (
        <div className="navbar">
            <h2>Eco Habit Tracker</h2>
            <ul className="nav-items">
                {navItems.map((item, index) => (
                    <li key={index} className="nav-item">
                        <Link to={item.path}>{item.name}</Link>
                    </li>
                ))}
            </ul>
        </div>
    )
}

export default Navbar;