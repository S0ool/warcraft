import {createSlice} from '@reduxjs/toolkit';

const initialState = {
    sleepIcon: '../../public/UpgradableSkills/PNG/Sleep.png',
    charmIcon: '../../public/UpgradableSkills/PNG/Charm3.png',
};

const dataSlice = createSlice({
    name: 'data',
    initialState,
    reducers: {},
});

export default dataSlice;
