import React from 'react'
import { BrowserRouter as Router, Route, Routes, Link } from 'react-router-dom';
import './styles/App.css'

import LandingPage from './pages/LandingPage';
import About from './pages/About'
import ContactUs from './pages/ContactUs';
// import Dashboard from './pages/Dashboard';
// import Profile from './pages/Profile';
// import ManageHabits from './pages/ManageHabits';
// import Settings from './pages/Settings';
// import Progress from './pages/Progress';

function App() {

  return (
    <Router>
      <div className='App'>
        <Routes>
          <Route path='/' element={<LandingPage />} />
          <Route path='/about' element={<About />} />
          <Route path='/contact' element={<ContactUs />} />
        </Routes>
      </div>
    </Router>
  )
}

export default App
