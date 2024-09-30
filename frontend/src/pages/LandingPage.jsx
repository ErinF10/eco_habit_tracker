import React from "react";
import { Link } from "react-router-dom"; 

const LandingPage = () => {
    const headerItems = [
        { name: 'Home', path: '/' },
        { name: 'About', path: '/about' },
        { name: 'Contact Us', path: '/contact' },
      ];
    return (
        <div className="landing-page">
            <header className="header">
                <nav>
                    <ul className="header-list">
                        {headerItems.map((item, index) => (
                            <li key={index} className="header-item">
                                <Link to={item.path}>{item.name}</Link>
                            </li>
                        ))}
                    </ul>
                    <div className="auth-links">
                        <Link to="/signin" className="auth-link">Sign In</Link>
                        <span className="separator">|</span>
                        <Link to="/create-account" className="auth-link">Create Account</Link>
                    </div>
                </nav>
            </header>
        </div>
    )
}

export default LandingPage;