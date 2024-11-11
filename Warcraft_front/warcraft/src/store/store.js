import {configureStore} from '@reduxjs/toolkit';
import authReducer from './authSlice.js';
import dataSlice from "./dataSlice.js";

export const store = configureStore({
    reducer: {
        [authReducer.name]: authReducer.reducer,
        [dataSlice.name]: dataSlice.reducer

    },
});

export default store;
