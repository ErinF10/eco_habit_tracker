import React from "react";
import Navbar from "../components/common/Navbar";
import Header from "../components/common/Header";
import '../styles/ecoBoard.css';

const EcoBoard = () => {
    const navigateToEcoBoard = () => {
        window.location.href = 'https://eco-board-5yf5.vercel.app/';
    }
    return (
        <div className="eco-board">
            <div className="navbar-container">
                <Navbar />
            </div>
            <div className="header-container">
                <Header page='Eco Board' />
            </div>
            <div className="main-content">
                <div className="eco-board-container">
                    <div className="eco-board-header">
                        <h1>Connect with the Eco Community</h1>
                        <p>Share your sustainable journey and learn from others</p>
                    </div>

                    <div className="features">
                        <div className="feature-card">
                            <svg className="feature-icon" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2">
                                <path d="M14.7519 12.5L10.7519 16.5M7.75192 11.5C7.75192 12.6046 6.85649 13.5 5.75192 13.5C4.64735 13.5 3.75192 12.6046 3.75192 11.5C3.75192 10.3954 4.64735 9.5 5.75192 9.5C6.85649 9.5 7.75192 10.3954 7.75192 11.5ZM20.7519 7.5C20.7519 8.60457 19.8565 9.5 18.7519 9.5C17.6474 9.5 16.7519 8.60457 16.7519 7.5C16.7519 6.39543 17.6474 5.5 18.7519 5.5C19.8565 5.5 20.7519 6.39543 20.7519 7.5ZM20.7519 15.5C20.7519 16.6046 19.8565 17.5 18.7519 17.5C17.6474 17.5 16.7519 16.6046 16.7519 15.5C16.7519 14.3954 17.6474 13.5 18.7519 13.5C19.8565 13.5 20.7519 14.3954 20.7519 15.5Z" />
                            </svg>
                            <h3>Share Your Wins</h3>
                            <p>Celebrate your eco-friendly achievements with the community</p>
                        </div>

                        <div className="feature-card">
                            <svg className="feature-icon" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2">
                                <path d="M12 3V5M5.31412 5.31412L6.728 6.728M3 12H5M5.31412 18.6859L6.728 17.272M12 19V21M18.6859 18.6859L17.272 17.272M21 12H19M18.6859 5.31412L17.272 6.728M15 12C15 13.6569 13.6569 15 12 15C10.3431 15 9 13.6569 9 12C9 10.3431 10.3431 9 12 9C13.6569 9 15 10.3431 15 12Z" />
                            </svg>
                            <h3>Get Inspired</h3>
                            <p>Discover new sustainable habits and tips from fellow eco-warriors</p>
                        </div>

                        <div className="feature-card">
                            <svg className="feature-icon" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2">
                                <path d="M15 19.128C15.853 19.3757 16.7368 19.5 17.6361 19.5C19.0609 19.5 20.4283 19.0803 21.6111 18.3081M15 19.128V21.5M15 19.128V16.5M21.6111 18.3081L19.5 20.5M21.6111 18.3081L23.5 16.5M3 13.5C3 16.8137 5.68629 19.5 9 19.5C12.3137 19.5 15 16.8137 15 13.5C15 10.1863 12.3137 7.5 9 7.5C5.68629 7.5 3 10.1863 3 13.5ZM9 11V16M11.5 13.5H6.5" />
                            </svg>
                            <h3>Join Discussions</h3>
                            <p>Connect with others committed to sustainable living</p>
                        </div>
                    </div>

                    <div className="cta-section">
                        <div className="cta-content">
                            <div className="cta-text">
                                <h2>Ready to join the conversation?</h2>
                                <p>Visit our Eco Board to connect with other environmentally conscious individuals.</p>
                            </div>
                    
                            <a href="https://eco-board-5yf5.vercel.app/">
                                <button className="cta-button" >
                                    Visit Eco Board
                                    <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2">
                                        <path d="M5 12H19M19 12L12 5M19 12L12 19"/>
                                    </svg>
                                </button>
                            </a>
                        </div>
                    </div>
                </div>

               
            </div>
        </div>
    )
}

export default EcoBoard;