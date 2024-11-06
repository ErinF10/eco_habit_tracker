import React from "react";

const CompletionIcon = (props) => {
    const getBackgroundColor = () => {
        switch (props.completionStatus) {
            case 'complete':
                return 'green';
            case 'partial':
                return 'yellow';
            case 'incomplete':
                return 'gray'
            default:
                return 'lightGray'
        }

    }
    return (
        <div className="completion-icon" style={{ backgroundColor: getBackgroundColor()}}>
            <p>{props.day}</p>
        </div>
    )
}

export default CompletionIcon;