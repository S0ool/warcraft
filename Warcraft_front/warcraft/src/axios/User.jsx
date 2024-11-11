import axios from 'axios';
import {login} from "../store/authSlice.js";


export const getUserProfile = async () => {
    const token = localStorage.getItem('token');
    try {
        const response = await axios.get('http://localhost:8000/api/v1/profile/', {
            headers: {
                'Authorization': `Bearer ${token}`
            }
        });
        return response.data;
    } catch (error) {
        console.error("Error fetching profile:", error);
        throw error;
    }
};
export const changeAvatar = async (event) => {
    event.preventDefault();

    const token = localStorage.getItem('token');
    const formData = new FormData();
    const avatarFile = document.getElementById('image_input').files[0];

    if (!avatarFile) {
        console.error("Файл аватара не выбран");
        return;
    }

    formData.append('avatar', avatarFile);

    try {
        const response = await axios.post('http://localhost:8000/api/v1/profile/', formData, {
            headers: {
                'Authorization': `Bearer ${token}`,
                'Content-Type': 'multipart/form-data',
            },
        });
        console.log('Аватар успешно обновлён');
        return response.data;
    } catch (error) {
        console.error("Ошибка при обновлении аватара:", error);
        throw error;
    }
};

export const LoginUser = async (e, setError, formData, dispatch, navigate) => {
    e.preventDefault();
    setError('');
    try {
        const response = await axios.post('http://localhost:8000/api/v1/login/', formData, {
            headers: {'Content-Type': 'application/json'}
        });
        console.log(response.data);
        dispatch(login({token: response.data.token, is_superuser: response.data.is_superuser}));
        navigate('/main');
    } catch (error) {
        setError('Неправильное имя пользователя или пароль');
    }
};

export const RegisterUser = async (e, setError, formData, dispatch, navigate) => {
    e.preventDefault();
    setError('');

    if (formData.password1 !== formData.password2) {
        setError('Пароли не совпадают');
        return;
    }

    try {
        const response = await axios.post('http://localhost:8000/api/v1/register/', formData, {
            headers: {'Content-Type': 'application/json'}
        });
        console.log(response.data);
        dispatch(login({token: response.data.token, is_superuser: response.data.is_superuser}));
        navigate('/main');
    } catch (error) {
        setError('Ошибка регистрации');
    }
};