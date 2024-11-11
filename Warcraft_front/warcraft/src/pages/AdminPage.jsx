import {useEffect} from "react";
import {useNavigate} from "react-router-dom";
import {useSelector} from "react-redux";
import {AdminHeader} from "../components/AdminPanel/AdminHeader/index.jsx";
import {Images} from "../components/AdminPanel/Images/index.jsx";


export const AdminPage = () => {
    const navigate = useNavigate();
    const isAuthenticated = useSelector((state) => state.auth.isAuthenticated);
    const isSuper = useSelector((state) => state.auth.isSuperUser);
    // useEffect(() => {
    //     if (!isAuthenticated) {
    //         navigate('/login');
    //     } else if (!isSuper) {
    //         navigate('/main');
    //     }
    // }, [isAuthenticated, navigate, isSuper]);


    return (
        <>
            <AdminHeader/>
            <Images/>
        </>
    )
};