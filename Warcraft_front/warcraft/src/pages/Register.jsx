// Register.js
import React, {useEffect, useState} from 'react';
import axios from 'axios';
import {Input} from '../UI/WarInput/index.jsx';
import {login} from "../store/authSlice.js";
import {useDispatch, useSelector} from "react-redux";
import {useNavigate} from "react-router-dom";

export const Register = () => {
    const sleepIcon = '../../public/UpgradableSkills/PNG/Sleep.png';
    const charmIcon = '../../public/UpgradableSkills/PNG/Charm3.png';
    const [formData, setFormData] = useState({ username: '', password1: '', password2: '' });
    const [error, setError] = useState('');
    const [showPassword, setShowPassword] = useState({ password1: false, password2: false });
    const dispatch = useDispatch();
    const handleChange = (e) => {
        setFormData({ ...formData, [e.target.name]: e.target.value });
    };

    const handleSubmit = async (e) => {
        e.preventDefault();
        setError('');

        if (formData.password1 !== formData.password2) {
            setError('Пароли не совпадают');
            return;
        }

        try {
            const response = await axios.post('http://localhost:8000/api/v1/register/', formData, {
                headers: { 'Content-Type': 'application/json' }
            });
            console.log(response.data);
            dispatch(login({ token: response.data.token, is_superuser: response.data.is_superuser }));
            navigate('/main');
        } catch (error) {
            setError('Ошибка регистрации');
        }
    };

    const togglePasswordVisibility = (field) => {
        setShowPassword((prev) => ({
            ...prev,
            [field]: !prev[field],
        }));
    };
    const navigate = useNavigate();
    const isAuthenticated = useSelector((state) => state.auth.isAuthenticated);

    useEffect(() => {
        if (isAuthenticated) {
            navigate('/main');
        }
    }, [isAuthenticated, navigate]);

    return (
        <div className="register-page">
            <div className="all">
                <div className="main_text">
                    <img src="../../public/User/logo.webp" alt="Logo" />
                    <div className="greeting_text">Регистрация в Warcraft 3 Frozen Throne</div>
                    <div className="bottom_text">Присоединяйтесь к сообществу игроков!</div>
                </div>
                <form onSubmit={handleSubmit} className="login-form register-form">
                    <div className="greeting_text reg_txt">Регистрация</div>

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
                             key={showPassword.password1}
                            type={showPassword.password1 ? "text" : "password"}
                            name="password1"
                            placeholder="Пароль"
                            value={formData.password1}
                            onChange={handleChange}
                            required
                        />
                        <div className="image id_1" onClick={() => togglePasswordVisibility('password1')}>
                            <img
                                src={showPassword.password1 ? charmIcon : sleepIcon}
                                alt="Show Password"
                                className="show"
                            />
                        </div>
                    </div>

                    <div className="password-container input_2">
                        <Input
                            key={showPassword.password2}
                            type={showPassword.password2 ? "text" : "password"}
                            name="password2"
                            placeholder="Повторите пароль"
                            value={formData.password2}
                            onChange={handleChange}
                            required
                        />
                        <div className="image id_2" onClick={() => togglePasswordVisibility('password2')}>
                            <img
                                src={showPassword.password2 ? charmIcon : sleepIcon}
                                alt="Show Password"
                                className="show"
                            />
                        </div>
                    </div>

                    <button type="submit" className="">Зарегистрироваться</button>
                </form>
            </div>
        </div>
    );
};
