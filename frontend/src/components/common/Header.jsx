import React from "react";

const Header = (props) => {
    return (
        <div className="header">
            <h2>{props.page}</h2>
            <p>Erin Forrest</p>
        </div>
    )
}

export default Header;