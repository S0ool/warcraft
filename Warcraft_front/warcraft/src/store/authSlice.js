import {createSlice} from '@reduxjs/toolkit';

const initialState = {
    isAuthenticated: !!localStorage.getItem('token'),
    token: localStorage.getItem('token') || null,
    isSuperUser: false,
};

const authSlice = createSlice({
    name: 'auth',
    initialState,
    reducers: {
        login: (state, action) => {
            state.isAuthenticated = true;
            state.token = action.payload.token;
            state.isSuperUser = action.payload.is_superuser;
            localStorage.setItem('token', action.payload.token);
        },
        logout: (state) => {
            state.isAuthenticated = false;
            state.token = null;
            state.isSuperUser = false;
            localStorage.removeItem('token');
        },
    },
});

export const {login, logout} = authSlice.actions;

export default authSlice;
