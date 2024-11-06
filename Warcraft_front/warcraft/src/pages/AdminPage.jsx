import {useEffect} from "react";
import {useNavigate} from "react-router-dom";
import {useSelector} from "react-redux";


export const AdminPage = () => {
    const navigate = useNavigate();
    const isAuthenticated = useSelector((state) => state.auth.isAuthenticated);
    const isSuper = useSelector((state) => state.auth.isSuperUser);
    useEffect(() => {
        if (!isAuthenticated  || !isSuper) {
            navigate('/main');
        }
    }, [isAuthenticated, navigate, isSuper]);



    return (
        <>
        </>
    )
}