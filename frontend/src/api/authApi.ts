import axios from "axios";
import type { IUser } from "../types/auth";

const api = axios.create({
    baseURL: 'http://localhost:8000/api/auth',
    withCredentials: true,
});

export const authApi = {
    getMe: async (): Promise<IUser> => {
        const response = await api.get('/me');
        return response.data
    },

    register: async (username: string, login: string, password: string): Promise<void> => {
        await api.post('/register', { username, login, password});
    },

    login: async (login: string, password: string): Promise<IUser> => {
        const response = await api.post('/login', {login, password});
        return response.data;
    },

    logout: async (): Promise<void> => {
        await api.post('/logout');
    },
};