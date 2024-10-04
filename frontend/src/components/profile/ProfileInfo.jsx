import React from "react";

const ProfileInfo = ({field, contents}) => {
    return (
        <div className="profile-info">
            <p>{field}: </p>
            {contents !== 'None' ? <p>{contents}</p> : <button className="add">+add</button>}
        </div>
    )
}

export default ProfileInfo;