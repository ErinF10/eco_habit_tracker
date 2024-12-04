import React from "react";
import { Link } from "react-router-dom"; 
import { SignInButton, SignedIn, SignedOut, UserButton } from "@clerk/clerk-react";
import '../styles/landingPage.css'

const LandingPage = () => {
    const headerItems = [
        { name: 'Home', path: '/' },
        { name: 'About', path: '/about' },
        { name: 'Contact Us', path: '/contact' },
      ];
    return (
        <div className="landing-page">
            <header className="landing-header">
                <nav>
                    <ul className="header-list">
                        {headerItems.map((item, index) => (
                            <li key={index} className="header-item">
                                <Link to={item.path}>{item.name}</Link>
                            </li>
                        ))}
                    </ul>
                    <div className="auth-links">                   
                        <button>
                            <Link to="/dashboard" className="auth-link">Get Started!</Link>
                        </button>
                        <span className="separator">|</span>
                        <SignedOut>
                            <SignInButton />
                        </SignedOut>
                        <SignedIn>
                            <UserButton />        
                        </SignedIn> 
                    </div>
                </nav>
            </header>
        </div>
    )
}

export default LandingPage;