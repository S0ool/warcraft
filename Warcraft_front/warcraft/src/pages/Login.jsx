// Login.js
import React, {useEffect, useState} from 'react';
import axios from 'axios';
import { Input } from '../UI/WarInput/index.jsx';
import {useDispatch, useSelector} from 'react-redux';
import { login } from '../store/authSlice.js';
import { useNavigate } from 'react-router-dom';

export const Login = () => {
    const sleepIcon = '../../public/UpgradableSkills/PNG/Sleep.png';
    const charmIcon = '../../public/UpgradableSkills/PNG/Charm3.png';
    const [formData, setFormData] = useState({ username: '', password: '' });
    const [error, setError] = useState('');
    const [showPassword, setShowPassword] = useState(false);
    const [icon, setIcon] = useState(sleepIcon);
    const dispatch = useDispatch();
    const navigate = useNavigate();
    const isAuthenticated = useSelector((state) => state.auth.isAuthenticated);


    useEffect(() => {
        if (isAuthenticated) {
            navigate('/main');
        }
    }, [isAuthenticated, navigate]);
    const handleChange = (e) => {
        setFormData({ ...formData, [e.target.name]: e.target.value });
    };

    const handleSubmit = async (e) => {
        e.preventDefault();
        setError('');

        try {
            const response = await axios.post('http://localhost:8000/api/v1/login/', formData, {
                headers: { 'Content-Type': 'application/json' }
            });
            console.log(response.data);
            dispatch(login({ token: response.data.token, is_superuser: response.data.is_superuser }));
            navigate('/main'); // Перенаправление на главную страницу
        } catch (error) {
            setError('Неправильное имя пользователя или пароль');
        }
    };

    const togglePassword = () => {
        setShowPassword(prev => !prev);
        setIcon(prev => (prev === sleepIcon ? charmIcon : sleepIcon));
    };

    return (
        <div className="login-page">
            <div className="all">
                <div className="main_text">
                    <img src="../../public/User/logo.webp" alt="Logo" />
                    <div className="greeting_text">Авторизация в Warcraft 3 Frozen Throne</div>
                    <div className="bottom_text">Присоединяйтесь к сообществу игроков!</div>
                </div>
                <form onSubmit={handleSubmit} className="login-form">
                    <div className="greeting_text reg_txt">Авторизация</div>
                    <Input
                        type="text"
                        name="username"
                        placeholder="Имя пользователя"
                        value={formData.username}
                        onChange={handleChange}
                        required
                    />
                    {error && <p className="error-message">{error}</p>}
                    <div className="password-container input_1">
                        <Input
                            type={showPassword ? "text" : "password"}
                            name="password"
                            placeholder="Пароль"
                            value={formData.password}
                            onChange={handleChange}
                            required
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
