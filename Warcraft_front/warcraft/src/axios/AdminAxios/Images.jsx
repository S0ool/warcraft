import axios from "axios";


export const getImagesAxios = async () => {
    try {
        const response = await axios.get('http://localhost:8000/api/v1/images/');
        return response.data;
    } catch (error) {
        console.error("Error fetching images:", error);
        throw error;
    }
};
export const deleteImageAxios = async (id) => {
    try {
        const response = await axios.delete(`http://localhost:8000/api/v1/images/${id}/`);
        return response.data;
    } catch (error) {
        console.error("Error deleting image:", error);
        throw error;
    }
};
export const createImageAxios = async (formData) => {
    try {
        const response = await axios.post('http://localhost:8000/api/v1/images/', formData);
        return response.data;
    } catch (error) {
        console.error("Error uploading image:", error);
        throw error;
    }
};
export const updateImageAxios = async (id, formData) => {
    try {
        const response = await axios.put(`http://localhost:8000/api/v1/images/${id}/`, formData);
        return response.data;
    } catch (error) {
        console.error("Error updating image:", error);
        throw error;
    }
};
export const getImageAxios = async (id) => {
    try {
        const response = await axios.get(`http://localhost:8000/api/v1/images/${id}/`);
        return response.data;
    } catch (error) {
        console.error("Error fetching image:", error);
        throw error;
    }
};