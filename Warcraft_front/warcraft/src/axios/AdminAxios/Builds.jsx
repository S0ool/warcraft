import axios from "axios";


export const getImages = async () => {
    try {
        const response = await axios.get('http://localhost:8000/api/v1/images/');
        return response.data;
    } catch (error) {
        console.error("Error fetching images:", error);
        throw error;
    }
};
export const deleteImage = async (id) => {
    try {
        const response = await axios.delete(`http://localhost:8000/api/v1/images/${id}/`);
        return response.data;
    } catch (error) {
        console.error("Error deleting image:", error);
        throw error;
    }
};
export const createImage = async (formData) => {
    try {
        const response = await axios.post('http://localhost:8000/api/v1/images/', formData);
        return response.data;
    } catch (error) {
        console.error("Error uploading image:", error);
        throw error;
    }
};
export const updateImage = async (id, formData) => {
    try {
        const response = await axios.put(`http://localhost:8000/api/v1/images/${id}/`, formData);
        return response.data;
    } catch (error) {
        console.error("Error updating image:", error);
        throw error;
    }
};
export const getImage = async (id) => {
    try {
        const response = await axios.get(`http://localhost:8000/api/v1/images/${id}/`);
        return response.data;
    } catch (error) {
        console.error("Error fetching image:", error);
        throw error;
    }
};