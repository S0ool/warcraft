import {useEffect, useState} from 'react';
import {Input} from '../UI/WarInput/index.jsx';
import {useDispatch, useSelector} from 'react-redux';
import {useNavigate} from 'react-router-dom';
import {LoginUser} from "../axios/User.jsx";

export const Login = () => {
    const dispatch = useDispatch();
    const navigate = useNavigate();
    const sleepIcon = useSelector((state) => state.data.sleepIcon);
    const charmIcon = useSelector((state) => state.data.charmIcon);
    const [formData, setFormData] = useState({username: '', password: ''});
    const [error, setError] = useState('');
    const [showPassword, setShowPassword] = useState(false);
    const [icon, setIcon] = useState(sleepIcon);

    const isAuthenticated = useSelector((state) => state.auth.isAuthenticated);


    useEffect(() => {
        if (isAuthenticated) {
            navigate('/main');
        }
    }, [isAuthenticated, navigate]);
    const handleChange = (e) => {
        setFormData({...formData, [e.target.name]: e.target.value});

    };


    const togglePassword = () => {
        setShowPassword(prev => !prev);
        setIcon(prev => prev === sleepIcon ? charmIcon : sleepIcon);
    };

    return (
        <div className="login-page">
            <div className="all">
                <div className="main_text">
                    <img src="../../public/User/logo.webp" alt="Logo"/>
                    <div className="greeting_text">Авторизация в Warcraft 3 Frozen Throne</div>
                    <div className="bottom_text">Присоединяйтесь к сообществу игроков!</div>
                </div>
                <form onSubmit={(e) => LoginUser(e, setError, formData, dispatch, navigate)} className="login-form">
                    <div className="greeting_text reg_txt">Авторизация</div>
                    <Input
                        type="text"
                        name="username"
                        placeholder="Имя пользователя"
                        value={formData.username}
                        onChange={handleChange}
                        required={true}
                    />
                    {error && <p className="error-message">{error}</p>}
                    <div className="password-container input_1">
                        <Input
                            type={showPassword ? "text" : "password"}
                            name="password"
                            placeholder="Пароль"
                            value={formData.password}
                            onChange={handleChange}
                            required={true}
                        />
                        <div className="image id_1" onClick={togglePassword}>
                            <img
                                src={icon}
                                alt="Show Password"
                                className="show"
                            />
                        </div>
                    </div>
                    <button type="submit" className="login-button">Войти</button>
                </form>
            </div>
        </div>
    );
};
