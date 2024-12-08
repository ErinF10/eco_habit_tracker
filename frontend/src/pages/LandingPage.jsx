import React from "react";
import { Link } from "react-router-dom"; 
import { SignInButton, SignUpButton, SignUp, SignedIn, SignedOut, UserButton } from "@clerk/clerk-react";
import imageArrow from '../images/arrow.png';
import imageBird from '../images/bird.png';
import imageLeaves from '../images/leaves.png';
import imageLeaf from '../images/leaf.png';
import '../styles/landingPage.css'

const LandingPage = () => {
    const headerItems = [
        { name: 'Home', path: '/' },
        { name: 'About', path: '/about' },
        { name: 'Contact Us', path: '/contact' },
      ];
    return (
               
        <div className="landing-page">
            <div className="heading">
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
                        <SignInButton />
                        <span className="separator">|</span>
                        <SignUpButton />
                        <SignedIn>
                            <UserButton />        
                        </SignedIn> 
                    </div>
                </nav>
            </header>

            <section className="hero">
                <h1>Your Eco Friendly Habit Tracker</h1>
                <button className="start-btn">Start Here!</button>
            </section>
            </div>
            


            <main className="main">

                <section className="info">
                    <img src={imageBird} alt='bird' className='info-image'/>
                    <div className="info-text">
                    <h2>Stay on top of your Habits</h2>
                    {/* <p>We know that it can be incredibly hard to form a new habit when you are leading a busy life and don’t have a way to check in with their new habit on a regular basis.</p> */}
                    <p>Building and maintaining new habits, especially sustainable ones, can feel overwhelming—especially when you’re juggling a busy lifestyle. We understand that it can be challenging to keep track of the small yet important actions that make a significant difference. Without a clear system to check in with your progress regularly, it’s easy to lose motivation and let those new habits slip away. That’s why we’ve created a seamless habit tracker that helps you stay on top of your eco-friendly goals, no matter how hectic life gets. Our simple yet effective system ensures you’ll never lose sight of your habits, giving you the accountability you need to turn your good intentions into lasting change.</p>
                    </div>
                </section>

                <section className="suggestions">
                    <div className="suggestions-text">
                    <h2>Get Personalized Suggestions</h2>
                    {/* <p>Many people want to create more sustainable habits in their daily lives but are not sure where to start. We help by providing personalized habit suggestions based on your daily routine.</p> */}
                    <p>Starting the journey toward a more sustainable lifestyle can be daunting when you’re not sure where to begin. The good news is that small, impactful changes can be integrated into your daily routine without overwhelming you. However, finding the right place to start is often the hardest part. Our app makes it easy by offering personalized habit suggestions tailored to your specific lifestyle. By filling out a brief survey about your daily habits and preferences, we provide you with actionable, eco-friendly suggestions that are relevant and achievable. Whether you’re looking to reduce your carbon footprint or simply live more sustainably, our custom recommendations help you take the first step in creating lasting, positive change in your life.</p>
                    </div>
                    <img src={imageLeaves} alt='leaves' className='suggestions-image'/>
                </section>

                <section className="milestones">
                    <img src={imageLeaf} alt='leaf' className='milestones-image'/>
                    <div className="milestones-text">
                    <h2>Track your Milestones</h2>
                    {/* <p>With our built-in feature to show your current total streak and weekly progress compared to total streak and previous weeks, you can keep track of how you are doing with keeping up with the goals you set for each week.</p> */}
                    <p>Tracking progress is crucial when it comes to forming new habits, and we’ve made it simple and rewarding. Our app not only lets you track your daily habits, but it also gives you an overview of your long-term progress. With features that display your current streak, as well as weekly progress comparisons against your best streaks, you’ll always have a clear view of how you’re doing. This visual representation of your achievements helps you stay motivated, pushing you to maintain consistency and celebrate the milestones you reach. Plus, we ensure that no missed days can be retroactively adjusted, keeping your progress honest and genuine. It’s a great way to stay motivated as you move closer to making eco-friendly habits second nature in your life.</p>
                    </div>
                </section>

                <section className="features">
                    <div className="feature">
                        <h2>Take the Survey</h2>
                        <p>some sample text some sample text some sample text some sample text some sample text some sample text </p>
                    </div>
                    <div className="feature-gap">
                        <img src={imageArrow} alt='arrow' className='arrow'/>
                    </div>
                    <div className="feature">
                        <h2>Get Habit Suggestions</h2>
                        <p>some sample text some sample text some sample text some sample text some sample text some sample text </p>
                    </div>
                    <div className="feature-gap">
                        <img src={imageArrow} alt='arrow' className='arrow'/>
                    </div>
                    <div className="feature">
                        <h2>Start your Eco Journey!</h2>
                        <p>some sample text some sample text some sample text some sample text some sample text some sample text </p>
                    <button className="start-btn">Start Here!</button>
                    </div>
                </section>
            </main>

            <footer>
            <p>&copy; 2024 Eco Habit Tracker</p>
            </footer>
        </div>
    )
}

export default LandingPage;