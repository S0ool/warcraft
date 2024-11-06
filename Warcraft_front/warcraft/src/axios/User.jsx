import axios from 'axios';

axios.defaults.baseURL = 'http://localhost:8000';

export const register = async (userData) => {
    try {
        const response = await axios.post('/api/v1/register/', userData, {
            headers: { 'Content-Type': 'application/json' }
        });
        return response.data;
    } catch (error) {
        console.error("Ошибка регистрации:", error.response.data);
        return error.response.data;
    }
};




export const login = async (credentials) => {
    try {
        const response = await axios.post('/api/v1/login/', credentials, {
            headers: { 'Content-Type': 'application/json' }
        });
        return response.data;
    } catch (error) {
        console.error("Ошибка входа:", error.response.data);

        return error.response.data;
    }
};

export const getUserProfile = async () => {
    const token = localStorage.getItem('token'); // Получаем токен
    try {
        const response = await axios.get('http://localhost:8000/api/v1/profile/', {
            headers: {
                'Authorization': `Bearer ${token}`, // Добавляем токен в заголовок
            }
        });
        return response.data; // Возвращаем данные пользователя
    } catch (error) {
        console.error("Error fetching profile:", error);
        throw error; // Бросаем ошибку, чтобы обработать её в компоненте
    }
}
export const changeAvatar = async (event) => {
    event.preventDefault();

    const token = localStorage.getItem('token'); // Получаем токен
    const formData = new FormData();
    const avatarFile = document.getElementById('image_input').files[0];

    if (!avatarFile) {
        console.error("Файл аватара не выбран");
        return;
    }

    formData.append('avatar', avatarFile); // Добавляем файл в FormData

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
