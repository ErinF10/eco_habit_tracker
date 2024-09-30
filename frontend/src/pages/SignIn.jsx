import React from "react";
import { Link } from "react-router-dom";

const SignIn = () => {
    return (
        <div>
            <Link to='/dashboard'>
                <button>Sign In</button>
            </Link>
        </div>
    )
}

export default SignIn;