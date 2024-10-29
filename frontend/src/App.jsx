import React from 'react'
import { BrowserRouter as Router, Route, Routes, Link } from 'react-router-dom';
import './styles/App.css'

import LandingPage from './pages/LandingPage';
import About from './pages/About'
import ContactUs from './pages/ContactUs';
import Dashboard from './pages/Dashboard';
import Profile from './pages/Profile';
import ManageHabits from './pages/ManageHabits';
import Settings from './pages/Settings';
import Progress from './pages/Progress';
import SignIn from './pages/SignIn';
import RoutineSurvey from './pages/RoutineSurvey';
//Test
function App() {

  return (
    <Router>
      <div className='App'>
        <Routes>
          <Route path='/' element={<LandingPage />} />
          <Route path='/about' element={<About />} />
          <Route path='/contact' element={<ContactUs />} />
          <Route path='/dashboard' element={<Dashboard />} />
          <Route path='/profile' element={<Profile />} />
          <Route path='/manage-habits' element={<ManageHabits />} />
          <Route path='/settings' element={<Settings />} />
          <Route path='/progress' element={<Progress />} />
          <Route path='/signin' element={<SignIn />} />
          <Route path='/routine-survey' element={<RoutineSurvey />} />
        </Routes>
      </div>
    </Router>
  )
}

export default App
