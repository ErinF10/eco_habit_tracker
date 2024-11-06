import React from "react";

const Habit = (props) => {
    return (
        <div className="habit">
            <div className="habit-name">
                <h3>{props.title}</h3>
                <div className="edit-delete">
                    <img alt='edit-icon'></img>
                    <img alt='delete-icon'></img>
                </div>
            </div>
            
            <div className="days-of-week-selector">
                <button>Mon</button>
                <button>Tue</button>
                <button>Wed</button>
                <button>Thu</button>
                <button>Fri</button>
                <button>Sat</button>
                <button>Sun</button>
            </div>
        </div>
    )
}

export default Habit;
